import pyaudio #handling recording function
import wave #handling .wav file

#beginning of class Recorder
class Recorder:

#public methods
    def __init__(self):
        # recording time (unit: s)
        self.__record_time = 3
        # file name
        self.__output_wavfile = "record.wav"
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
        self.__stream = pyaudio.Stream()
    
    def __exit__(self):
        self.__close()
        
    def set_config(self, time_sec=3, file="record.wav", device_index=1, sampling_rate=44100, chunk=2**10, format=pyaudio.paInt16, nchannels=1):
        # configure foundimental information

        # recording time (unit: s)
        self.__record_time = time_sec
        # file name
        self.__output_wavfile = file
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
    
    def show_deviceinfo(self):
        for i in range(self.audio.get_device_count()):
            print(self.audio.get_device_info_by_index(i))

    def record_voice(self, wfile_list=["record.wav"]):
        for w in wfile_list:
            #audio.open() method returns new Stream instance taking some arguments for configuration
            self.__stream = self.__audio.open(
            format = self.__format,
            channels = self.__nchannels,
            rate = self.__sampling_rate,
            input = True,
            input_device_index = self.__idevice, # device1(Mouse_mic) will be used for input device
            frames_per_buffer = self.__chunk)

            print("start recording...")
            frames = []
            for i in range(0, int(self.__sampling_rate / self.__chunk * self.__record_time)):
                data = self.__stream.read(self.__chunk) # chunkごとにdataを書き出す write raw data at each chunk
                frames.append(data)
            print("finished recording\noutput_file was generated\n")
            return self.__prepare_file(frames, w)

#private methods          
    def __prepare_file(self, frames, wfile, mode='wb'):
        if wfile != self.__output_wavfile:
            self.__output_wavfile = wfile
        wavefile = wave.open(wfile, mode)
        wavefile.setnchannels(self.__nchannels)
        wavefile.setsampwidth(self.__audio.get_sample_size(self.__format))
        wavefile.setframerate(self.__sampling_rate)
        wavefile.writeframes(b"".join(frames))
        return self.__output_wavfile
       
    def __close(self):
        self.__stream.close()
        self.__audio.terminate()
        self.__output_wavfile.close()

#end of class Record