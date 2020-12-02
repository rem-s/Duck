#モジュールインポート
from abc import ABC, abstractmethod
import pyaudio
import wave
from os import listdir, makedirs
import copy
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import *
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import os
import cv2
import sys
import time
import math
import datetime
import numpy as np
from PIL import Image
from collections import deque

#pytorchフレームワーク
import torch
import torch.nn as nn
import torch.optim as optim
import torch.utils.data as data
import torchvision
from torchvision import models, transforms
from torchvision.transforms import functional as F

#画像用API
from model.SEGNET import *
from model.transform import *
from model.IPU import *

class BaseWindow(ABC):
    
    def __init__(self):
        pass
    
    def setWindowLayout(self):
        pass
    
    def setTimer(self):
        pass
    
    def setActionTrig(self):
        pass
    
    def update(self):
        pass
    
    def getWindow(self):
        pass
    
    def getWidget(self):
        pass
    
    def closeWindow(self):
        pass

class MultiChannelMicWindow(BaseWindow):
    
    def __init__(self, tcp_sound):
        super().__init__()
        self.tcp = tcp_sound
        self.dsize_sensor = 3

        self.radians = math.pi / 180
        self.theta_max = 90 # direction-axis on positive coordinate
        self.nbins = 16  # number of bins to get orientation resolution
        self.direction = np.zeros(self.theta_max*2)
        self.resolution = len(self.direction) // self.nbins
        
        self.radius = 90 # y-axis max
        self.r_width = self.radius // 10 # 10 of sub-radius
        
        self.Q = deque()
        self.x_list = []
        self.y_list = []
        self.n_update = 0

        self.setWindowLayout()
    
    def setWindowLayout(self):

        self._window = QMdiSubWindow()
        self._window.setWindowTitle("SoundSourceDirection")
        self._window.setWidget(pg.GraphicsLayoutWidget())
        self._widget = self._window.widget().addPlot()
        self._widget.setTitle("Sound Localization", color="w", italic=False)

        self._widget.setXRange(-self.theta_max, self.theta_max)#(-180, 180)
        self._widget.setYRange(1, self.theta_max) # yrange_max = radius
        
    def setTimer(self):
        self._timer = QtCore.QTimer()
        self._timer.timeout.connect(self.update)
        self._timer.start(1)
        
        self._stop_timer = QtCore.QTimer()
        self._stop_timer.timeout.connect(self.closeWindow)
    
    def setActionTrig(self, action):
        pass
    
    def update(self):

        dir = b""
        while len(dir) < self.dsize_sensor: dir += self.tcp.receive(self.dsize_sensor)
        dir = int.from_bytes(dir, 'big')
        
        print('dir', dir)
        if dir > 180: return
        theta = dir // 10 * 10
        if self.n_update < 128:
            self.Q.append(theta) # append right
            self.n_update = self.n_update + 1
        else:
            self.direction[self.Q.popleft()] -= 1 # remove old
            self.Q.append(theta) # append right

        self.direction[theta] = min(self.direction[theta]+1, 10)
        
        self._widget.clear()
        for r in range(0, self.radius+1, self.r_width):
            x = r * np.cos(np.linspace(0, 2*np.pi, 100))
            y = r * np.sin(np.linspace(0, 2*np.pi, 100))
            self._widget.plot(x, y, pen=pg.mkColor('c'))
        
        self.x_list = []
        self.y_list = []
        for theta in self.Q:
            # Transform to cartesian and plot
            x = self.r_width * self.direction[theta] * math.cos(self.radians*theta)
            y = self.r_width * self.direction[theta] * math.sin(self.radians*theta)
            self.x_list.append(int(x))
            self.y_list.append(int(y))
        
        self._widget.plot(self.x_list, self.y_list, symbol='o', symbolSize=10, symbolPen=(255,255,255,200), symbolBrush=(0,0,255,150))
        
    def getWindow(self):
        return self._window
    
    def getWidget(self):
        return self._widget
    
    def closeWindow(self):
        #stop Qtimer threads
        self._timer.stop()
        self._stop_timer.stop()
        self._recorder.closeAll()

class SonicWindow(BaseWindow):
    
    def __init__(self, tcp):
        self.tcp = tcp
        self.xrange_max = 50
        self.yrange_max = 500
        self.prev = 0
        self.dsize_sensor = 3
        self.sonicDistanceList = np.zeros(self.xrange_max)
        self.setWindowLayout()
        
    def setWindowLayout(self):
        self._window = QMdiSubWindow()
        self._window.setWindowTitle("UltrasonicDistance")
        self._window.setWidget(pg.PlotWidget())
        self._widget = self._window.widget()
        self._widget.setBackground('k')
        self._widget.setTitle("distance[cm]", color="r", italic=True)
        self._widget.setXRange(0, self.xrange_max)
        self._widget.setYRange(0, self.yrange_max)
        self._widget.showGrid(x=True, y=True)
        
    def setTimer(self):
        self._timer = QtCore.QTimer()
        self._timer.timeout.connect(self.update)
        self._timer.start(1)
    
    def setActionTrig(self):
        pass
    
    def update(self):

        sonic = b""
        while len(sonic) < self.dsize_sensor: sonic += self.tcp.receive(self.dsize_sensor)
        sonic = int.from_bytes(sonic, 'big')

        self.sonicDistanceList = np.append(self.sonicDistanceList, np.array(sonic))
        if len(self.sonicDistanceList)%(self.xrange_max//2) == 0:
            self.sonicDistanceList = self.sonicDistanceList[self.xrange_max//2:]
        
        self._widget.clear()
        self._widget.plot().setData(self.sonicDistanceList, pen="c")
    
    def getWindow(self):
        return self._window
    
    def getWidget(self):
        return self._widget
    
    def closeWindow(self):
        self._timer.stop()

class ImageWindow(BaseWindow):
    
    def __init__(self, tcp):
        self.tcp = tcp
        self.dsize_sensor = 3
        self.height, self.width, self.channel, self.label = int(128/2), int(416/2), 3, 1
        self.dsize_img = self.height*self.width*self.channel
        self.data = None
        self.setWindowLayout()

        #モデル読み込み
        self.transform = ImageTransform((self.height, self.width))
        self.net = SEGNET(self.channel, self.label)
        self.net.load_state_dict(torch.load("./model/model.pt", map_location=torch.device('cpu')))
        
    def setWindowLayout(self):
        self._window = QMdiSubWindow()
        self._window.setWindowTitle("CameraImage")
        self._window.setWidget(pg.ImageView())
        self._widget = self._window.widget()
    
    def setTimer(self):
        self._timer = QtCore.QTimer()
        self._timer.timeout.connect(self.update)
        self._timer.start(1)
        
    def setActionTrig(self):
        pass
    
    def update(self):

        #画像受信
        name = int(time.time()*100)
        img = b""
        while len(img) < self.dsize_img: img += self.tcp.receive(256)
        narray = np.frombuffer(img, dtype='uint8')
        narray = narray.reshape((self.height, self.width, self.channel))
        narray = cv2.cvtColor(narray, cv2.COLOR_BGR2RGB)
        img_input = Image.fromarray(np.uint8(narray))
        img_input = self.transform(img_input, phase="test", height=self.height, width=self.width)

        #画像判定
        outputs = self.net(img_input)
        i = np.clip(img_input.numpy()[0], 0, 1)
        o = np.clip(outputs.detach().numpy()[0][0], 0, 1) 
        i[1, :, :] += o

        #角度算出
        o = np.where(o > 0.5, 0, 1)
        l_img = labeling(o)
        r_img = compare_area(l_img)
        degree, grav = grav_degree(r_img)
        degree = degree.to_bytes(self.dsize_sensor, 'big', signed=True) 
        self.tcp.send(degree)

        #画像保存
        #cv2.imwrite('Image/raw/%d.jpg'%(name), narray, [cv2.IMWRITE_JPEG_QUALITY, 100])
        #cv2.imwrite('Image/seg/%d.jpg'%(name), np.where(o == 1, 0, 255))

        #画像表示
        self.data = np.clip(i*255, 0, 255).astype(np.uint8).transpose(2, 1, 0)
        self._widget.setImage(self.data)
        self._widget.getImageItem().dataTransform()
        
    def getWindow(self):
        return self._window
    
    def getWidget(self):
        return self._widget
    
    def closeWindow(self):
        #stop Qtimer threads
        self._timer.stop()

### end of class ImageWindow
class AccWindow(BaseWindow):
    
    def __init__(self, tcp):
        self.tcp = tcp
        self.xrange_max = 50
        self.yrange_max = 128
        self.prev = 0
        self.dsize_sensor = 3
        self.x_accList = np.zeros(self.xrange_max)
        self.y_accList = np.zeros(self.xrange_max)
        self.z_accList = np.zeros(self.xrange_max)
        self.setWindowLayout()
    
    def setWindowLayout(self):
        self._window = QMdiSubWindow()
        self._window.setWindowTitle("AccelerationSensorValues")
        self._window.setWidget(pg.PlotWidget())
        self._widget = self._window.widget()
        self._widget.setBackground('k')
        self._widget.setTitle("3axisAcc", color="r", italic=True)
        self._widget.setXRange(0, self.xrange_max)
        self._widget.setYRange(self.yrange_max*-1, self.yrange_max)
        self._widget.showGrid(x=True, y=True)
        
    def setTimer(self):
        self._timer = QtCore.QTimer()
        self._timer.timeout.connect(self.update)
        self._timer.start(1)
        
    def setActionTrig(self):
        pass
    
    def update(self):

        acc = [b"",b"",b""] 
        for i in range(3):
            while len(acc[i]) < self.dsize_sensor: acc[i] += self.tcp.receive(self.dsize_sensor)
            acc[i] = int.from_bytes(acc[i], 'big', signed=True) 
        
        self.x_accList = np.append(self.x_accList, np.array(acc[0]))
        self.y_accList = np.append(self.y_accList, np.array(acc[1]))
        self.z_accList = np.append(self.z_accList, np.array(acc[2]))
        
        if len(self.x_accList)%(self.xrange_max//2) == 0:
            self.x_accList = self.x_accList[self.xrange_max//2:]
            
        if len(self.y_accList)%(self.xrange_max//2) == 0:
            self.y_accList = self.y_accList[self.xrange_max//2:]
            
        if len(self.z_accList)%(self.xrange_max//2) == 0:
            self.z_accList = self.z_accList[self.xrange_max//2:]
        
        self._widget.clear()
        self._widget.plot().setData(self.x_accList, pen="r")
        self._widget.plot().setData(self.y_accList, pen="g")
        self._widget.plot().setData(self.z_accList, pen="b")

    def getWindow(self):
        return self._window
    
    def getWidget(self):
        return self._widget
    
    def closeWindow(self):
        #stop Qtimer threads
        self._timer.stop()

### end of class AccWindow

def DebugTrig():
    print("this is DegugTrig")
    
class QtMultiWindow(QMainWindow):
    
    def __init__(self, tcp_sonic, tcp_acc, tcp_image, tcp_sound):
        
        super().__init__()
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        
        self._sonicWin = SonicWindow(tcp_sonic)
        self._accWin = AccWindow(tcp_acc)
        self._imageWin = ImageWindow(tcp_image)
        self._multWin = MultiChannelMicWindow(tcp_sound)
        subWindowList = [self._sonicWin, self._accWin, self._imageWin, self._multWin]
        
        self.setWindowLayout()
        
        # addSubwindow to mdi system
        for subwin in subWindowList:
            if subwin is not None:
                self.mdi.addSubWindow(subwin.getWindow())
                subwin.getWidget().show()
                subwin.setTimer()
        print("done")
        self.mdi.tileSubWindows()
        
    def setWindowLayout(self):
        ### icon and title setting ###
        self.setWindowIcon(QIcon("REMsIcon.jpg"))
        self.setWindowTitle("QtMultiWindow")
        
        ### statusBar ###
        self.statusBar()
        
        ### menuBar ###
        menubar = self.menuBar()
       
        # exitAction
        self.exitAction = QAction("Exit", self)
        self.exitAction.setShortcut("Crtl+Q")
        self.exitAction.setStatusTip("Exit REMs application") #選択しようとしたとき、status barにこれが表示される
        self.exitAction.triggered.connect(DebugTrig)#(qApp.quit)
        
        main_tab = menubar.addMenu("MainMenu")
        main_tab.addAction("Cascade")
        main_tab.addAction("Tiled")
        main_tab.addAction(self.exitAction)
        main_tab.triggered[QAction].connect(self.setActionTrig)

    def setActionTrig(self, action):
        if action.text() == "Cascade": self.mdi.cascadeSubWindows()
        elif action.text() == "Tiled": self.mdi.tileSubWindows()
        elif action == self.exitAction: print("Debug print from mainmenu")
    