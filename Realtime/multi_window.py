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

class VoicePlotWindow(QMainWindow):
    #constructor
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
        
        super().__init__()
        self.mdi = QMdiArea()
        #self.mdi.setBackGround()
        self.initUI()
        
        # recording time (unit: s)
        self.__record_time = 5*2
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
        self.byte_data = bytearray()
        self.callback_on = True
        self.__stream.start_stream()
        
        self.plot_data = np.zeros(self.__chunk*2)
        self.prev = 0
        self.next = self.__chunk*2
        
    def initUI(self):
        self.setWindowIcon(QIcon("REMsIcon.jpg"))
        self.title = "RealtimeVoicePlot"
        self.setWindowTitle(self.title)
        self.setCentralWidget(self.mdi)
        #self.mdi.subWindowActivated.connect(self.setTimers)
        #self.menuBar()
        self.statusBar()
        self.setWindowLayout()
        #self.setGeometry(self.window_x, self.window_y, self.width, self.height)
        
    def setWindowLayout(self):
        ### menu bar ###
        
        # newAction
        self.newAction = QAction("New", self)
        self.newAction.setShortcut("Ctr+N")
        self.newAction.setStatusTip("Make a new window")
        # exitAction
        self.exitAction = QAction("Exit", self)
        self.exitAction.setShortcut("Crtl+Q")
        self.exitAction.setStatusTip("Close the window") #選択しようとしたとき、status barにこれが表示される
        self.exitAction.triggered.connect(self.DebugTrig)#(qApp.quit)
        """
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        """
        menubar = self.menuBar()
        win_tab = menubar.addMenu("Voice")
        win_tab.addAction(self.newAction)
        win_tab.addAction("Cascade")
        win_tab.addAction("Tiled")
        win_tab.addAction("Update")
        win_tab.addAction(self.exitAction)
        win_tab.triggered[QAction].connect(self.WindowTrig)
        
        file_tab = menubar.addMenu("Camera")
        file_tab.addAction("New")
        file_tab.addAction("Edit")
        file_tab.addAction("Close")
        file_tab.addAction(self.exitAction)
        file_tab.triggered[QAction].connect(self.WindowTrig)
    
    def setTimers(self):
        self.update_timer = QtCore.QTimer()
        self.update_timer.timeout.connect(self.update)
        self.update_timer.start(100) # call plot update func every 100ms
        
        """
        self.stop_timer = QtCore.QTimer()
        self.stop_timer.timeout.connect(self.close_all)
        self.stop_timer.start(1000*self.__record_time) # plot stops when record time passes
        """
        
    def DebugTrig(self):
        print("Debug print")
        
    def WindowTrig(self, p):
        if p == self.newAction:
            sub = QMdiSubWindow()
            sub.setWindowTitle("Sub Window")
            #sub.setWidget(pg.GraphicsWindow())
            sub.setWidget(pg.PlotWidget())
            self.mdi.addSubWindow(sub)
            sub.widget().setXRange(0, 1024)
            sub.widget().setYRange(-1,1)
            sub.show()
            self.setTimers()
            print("New window activated...")

        elif p.text() == "Cascade":
            self.mdi.cascadeSubWindows()
        elif p.text() == "Tiled":
            self.mdi.tileSubWindows()
        elif p.text() == "Update":
            self.update()
    
    def callback(self, in_data, frame_count, time_info, status):
        #print(len(in_data), frame_count) #=> class "bytes", class "int"
        if self.callback_on == True:
            self.byte_data.extend(in_data)
            #print("byte_data = ", len(self.byte_data)/2048)
        return (None, pyaudio.paComplete)
    
    def update(self):
        self.__stream.stop_stream()
        ### critical section start ###
        next_plot = np.frombuffer(bytes(self.byte_data[self.prev:self.next]), dtype="int16") / 2**15
        #self.plot_data = next_plot
        self.plot_data = np.append(self.plot_data, next_plot)
        #print("byte_data = ", len(self.byte_data[self.prev:self.next])/2048)
        #print("plot_data = ", self.plot_data.shape)
        ### critical section end ###
        self.__stream.start_stream()
        self.prev = self.next
        self.next = self.prev + self.__chunk*2
        
        self.subWindow_list = self.mdi.subWindowList()
        for swin in self.subWindow_list:
            iswid = swin.widget()
            iswid.clear()
            #iswid.plot([1,2,3,4,5,6,7,8,9,10], [random.uniform(-1.0, 1.0) for _ in range(10)])
            #iswid.plot([ _ for _ in range(len(self.plot_data))], self.plot_data[self.prev:self.next]) # plot the data
            #iswid.plot(self.plot_data[self.prev:self.next-self.__chunk])
            if len(self.plot_data)/1024 > 5:
                self.plot_data = self.plot_data[1024:]
                #print(len(self.plot_data)/1024)
                iswid.plot(clear=False).setData(self.plot_data, clear=False, pen="y")
                #pg.GraphicsWindow().addPlot().plot().setData()
            
    def get_device_info(self):
        for i in range(self.__audio.get_device_count()):
            print(self.__audio.get_device_info_by_index(i))
         
    def make_wav_file(self, frames, wfile, mode='wb'):
        wavefile = wave.open(wfile, mode)
        wavefile.setnchannels(self.__nchannels)
        wavefile.setsampwidth(self.__audio.get_sample_size(self.__format))
        wavefile.setframerate(self.__sampling_rate)
        wavefile.writeframes(bytes(frames))
        wavefile.close()
        return wfile

    def close_all(self):
        #stop Qtimer threads
        self.update_timer.stop() 
        self.stop_timer.stop()
        #stop and close audio stream
        self.__stream.stop_stream()
        self.__stream.close()
        self.__audio.terminate()
        #make wav file that is made of stream byte data
        self.make_wav_file(self.byte_data, self.__output_wavfile)
        print("pyaudio was terminated")

#end of class VoicePlotWindow
if __name__=="__main__":
    from PyQt5.QtGui import QApplication
    
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    
    win = VoicePlotWindow()
    win.show()
    #print(win.get_device_info())
    #app.aboutToQuit.connect(app.deleteLater)
    print("start recording")
    sys.exit(app.exec_())
    print("finished recording")