import wave
import numpy as np
import scipy.signal
from scipy.fftpack import realtransforms

#beginning of class MFCC
class MFCC:
    
#public method
    def __init__(self, wavfile="record.wav"):
        self.__waveform = wave.open(str(wavfile), mode="rb")
        self.__freq = self.__waveform.getframerate()
    
    def get_sampliing_freq(self):
        return self.__freq
    
    def get_mfcc(self, p=0.97, nchannels=24, nceps=12):
        #extract raw data from wavfile
        __signal = []
        __signal = self.__waveform.readframes(-1) #read all data
        __signal = np.frombuffer(__signal, dtype="int16") / float(2**15) #normalize

        #multiply preEmphasis filter
        __signal = self.__preEmphasis(__signal, p)
        #hamming window
        dataSz = len(__signal)
        hammingWindow = np.hamming(dataSz)
        __signal = __signal * hammingWindow

        #get spectrum
        self.__nfft = 2**int(np.log2(dataSz)+1)
        spec = np.abs(np.fft.fft(__signal, self.__nfft)/(self.__nfft/2))[:self.__nfft//2]

        #melfilterbank
        #numChannels = 24
        df = self.__freq / self.__nfft
        filterbank, fcenters = self.__melFilterBank(self.__freq, self.__nfft, nchannels)

        #apply melfilterbank to each spectrum, then take sum all
        mspec = []
        for c in np.arange(0, nchannels):
            mspec.append(np.log10(sum(spec * filterbank[c])))
        mspec = np.array(mspec)
        
        #get mfcc by discrete cosine form
        mfcc = self.__dct(mspec, nceps)
        #print(type(mfcc))
        return mfcc

#private methods
    #pre-emphasis filter
    def __preEmphasis(self, signal, p):
        #signal := voice_signal, p := coefficient
        #make FIR filter such that coefficients are (1.0, p)
        return scipy.signal.lfilter([1.0, -p], 1, signal)
    
    #convert hz to mel
    def __hz2mel(self, f):
        return 1127.01048 * np.log(f/700.0 + 1.0)
    
    #convert mel to hz
    def __mel2hz(self, m):
        return 700*(np.exp(m/1127.01048) - 1.0)

    #generate melfilterbank
    def __melFilterBank(self, fs, nfft, nchannels):
        #ナイキスト周波数
        fmax = fs / 2
        melmax = self.__hz2mel(fmax)
        nmax = nfft // 2
        df = fs / nfft
        dmel = melmax / (nchannels + 1)
        melcenters = np.arange(1, nchannels + 1) * dmel
        fcenter = self.__mel2hz(melcenters)
        indexcenter = np.round(fcenter / df)
        indexstart = np.hstack((0, indexcenter[0:nchannels - 1]))
        # 各フィルタの終了位置のインデックス
        indexstop = np.hstack((indexcenter[1:nchannels], [nmax]))
        
        filterbank = np.zeros((nchannels, nmax))
        for c in np.arange(0, nchannels):
            # 三角フィルタの左の直線の傾きから点を求める
            increment= 1.0 / (indexcenter[c] - indexstart[c])
            for i in np.arange(indexstart[c], indexcenter[c]):
                filterbank[c, int(i)] = (i - indexstart[c]) * increment
            # 三角フィルタの右の直線の傾きから点を求める
            decrement = 1.0 / (indexstop[c] - indexcenter[c])
            for i in np.arange(indexcenter[c], indexstop[c]):
                filterbank[c, int(i)] = 1.0 - ((i - indexcenter[c]) * decrement)
        return filterbank, fcenter
    
    #discrete cosine transform
    def __dct(self, mspec, nceps):
        ceps = realtransforms.dct(mspec, type=2, norm="ortho", axis=-1)
        #return lower features by n
        return ceps[:nceps]

#end of class MFCC