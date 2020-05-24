import pyaudio #handling recording function
import wave #handling .wav file
from os import listdir, makedirs

#プロット関係のライブラリ
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import numpy as np
import sys
import time

class VoicePlotWindow(object):
    
    def __init__(self, wfile="record.wav", dst="./", overwrite=False):
        
        if dst[-1] != "/":
            print("Destination must be ended with \"/\"")
            raise NotADirectoryError
        
        makedirs(dst, exist_ok=True) # check if dst already exists. If doesn't, make new dir
        
        if overwrite == False and set.intersection(set(wfile), listdir(dst)) != set():
            print("Same wavfile exists in {0}\nYou were about to overwrite {1}\nIf you wouldn't mind it, set overwrite flag True".format(dst, dst+w))
            raise FileExistsError

        # recording time (unit: s)
        self.__record_time = 10
        # file name
        self.__output_wavfile = wfile
        # index number of microphone
        self.__idevice = 1
        # format of audio
        self.__format = pyaudio.paInt16
        # monaural
        self.__nchannels = 1
        # sampling rate,which is usually 16KHz(=16kHz?) In the special case, raspberryPi needs 44.1kHz
        self.__sampling_rate = 44100 #8192*2
        # number of extracted data at a time,that is called chunk
        self.__chunk = 2**10
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
        self.record = False
        self.playback_on = False
        self.plot_on = True
        self.stop_callback = False
        
        self.byte_data = bytearray()
        self.win=pg.GraphicsWindow()
        self.win.setWindowTitle("Real-time plot")
        self.plt=self.win.addPlot()
        self.plt.setXRange(0, self.__chunk*5)
        self.plt.setYRange(-1,1)
        self.curve=self.plt.plot()
        
        #音声データの格納場所(プロットデータ)
        self.plot_data = np.zeros(self.__chunk*2)
        #self.write_time = int(self.__sampling_rate * self.__record_time / self.__chunk)
        self.prev = 0
        self.next = self.__chunk*2
        
        self.__stream.start_stream()
        
        self.update_timer = QtCore.QTimer()
        self.update_timer.timeout.connect(self.update)
        self.update_timer.start(100) # call plot update func every 100ms
        
        self.stop_timer = QtCore.QTimer()
        self.stop_timer.timeout.connect(self.close_all)
        self.stop_timer.start(1000*self.__record_time) # plot stops when record time passes

    def callback(self, in_data, frame_count, time_info, status):
        #print(len(in_data), frame_count) #=> class "bytes", class "int"
        if self.plot_on == True:
            self.byte_data.extend(in_data)
        return (None, pyaudio.paComplete)
    
    def update(self):
        self.__stream.stop_stream()
        ## critical section start
        next_plot = np.frombuffer(bytes(self.byte_data[self.prev:self.next]), dtype="int16") / 2**15
        #self.plot_data = next_chunk
        self.plot_data = np.append(self.plot_data, next_plot)
        ## critical section end
        self.__stream.start_stream()
        self.prev = self.next
        self.next = self.prev + self.__chunk*2
        
        if len(self.plot_data)/1024 > 5:
            self.plot_data = self.plot_data[1024:]
        self.curve.setData(self.plot_data) # plot the data
        #print(len(self.plot_data)/1024)
        
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
        self.__stream.stop_stream()
        self.stop_timer.stop()
        self.update_timer.stop()
        self.make_wav_file(self.byte_data, self.__output_wavfile)
        self.__stream.close()
        self.__audio.terminate()
        print("pyaudio was terminated")

#end of class VoicePlotWindow
if __name__=="__main__":
    from PyQt5.QtGui import QApplication
    
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    
    win = VoicePlotWindow()
    #print(win.get_device_info())
    #app.aboutToQuit.connect(app.deleteLater)
    print("start recording")
    sys.exit(app.exec_())
    print("finished recording")