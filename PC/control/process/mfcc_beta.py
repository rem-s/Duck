import librosa
y, sr = librosa.load("record.wav", sr=44100, duration=3.0)
print(y.shape, sr)
y = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=12)
print(y.shape)