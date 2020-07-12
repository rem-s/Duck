import numpy as np
import pandas as pd
import librosa
from sklearn.externals import joblib
from sklearn.mixture import GaussianMixture

speakers = {
    0: "banri", 1: "gb", 2: "reon", 3: "tari"
}
speakers_size = {
    "banri": 30, "gb": 30, "reon": 30, "tari": 30
}

feature_df = pd.read_csv("../dataset/speaker_reco_dataset.csv")
speaker_df = feature_df["speaker"]
train_df = feature_df.drop("Unnamed: 0", axis=1).drop("speaker", axis=1)

n_classes = 64
gmm1 = GaussianMixture(n_components=n_classes, covariance_type='diag', max_iter=100, random_state=0)
gmm2 = GaussianMixture(n_components=n_classes, covariance_type='diag', max_iter=100, random_state=0)
gmm3 = GaussianMixture(n_components=n_classes, covariance_type='diag', max_iter=100, random_state=0)
gmm4 = GaussianMixture(n_components=n_classes, covariance_type='diag', max_iter=100, random_state=0)
gmms_ = [gmm1, gmm2, gmm3, gmm4]

n_sample = train_df.shape[0]
n_estimators = len(gmms_)
offset = 0
models_ = []

for sp, gmm in enumerate(gmms_):
    # Since we have class labels for the training data, we can
    # initialize the GMM parameters in a supervised manner.
    gmm.means_init = np.array([train_df[offset:(offset+n_sample//4)].mean(axis=0) for i in range(n_classes)])
    #print("(1, 12)?? = ", gmm.means_init.shape)
    
    # Train the other parameters using the EM algorithm
    models_.append(gmm.fit(train_df[offset:(offset+n_sample//4)]))
    offset = offset+(n_sample//4)

total_size = 40
test_size = 10
count = 0

for i, (sp, sz) in enumerate(speakers_size.items()):
    for t in range(test_size):
        wf = "../dataset/speech_samples/text_independent/{}/reco{}.wav".format(sp, t+sz)
        y, sr = librosa.load(wf, sr=44100, duration=3.0)
        mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=12)
        
        max_score = -99999
        max_speaker = None
        for m in range(n_estimators):
            for vi in range(mfcc.shape[1]):
                score = models_[m].score(mfcc.T[vi].reshape(1, -1))
                if score > max_score:
                    max_score, max_speaker = score, speakers[m]
        
        predicted_sp = max_speaker
        actual_sp = sp
        print("predicted: ", predicted_sp, "actual: ", actual_sp)
        if predicted_sp == actual_sp:
            count = count + 1

print("accuracy: ", count/total_size)

joblib.dump(models_, "../models/speaker_reco_gmms.model")