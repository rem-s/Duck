# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np
import librosa
from sklearn.cluster import KMeans
from sklearn.externals import joblib

speakers = {
    0: "banri", 1: "gb", 2: "reon", 3: "tari"
}
speakers_size = {
    "banri": 30, "gb": 30, "reon": 30, "tari": 30
}

feature_df = pd.read_csv("../dataset/speaker_reco_dataset.csv")
speaker_df = feature_df["speaker"]
train_df = feature_df.drop("Unnamed: 0", axis=1).drop("speaker", axis=1)
#train_df.head()

n_samples = train_df.shape[0]
n_speakers = len(speakers)
n_clusters = 64

kmeans1 = KMeans(n_clusters=n_clusters, random_state=None)
kmeans2 = KMeans(n_clusters=n_clusters, random_state=None)
kmeans3 = KMeans(n_clusters=n_clusters, random_state=None)
kmeans4 = KMeans(n_clusters=n_clusters, random_state=None)

kmeans_ = [kmeans1, kmeans2, kmeans3, kmeans4]

offset = 0
codebook = []
for sp in range(len(kmeans_)):
    codebook.append(kmeans_[sp].fit(train_df[offset:(offset+n_samples//4)]))
    offset = offset+(n_samples//4)

total_size = 40
test_size = 10
count = 0

for sp, sz in speakers_size.items():
    for t in range(test_size):
        wf = "../dataset/speech_samples/text_independent/{}/reco{}.wav".format(sp, t+sz)
        print(wf)
        y, sr = librosa.load(wf, sr=44100, duration=3.0)
        mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=12)
        
        d = np.zeros((4, 12))
        for cc, cb in enumerate(codebook):
            for vi in range(mfcc.shape[1]):
                for ci in range(cb.cluster_centers_.shape[0]):
                    d[cc] += np.abs(mfcc.T[vi] - cb.cluster_centers_[ci])**2
        
        d_sum = np.zeros((4, 1))
        d_sum = np.sum(d, axis=1) # sum values of 12-dimentional vector for each row
        
        predicted_sp = speakers[np.argmin(d_sum)]
        actual_sp = sp
        print("predicted: ", predicted_sp, "actual: ", actual_sp)
        if predicted_sp == actual_sp:
            count = count + 1

print("accuracy: ", count/total_size)

joblib.dump(codebook, "../models/speaker_reco_kmeans.model")