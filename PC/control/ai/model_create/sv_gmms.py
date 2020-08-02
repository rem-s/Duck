import librosa
import glob
import numpy as np
import pandas as pd
from sklearn.externals import joblib
from sklearn.mixture import GaussianMixture

feature_df = pd.read_csv("../dataset/sv_mfccs.csv")
speaker_df = feature_df["speaker"]
label_df = feature_df["label"]
train_df = feature_df.drop("speaker", axis=1).drop("label", axis=1).drop("Unnamed: 0", axis=1)
#print(train_df.columns)

n_clusters = 64
gmms_ = GaussianMixture(n_components=n_clusters, covariance_type='diag', max_iter=100, random_state=None)

n_sample = train_df.shape[0]
n_estimators = 1

# Since we have class labels for the training data, we can
# initialize the GMM parameters in a supervised manner.
#gmms_.means_init = np.array([train_df[:].mean(axis=0)])

# Train the other parameters using the EM algorithm
gmms_.fit(train_df)

speech_count = 0
total_speech = len(glob.glob('../dataset/speech_samples/text_dependent/robot_manip/reon/*'))

max_score, min_score = None, None

for speech in sorted(glob.glob('../dataset/speech_samples/text_dependent/robot_manip/reon/*')):
    
    print(float(speech_count/total_speech),'percent completed')
    
    y, sr = librosa.load(speech, sr=44100, duration=3.0)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=12)
    
    for i, mfcc_frame in enumerate(mfcc.T):
        score = gmms_.score(mfcc_frame.reshape(1, -1))
        if max_score is None or score > max_score:
            max_score = score
        if min_score is None or score < min_score:
            min_score = score
    
    speech_count = speech_count + 1

print("min_score:", min_score, "max_score:", max_score)
score = (min_score, max_score)
joblib.dump(score, "../models/sv_gmms_score.model")
joblib.dump(gmms_, "../models/sv_gmms_model.model")