import librosa
from PC.control.sensor.mic import *
from sklearn.externals import joblib

# record your speech
record = Recorder()
file_dst = "./test_speech/"
out_file = record.record_voice(wfile_list=["utterance{}.wav".format(w) for w in range(3)], dst=file_dst, overwrite=True)

# load GMMs-based speaker recognition model
models_ = joblib.load("./control/ai/models/speaker_reco_gmms.model")

# number of speakers are 4
# please do not modify speakers order(dictionary key's order)
speakers = {
    0: "banri", 1: "gb", 2: "reon", 3: "tari"
}
# speech size is following
speakers_size = {
    "banri": 30, "gb": 30, "reon": 30, "tari": 30
}

for w in out_file:
    y, sr = librosa.load(file_dst+w, sr=44100, duration=3.0)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=12)

    max_score = -99999
    max_speaker = None
    for i in range(len(models_)):
        score = models_[i].score(mfcc.T)
        print(score)
        if score > max_score:
            max_score, max_speaker = score, speakers[i]
    
    predicted_sp = max_speaker
    print("speech: {0}, predicted: {1}".format(w, predicted_sp))