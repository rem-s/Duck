from abc import ABC, abstractmethod
import pyaudio #handling recording function
import wave #handling .wav file
from os import listdir, makedirs
import copy
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import *
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import numpy as np
import sys
import time
import datetime
from cv2 import cvtColor, COLOR_BGR2RGB

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
    
    def __init__(self, wfile="record.wav", dst="./", overwrite=False):
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
        self.__record_time = 5
        # file name
        self.__output_wavfile = wfile
        # index number of microphone
        self.__idevice = 1
        # format of audio
        self.__format = pyaudio.paInt16
        # monaural
        self.__nchannels = 1
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
        self.input_device_index = device_index
    
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
        self._timer.start(10) # call plot update func every 35ms
        
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
        self._timer.start(50) # call plot update func every 100ms
    
    def setActionTrig(self):
        pass
    
    def update(self):
        msg = self.tcp.receive(3)
        msg = int.from_bytes(msg, byteorder="big", signed=True)-100
       
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
        self._timer.stop()

class ImageWindow(BaseWindow):
    
    def __init__(self, tcp):
        self.tcp = tcp
        
        self.image_height = 60
        self.image_width = 80
        self.image_nchannel = 3
        self.payload_size = self.image_height*self.image_width*self.image_nchannel
        self.data = None
        self.setWindowLayout()
        
    def setWindowLayout(self):
        self._window = QMdiSubWindow()
        self._window.setWindowTitle("CameraImage")
        #image widget
        self._window.setWidget(pg.ImageView())
        self._widget = self._window.widget()
    
    def setTimer(self):
        self._timer = QtCore.QTimer()
        self._timer.timeout.connect(self.update)
        self._timer.start(50) # fps 15
        
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
        self._timer.start(50) # call plot update func every 60ms
        
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
    
    def __init__(self, tcp_sonic, tcp_acc, tcp_image, recorder):#windowList=[voiceWin=None, imageWin=None, sensorWin=None]):
        
        super().__init__()
        self.mdi = QMdiArea()
        #self.setGeometry(self.window_x, self.window_y, self.width, self.height)
        #self.mdi.subWindowActivated.connect(self.setTimers)
        self.setCentralWidget(self.mdi)
        
        ### setting for sensors instance
        self._voiceWin = VoiceWindow(recorder)
        self._sonicWin = SonicWindow(tcp_sonic)
        self._accWin = AccWindow(tcp_acc)
        self._imageWin = ImageWindow(tcp_image)
        
        subWindowList = [self._voiceWin, self._sonicWin, self._accWin, self._imageWin]
        
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
        if action.text() == "Cascade":
            self.mdi.cascadeSubWindows()
        elif action.text() == "Tiled":
            self.mdi.tileSubWindows()
        elif action == self.exitAction:
            print("Debug print from mainmenu")
    