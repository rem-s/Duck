from abc import ABC, abstractmethod

class VoiceRecorder(object):
    #recording functionality
    import pyaudio #handling recording function
    import wave #handling .wav file
    from os import listdir, makedirs
    
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
        # sampling rate,which is usually 16KHz In case of raspberryPi, you need 44.1kHz instread
        self.__sampling_rate = 44100 #8192*2
        # number of extracted data at a time,that is called chunk, mostly 1024 Byte at a time
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
            input_device_index = self.__idevice, # device1(Mouse_mic) will be used for input device
            frames_per_buffer = self.__chunk,
            stream_callback = self.callback
        )
        self.callback_on = True
        self.byte_data = bytearray()
        self.__stream.start_stream()
        
        self.prev = 0
        self.next = self.__chunk*2
    
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
        if self.callback_on == True:
            self.byte_data.extend(in_data)
            #print("byte_data = ", len(self.byte_data)/2048)
        return (None, pyaudio.paComplete)
    
    def showDeviceInfo(self):
        for i in range(self.__audio.get_device_count()):
            print(self.__audio.get_device_info_by_index(i))
    
    def getStream(self):
        return self.__stream
    
    def getByteData(self, begin, end):
        return self.byte_data[begin:end]
        
    def getChunk(self):
        return self.__chunk
    
    def getAudioFileList(self):
        return self.__output_wavfile
    
    def makeWavFile(self, frames, wfile, mode='wb'):
        wavefile = wave.open(wfile, mode)
        wavefile.setnchannels(self.__nchannels)
        wavefile.setsampwidth(self.__audio.get_sample_size(self.__format))
        wavefile.setframerate(self.__sampling_rate)
        wavefile.writeframes(bytes(frames))
        wavefile.close()
        return wfile

    def closeAll(self):
        #stop and close audio stream
        self.__stream.stop_stream()
        self.__stream.close()
        self.__audio.terminate()
        #make wav file that is made of stream byte data
        self.make_wav_file(self.byte_data, self.__output_wavfile)
        print("pyaudio was terminated")

### end of VoiceRecorder

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

class VoiceWindow(BaseWindow):
    
    def __init__(self, recorder):
        self._recorder = recorder
        self.chunk = self._recorder.getChunk()
        self.plot_data = np.zeros(self.chunk*2)
        
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
        self._widget.setTitle("Operator voice", color="r", italic=True)
        self._widget.setXRange(0, 1024)
        self._widget.setYRange(-1, 1)
        self._widget.showGrid(x=True, y=True)

    def setTimer(self):
        self._timer = QtCore.QTimer()
        self._timer.timeout.connect(self.update)
        self._timer.start(200) # call plot update func every 100ms
        """
        self.stop_timer = QtCore.QTimer()
        self.stop_timer.timeout.connect(self.close_all)
        self.stop_timer.start(1000*self.__record_time) # plot stops when record time passes
        """
    
    def setActionTrig(self, action):
        pass
    
    def update(self):
        self._recorder.getStream().stop_stream()
        ### critical section start ###
        next_plot = np.frombuffer(bytes(self._recorder.getByteData(self.prev, self.next)), dtype="int16") / 2**16
        self.plot_data = np.append(self.plot_data, next_plot) # Add new 1024 elements to last
        ### critical section end ###
        self._recorder.getStream().start_stream()
        self.prev = self.next
        self.next = self.prev + self.chunk*2
        
        self._widget.clear()
        if len(self.plot_data)/self.chunk > 5:
            self.plot_data = self.plot_data[self.chunk:] # Remove first 1024 elements
            #print(len(self.plot_data)/1024)
            self._widget.plot().setData(self.plot_data, pen="y")
    
    def getWindow(self):
        return self._window
    
    def getWidget(self):
        return self._widget
    
    def closeWindow(self):
        #stop Qtimer threads
        self._timer.stop() 
        #self.stop_timer.stop()
        
class SonicWindow(BaseWindow):
    
    def __init__(self, tcp):
        self.tcp = tcp
        self.xrange_max = 20
        self.yrange_max = 100
        self.prev = 0
        self.sonicDistanceList = np.zeros(self.xrange_max)
        self.setWindowLayout()
        
    def setWindowLayout(self):
        self._window = QMdiSubWindow()
        self._window.setWindowTitle("Ultrasonic distance")
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
        
        if msg-self.prev > 0:
            d = np.linspace(self.prev, msg, self.xrange_max)
        else:
            d = np.linspace(msg, self.prev, self.xrange_max)
        
        self.prev = msg
        self.sonicDistanceList = np.append(self.sonicDistanceList, d)
        #print("sonicList = ", len(self.sonicDistanceList)//50)
        
        if len(self.sonicDistanceList)%(self.xrange_max) == 0:
            self.sonicDistanceList = self.sonicDistanceList[self.xrange_max:]
        
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
    
    def __init__(self):
        # load the image
        image1 = Image.open('icon.jpg')
        image2 = Image.open('kirakira.jpg')
        # convert image to numpy array
        self.data1 = np.asarray(image1)
        self.data2 = np.asarray(image2)
        sef.imgList = [self.data1, self.data2]
        
        self.count = 0
        
    def setWindowLayout(self):
        self._window = QMdiSubWindow()
        self._window.setWindowTitle("CameraImage")
        #image widget
        self._window.setWidget(pg.ImageView())
        self._widget = self._window.widget()
    
    def setTimer(self):
        self._timer = QtCore.QTimer()
        self._timer.timeout.connect(self.update)
        self._timer.start(3000) # fps 15
    
    def setActionTrig(self):
        pass
    
    def update(self):
        global count, imgList
        data = imgList[count]
        self._widget.setImage(data)
        #count = (count + 1)%2
    
    def getWindow(self):
        return self._window
    
    def getWidget(self):
        return self._widget
    
    def closeWindow(self):
        #stop Qtimer threads
        self._timer.stop()

class AccWindow(BaseWindow):
    
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

#recording functionality
import pyaudio #handling recording function
import wave #handling .wav file
from os import listdir, makedirs
#plotting functionality
from PyQt5.QtWidgets import *#QMainWindow, QApplication, QWidget, QWidgetAction, QAction, QPushButton, qApp, QMdiArea
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import *
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import numpy as np
import sys
import time
import random
from PIL import Image

"""
print(type(data))
# summarize shape
print(data.shape)

# create Pillow image
image2 = Image.fromarray(data)
print(type(image2))

# summarize image details
print(image2.mode)
print(image2.size)
"""
def DebugTrig():
    print("this is DegugTrig")
    
class QtMultiWindow(QMainWindow):
    
    def __init__(self, tcp, recorder):#windowList=[voiceWin=None, imageWin=None, sensorWin=None]):
        
        super().__init__()
        self.mdi = QMdiArea()
        #self.setGeometry(self.window_x, self.window_y, self.width, self.height)
        #self.mdi.subWindowActivated.connect(self.setTimers)
        self.setCentralWidget(self.mdi)
        
        ### setting for sensors instance
        self._tcp = tcp
        self._voiceWin = VoiceWindow(recorder)
        #self._imageWin = ImageWindow()
        self._sonicWin = SonicWindow(tcp)
        subWindowList = [self._voiceWin, self._sonicWin]# self._imageWin]
        
        self.setWindowLayout()
        
        # addSubwindow to mdi system
        for subwin in subWindowList:
            if subwin is not None:
                self.mdi.addSubWindow(subwin.getWindow())
                subwin.getWidget().show()
                subwin.setTimer()
        
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
    from tcp import TCP
    
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    
    tcp = TCP("192.168.0.142", 8889, server_flag=True)
    recorder = VoiceRecorder()
    
    win = QtMultiWindow(tcp, recorder)
    
    win.show()
    #print(win.get_device_info())
    #app.aboutToQuit.connect(app.deleteLater)
    sys.exit(app.exec_())