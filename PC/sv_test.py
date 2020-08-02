import librosa
import glob
from sklearn.externals import joblib
from control.sensor.mic import Recorder

# speaker verification test

if __name__ == "__main__":
    
    gmms_ = joblib.load('./control/ai/models/sv_gmms_model.model')
    threshold_min, threshold_max = joblib.load('./control/ai/models/sv_gmms_score.model')
    print('threshold: ', threshold_min, '~', threshold_max, '\n')

    count = 0
    total = len(glob.glob('./control/ai/dataset/speech_test/text_dependent/robot_manip/reon/*'))

    max_score, min_score = None, None
    
    for speech in glob.glob('./control/ai/dataset/speech_test/text_dependent/robot_manip/reon/*'):
        print(speech, speech.split("/")[-1])
        
        y, sr = librosa.load(speech, sr=44100, duration=3.0)
        mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=12)

        for i, mfcc_frame in enumerate(mfcc.T):
            score = gmms_.score(mfcc_frame.reshape(1, -1))
            if max_score is None or score > max_score:
                max_score = score
            if min_score is None or score < min_score:
                min_score = score
        
        print("min_score:", min_score, "max_score:", max_score)
        # check if thresholds are between min_score and max_score
        if threshold_min <= min_score and max_score <= threshold_max:
            count = count + 1
    # print accuracy
    print(float(count/total))