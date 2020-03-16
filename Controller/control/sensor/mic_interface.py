import pyaudio #handling recording function
import wave #handling .wav file

class Recorder:
    def __init__(self):
        # recording time (unit: s)
        self.record_time = 3
        # file name
        self.output_wavfile = "record.wav"
        # index number of microphone
        self.idevice = 1
        # format of audio
        self.format = pyaudio.paInt16
        # monaural
        self.nchannels = 1
        # sampling rate,which is usually 16KHz(=16kHz?) In the special case, raspberryPi needs 44.1kHz
        self.sampling_rate = 44100 #8192*2
        # number of extracted data at a time,that is called chunk
        self.chunk = 2**10
        # get device information
        self.audio = pyaudio.PyAudio()
        # instance of stream obj for making wav file
        self.stream = pyaudio.Stream()
    
    def __exit__(self):
        self.close()
        
    def set_config(self, time_sec=3, file="record.wav", device_index=1, sampling_rate=44100, chunk=2**10, format=pyaudio.paInt16, nchannels=1):
        # configure foundimental information

        # recording time (unit: s)
        self.record_time = time_sec
        # file name
        self.output_wavfile = file
        # index number of microphone
        self.idevice = device_index
        # sampling rate,which is usually 16kHz
        self.sampling_rate = sampling_rate
        # number of extracted data at a time,that is called chunk
        self.chunk = chunk
        # format of audio
        self.format = format
        # monaural
        self.nchannels = nchannels
    
    def show_deviceinfo(self):
        for i in range(self.audio.get_device_count()):
            print(self.audio.get_device_info_by_index(i))

    def record(self, wfile_list=["record.wav"]):
        for w in wfile_list:
            #audio.open() method returns new Stream instance taking some arguments for configuration
            self.stream = self.audio.open(
            format = self.format,
            channels = self.nchannels,
            rate = self.sampling_rate,
            input = True,
            input_device_index = self.idevice, # device1(Mouse_mic) will be used for input device
            frames_per_buffer = self.chunk)

            print("start recording...")
            frames = []
            for i in range(0, int(self.sampling_rate / self.chunk * self.record_time)):
                data = self.stream.read(self.chunk) # chunkごとにdataを書き出す write raw data at each chunk
                frames.append(data)
            print("finished recording\noutput_file was generated\n")
            return self.prepare_file(frames, w)
          
    def prepare_file(self, frames, wfile, mode='wb'):
        if wfile != self.output_wavfile:
            self.output_wavfile = wfile
        wavefile = wave.open(wfile, mode)
        wavefile.setnchannels(self.nchannels)
        wavefile.setsampwidth(self.audio.get_sample_size(self.format))
        wavefile.setframerate(self.sampling_rate)
        wavefile.writeframes(b"".join(frames))
        return self.output_wavfile
       
    def close(self):
        self.stream.close()
        self.audio.terminate()
        self.output_wavfile.close()
#end of class Record