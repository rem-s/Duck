from abc import ABC, abstractmethod
###recording functionality###
import pyaudio #handling recording function
import wave #handling .wav file
from os import listdir, makedirs
import copy
###plotting functionality###
from PyQt5.QtWidgets import *#QMainWindow, QApplication, QWidget, QWidgetAction, QAction, QPushButton, qApp, QMdiArea
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import *
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import numpy as np
import sys
import time
#import random
import datetime
#from PIL import Image
from cv2 import cvtColor, COLOR_BGR2RGB
import random

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

### end of BaseWindow

class VoiceRecorder(object):
    
    def __init__(self, record_time, nchannels, sr=16000, wfile="record.wav", dst="./", overwrite=False, idevice=1):
        # dst must be ended with "/"
        if dst[-1] != "/":
            print("Destination must be ended with \"/\"")
            raise NotADirectoryError
        # check if dst already exists. If doesn't, make new dir
        makedirs(dst, exist_ok=True)
        # overwrite flag enables your record files not to be overwritten, if overwrite is False
        if overwrite == False and set.intersection(set(wfile), listdir(dst)) != set():
            print("Same wavfile exists in {0}\nYou were about to overwrite {1}\nIf you wouldn't mind it, set overwrite flag True".format(dst, dst+w))
            raise FileExistsError
        
        # recording time (unit: s)
        self.__record_time = record_time
        # file name
        self.__output_wavfile = wfile
        # index number of microphone
        self.__idevice = idevice
        # format of audio
        self.__format = pyaudio.paInt16
        # monaural
        self.__nchannels = nchannels
        # sampling rate,which is usually 16KHz In terms of raspberryPi, you need 44.1kHz instread
        self.__sampling_rate = 44100 #8192*2
        # number of frame to extract at a time,that is called chunk,
        self.__chunk = 1024
        # get device information
        self.__audio = pyaudio.PyAudio()
        # instance of stream obj for making wav file
        #audio.open() method returns a new Stream instance taking some arguments for configuration
        self.__stream = self.__audio.open(
            format = self.__format,
            channels = self.__nchannels,
            rate = self.__sampling_rate,
            input = True,
            output = False,
            input_device_index = self.__idevice,
            frames_per_buffer = self.__chunk,
            stream_callback = self.callback
        )
        self.callback_on = True
        self.byte_data = bytearray()
        self.__stream.start_stream()
    
    def setConfig(self, time_sec=3, outfile=["record.wav"], device_index=1, sampling_rate=44100, chunk=2**10, \
                   format=pyaudio.paInt16, nchannels=1):
        # configure foundimental information
        
        # recording time (unit: s)
        self.__record_time = time_sec
        # file name
        self.__output_wavfile = outfile
        # index number of microphone
        self.__idevice = device_index
        # sampling rate,which is usually 16kHz
        self.__sampling_rate = sampling_rate
        # number of extracted data at a time,that is called chunk
        self.__chunk = chunk
        # format of audio
        self.__format = format
        # monaural
        self.__nchannels = nchannels
        
    def callback(self, in_data, frame_count, time_info, status):
        #print(len(in_data), frame_count) #=> class "bytes", class "int"
        #if self.callback_on == True:
        self.byte_data.extend(in_data)
        #print("callback time", datetime.time())
        return (None, pyaudio.paContinue)
    
    def setDeviceIndex(self, device_index):
        self.__idevice = device_index
    
    def getDeviceIndex(self):
        audio_device_dict = {}
        for i in range(self.__audio.get_device_count()):
            audio_device_dict[i] = self.__audio.get_device_info_by_index(i)['name']
        return audio_device_dict
    
    def getRecordInfo(self):
        return (self.__idevice, self.__record_time, self.__sampling_rate, self.__format, self.__nchannels)
    
    def getStream(self):
        return self.__stream
    
    def getRecordTime(self):
        return self.__record_time
    
    def getByteData(self, begin, end):
        #print("getByteData: ", type(self.byte_data[begin:end]), len(self.byte_data[begin:end]))
        return copy.deepcopy(self.byte_data[begin:end])
        
    def getChunk(self):
        return self.__chunk
    
    def getAudioFileList(self):
        return self.__output_wavfile
    
    def makeWavFile(self, frames, wfile, mode='wb'):
        wavefile = wave.open(wfile, mode)
        wavefile.setnchannels(self.__nchannels)
        wavefile.setsampwidth(self.__audio.get_sample_size(self.__format))
        wavefile.setframerate(self.__sampling_rate)
        #print("frame length: ", len(frames)) #frame lengthとbyte data lengthは同じだった
        #print("byte data: ", len(bytes(frames)))
        wavefile.writeframes(bytes(frames))
        wavefile.close()
        return wfile
    
    def closeAll(self):
        #stop and close audio stream
        self.__stream.stop_stream()
        self.__stream.close()
        self.__audio.terminate()
        #make wav file that is made of stream byte data
        self.makeWavFile(self.byte_data, self.__output_wavfile)
        print("pyaudio was terminated")

### end of VoiceRecorder

class VoiceWindow(BaseWindow):
    
    def __init__(self, recorder):
        super().__init__()
        self._recorder = recorder
        self.chunk = self._recorder.getChunk()
        self.plot_data = np.zeros(self.chunk*2)
        
        self.xrange_max = self.chunk
        self.prev = 0
        self.next = self.chunk*2
        
        self.setWindowLayout()
    
    def setWindowLayout(self):
        self._window = QMdiSubWindow()
        self._window.setWindowTitle("VoiceWaveform")
        self._window.setWidget(pg.PlotWidget())
        self._widget = self._window.widget()
        ### Background colors ###
        #blue  b
        #green g
        #red   r
        #cyan (bright blue-green) c
        #magenta (bright pink)    m
        #yellow y
        #black  k
        #white  w
        #########################
        self._widget.setBackground('k')
        self._widget.setTitle("OperatorVoice", color="r", italic=True)
        self._widget.setXRange(0, self.xrange_max)
        self._widget.setYRange(-1, 1)
        self._widget.showGrid(x=True, y=True)

    def setTimer(self):
        self._timer = QtCore.QTimer()
        self._timer.timeout.connect(self.update)
        self._timer.start(40) # call plot update func every 35ms
        
        self._stop_timer = QtCore.QTimer()
        self._stop_timer.timeout.connect(self.closeWindow)
        print("record start recording sec: ", self._recorder.getRecordTime())
        #self._stop_timer.start(1000*self._recorder.getRecordTime()) # plot stops when record time passes
    
    def setActionTrig(self, action):
        pass
    
    def update(self):
        next_plot = np.frombuffer(bytes(self._recorder.getByteData(self.prev, self.next)), dtype="int16") / 2**16
        self.plot_data = np.append(self.plot_data, next_plot) # Add new 1024 elements to last
        self.prev = self.next
        self.next = self.prev + self.chunk*2
        if len(self.plot_data)/self.chunk > 5:
#        if len(self.plot_data)%(self.chunk)==0:
            self._widget.clear()
            self.plot_data = self.plot_data[self.xrange_max:] # Remove first 1024 elements
            self._widget.plot().setData(self.plot_data, pen="y")
    
    def getWindow(self):
        return self._window
    
    def getWidget(self):
        return self._widget
    
    def closeWindow(self):
        #stop Qtimer threads
        self._timer.stop()
        #self._stop_timer.stop()
        #self._recorder.closeAll()

class MultiChannelMicWindow(BaseWindow):
    
    def __init__(self, recorder):
        super().__init__()
        self._recorder = recorder
        self.setWindowLayout()
    
    def setWindowLayout(self):
        self._window = QMdiSubWindow()
        self._window.setWindowTitle("SoundSourceDirection")
        self._window.setWidget(pg.GraphicsLayoutWidget(show=False))
        self._widget = self._window.widget().addPlot(row=0, col=0)
        #pg.PlotItem(pg.BarGraphItem(x=range(5), height=[1,5,2,4,3], width=0.5)
        ### Background colors ###
        #blue  b
        #green g
        #red   r
        #cyan (bright blue-green) c
        #magenta (bright pink)    m
        #yellow y
        #black  k
        #white  w
        #########################
        #self._widget.setBackground('b')
        self.dir = np.zeros(500)
        self.x = np.sin(np.linspace(0, 2*np.pi, 500))# * (0.2 * np.cos(np.linspace(0, 2*np.pi, 1000) * 32))
        self.y = np.cos(np.linspace(0, 2*np.pi, 500))# * (0.2 * np.cos(np.linspace(0, 2*np.pi, 1000) * 32))
        self.x_resolution = np.cos(np.linspace(0, 2*np.pi, 500) * 360)
        self.y_resolution = self.x_resolution
        #self._widget.setTitle("SoundSourceDirection", color="r", italic=True)
        self._widget.setXRange(-1, 1)
        self._widget.setYRange(-1, 1)
        #self._widget.showGrid(x=True, y=True)
        
    def setTimer(self):
        self._timer = QtCore.QTimer()
        self._timer.timeout.connect(self.update)
        self._timer.start(1000) # call plot update func every 35ms
        
        self._stop_timer = QtCore.QTimer()
        self._stop_timer.timeout.connect(self.closeWindow)
        print("record start recording sec: ", self._recorder.getRecordTime())
        #self._stop_timer.start(1000*self._recorder.getRecordTime()) # plot stops when record time passes
    
    def setActionTrig(self, action):
        pass
    
    def update(self):

        x = self.x * (0.5 + self.dir * self.x_resolution)
        y = self.y * (0.5 + self.dir * self.y_resolution)
        
        self._widget.clear()
        self._widget.plot(x=x, y=y)
        
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
        self.yrange_max = 100
        self.prev = 0
        self.sonicDistanceList = np.zeros(self.xrange_max)
        self.setWindowLayout()
        
    def setWindowLayout(self):
        self._window = QMdiSubWindow()
        self._window.setWindowTitle("UltrasonicDistance")
        self._window.setWidget(pg.PlotWidget())
        self._widget = self._window.widget()
        ### Background colors ###
        #blue  b
        #green g
        #red   r
        #cyan (bright blue-green) c
        #magenta (bright pink)    m
        #yellow y
        #black  k
        #white  w
        #########################
        self._widget.setBackground('k')
        self._widget.setTitle("distance[cm]", color="r", italic=True)
        self._widget.setXRange(0, self.xrange_max)
        self._widget.setYRange(0, self.yrange_max)
        self._widget.showGrid(x=True, y=True)
        
    def setTimer(self):
        self._timer = QtCore.QTimer()
        self._timer.timeout.connect(self.update)
        self._timer.start(60) # call plot update func every 100ms
    
    def setActionTrig(self):
        pass
    
    def update(self):
        msg = self.tcp.receive(3)
        msg = int.from_bytes(msg, byteorder="big", signed=True)-100
        #msg = np.frombuffer(msg, dtype="int16")
        
        """
        #プロットするグラフを単調増加か単調減少かにする
        # self.prevからmsgの差分をself.xrange_max個に分ける
        if msg-self.prev > 0:
            d = np.linspace(self.prev, msg, self.xrange_max)
        else:
            d = np.linspace(msg, self.prev, self.xrange_max)
        #前回の距離を記憶
        self.prev = msg
        self.sonicDistanceList = np.append(self.sonicDistanceList, d)
        """
        
        self.sonicDistanceList = np.append(self.sonicDistanceList, np.array(msg))
        
        if len(self.sonicDistanceList)%(self.xrange_max//2) == 0:
            self.sonicDistanceList = self.sonicDistanceList[self.xrange_max//2:]
        
        self._widget.clear()
        self._widget.plot().setData(self.sonicDistanceList, pen="c")
    
    def getWindow(self):
        return self._window
    
    def getWidget(self):
        return self._widget
    
    def closeWindow(self):
        #stop Qtimer threads
        self._timer.stop()
        #print(self.sonicDistanceList)

### end of SensorWindow

class ImageWindow(BaseWindow):
    
    def __init__(self, tcp):
        self.tcp = tcp
        
        self.image_height = 600
        self.image_width = 800
        self.image_nchannel = 3
        self.payload_size = self.image_height*self.image_width*self.image_nchannel
        self.data = None
        self.setWindowLayout()
        
    def setWindowLayout(self):
        self._window = QMdiSubWindow()
        self._window.setWindowTitle("CameraImage")
        #image widget
        self._window.setWidget(pg.ImageView())#pg.ImageView(view=pg.PlotItem()))
        self._widget = self._window.widget()
    
    def setTimer(self):
        self._timer = QtCore.QTimer()
        self._timer.timeout.connect(self.update)
        self._timer.start(100) # fps 15
        
    def setActionTrig(self):
        pass
    
    def update(self):
        self.data = b""
        #self.tcp.setBlockingMode(True)
        #self.tcp.setTimeout(None)
        while len(self.data) < self.payload_size:
            #print("Recv: {}".format(len(data)))
            self.data += self.tcp.receive(self.payload_size-len(self.data))
        self.data = np.frombuffer(self.data, dtype='uint8')
        ### decode image and reshape that into heigt*width*channel ###
        
        #imageBGR = cv2.imdecode(self.data, cv2.IMREAD_COLOR).reshape((self.image_height, self.image_width, self.image_nchannel))
        
        self.data = self.data.reshape((self.image_height, self.image_width, self.image_nchannel))
        self.data = cvtColor(self.data, COLOR_BGR2RGB)
        self.data = self.data.transpose(1, 0, 2)
        
        #qimage = QtGui.QImage(self.data, self.image_width, self.image_height, self.image_width * 4, QtGui.QImage.Format_ARGB32_Premultiplied)
        #pixmap = QtGui.QPixmap.fromImage(qimage);
        
        #self.image = Image.fromarray(self.data)
        #self._widget.image(self.data)
        self._widget.setImage(self.data)
        self._widget.getImageItem().dataTransform()
        #print(pixmap, pixmap.shape)
        
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
        self.yrange_max = 100
        self.prev = 0
        self.x_accList = np.zeros(self.xrange_max)
        self.y_accList = np.zeros(self.xrange_max)
        self.z_accList = np.zeros(self.xrange_max)
        self.setWindowLayout()
    
    def setWindowLayout(self):
        self._window = QMdiSubWindow()
        self._window.setWindowTitle("AccelerationSensorValues")
        self._window.setWidget(pg.PlotWidget())
        self._widget = self._window.widget()
        ### Background colors ###
        #blue  b
        #green g
        #red   r
        #cyan (bright blue-green) c
        #magenta (bright pink)    m
        #yellow y
        #black  k
        #white  w
        #########################
        self._widget.setBackground('k')
        self._widget.setTitle("3axisAcc", color="r", italic=True)
        self._widget.setXRange(0, self.xrange_max)
        self._widget.setYRange(self.yrange_max*-1, self.yrange_max)
        self._widget.showGrid(x=True, y=True)
        
    def setTimer(self):
        self._timer = QtCore.QTimer()
        self._timer.timeout.connect(self.update)
        self._timer.start(60) # call plot update func every 60ms
        
    def setActionTrig(self):
        pass
    
    def update(self):
        x_acc = self.tcp.receive(3)
        x_acc = int.from_bytes(x_acc, byteorder="big", signed=True)-150
        
        y_acc = self.tcp.receive(3)
        y_acc = int.from_bytes(y_acc, byteorder="big", signed=True)-150
        
        z_acc = self.tcp.receive(3)
        z_acc = int.from_bytes(z_acc, byteorder="big", signed=True)-150
        
        self.x_accList = np.append(self.x_accList, np.array(x_acc))
        self.y_accList = np.append(self.y_accList, np.array(y_acc))
        self.z_accList = np.append(self.z_accList, np.array(z_acc))
        
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
    
    def __init__(self, recorder=[], mc_recorder=[], tcp_sonic=None, tcp_acc=None, tcp_image=None):#windowList=[voiceWin=None, imageWin=None, sensorWin=None]):
        
        super().__init__()
        self.mdi = QMdiArea()
        #self.setGeometry(self.window_x, self.window_y, self.width, self.height)
        #self.mdi.subWindowActivated.connect(self.setTimers)
        self.setCentralWidget(self.mdi)
        
        self.subWindowList = []
        ### setting for sensors instance
        if tcp_sonic:
            self._sonicWin = SonicWindow(tcp_sonic)
            self.subWindowList.append(self._sonicWin)
        if tcp_acc:
            self._accWin = AccWindow(tcp_acc)
            self.subWindowList.append(self._accWin)
        if tcp_image:
            self._imageWin = ImageWindow(tcp_image)
            self.subWindowList.append(self._imageWin)
        if recorder is not []:
            for rec in recorder:
                self.subWindowList.append(VoiceWindow(rec))
                #subWindowList.append(self._voiceWin)
        if mc_recorder is not []:
            for rec in mc_recorder:
                self.subWindowList.append(MultiChannelMicWindow(rec))
            #subWindowList.append(self._micWin)
        
        self.setWindowLayout()
        
        # addSubwindow to mdi system
        for subwin in self.subWindowList:
            if subwin is not None:
                self.mdi.addSubWindow(subwin.getWindow())
                subwin.getWidget().show()
                subwin.setTimer()
        
        self.mdi.tileSubWindows()
        
    def setWindowLayout(self):
        ### icon and title setting ###
        self.setWindowIcon(QIcon("REMsIcon.jpg"))
        self.setWindowTitle("QtMultiWindow")
        
        ### statusBar ###
        self.statusBar()
        
        ### menuBar ###
        menubar = self.menuBar()
        
        """
        # newAction
        self.voiceNewAction = QAction("New voice", self)
        #self.newAction.setShortcut("Crtl+N")
        self.voiceNewAction.setStatusTip("Create a voice wave window")
        # newAction
        self.cameraNewAction = QAction("New camera", self)
        #self.newAction.setShortcut("Crtl+N")
        self.cameraNewAction.setStatusTip("Create a camera window")
        
        self.sonicNewAction = QAction("New sonic", self)
        #self.newAction.setShortcut("Crtl+N")
        self.sonicNewAction.setStatusTip("Create a ultrasonic window")
        
        # closeAction
        self.closeAction = QAction("Close", self)
        #self.closeAction.setShortcut("Crtl+D")
        self.closeAction.setStatusTip("Close a subwindow") #選択しようとしたとき、status barにこれが表示される
        self.closeAction.triggered.connect(DebugTrig)#(qApp.quit)
        """
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
        
        """
        voice_tab = menubar.addMenu("Voice")
        voice_tab.addAction(self.voiceNewAction)
        voice_tab.addAction(self.closeAction)
        voice_tab.triggered[QAction].connect(self.voiceActionTrig)
        
        cam_tab = menubar.addMenu("Camera")
        cam_tab.addAction(self.cameraNewAction)
        cam_tab.addAction(self.closeAction)
        cam_tab.triggered[QAction].connect(self.cameraActionTrig)
        
        sonic_tab = menubar.addMenu("Sonic")
        sonic_tab.addAction(self.sonicNewAction)
        sonic_tab.addAction(self.closeAction)
        sonic_tab.triggered[QAction].connect(self.sonicActionTrig)
        """
        
    def setActionTrig(self, action):
        if action.text() == "Cascade":
            self.mdi.cascadeSubWindows()
        elif action.text() == "Tiled":
            self.mdi.tileSubWindows()
        elif action == self.exitAction:
            print("Debug print from mainmenu")
    
#end of class VoicePlotWindow
if __name__=="__main__":
    
    from PyQt5.QtGui import QApplication
    from tcp_server import TCP
    
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    
    server_ip = "192.168.0.192"
    # tcp_for_sonic = TCP(server_ip, 8887, server_flag=True)
    # tcp_for_acc = TCP(server_ip, 8888, server_flag=True)
    # tcpi = TCP(server_ip, 8889, server_flag=True)
    # recorder = VoiceRecorder(record_time=5)
    # recorder.setDeviceIndex(1)

    rec1 = VoiceRecorder(record_time=5, nchannels=2, idevice=2) # nchannel=2 per port port numbers are 1,2
    rec1.getDeviceIndex()
    #rec2 = VoiceRecorder(record_time=5, nchannels=2, idevice=3) # nchannel=2 per port port numbers are 1,2
    # #recorder.getDeviceIndex()
    win = QtMultiWindow(mc_recorder=[rec1]) 
    #win = QtMultiWindow(tcp_image=tcpi)#tcp_for_sonic, tcp_for_acc, tcp_for_image, recorder)
    
    win.show()
    #print(win.get_device_info())
    #app.aboutToQuit.connect(app.deleteLater)
    sys.exit(app.exec_())