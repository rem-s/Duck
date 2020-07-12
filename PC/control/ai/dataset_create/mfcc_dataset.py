# -*- coding: UTF-8 -*-
#これはdatasetを生成するためのプログラムなので単体動作を想定している
if __name__ == "__main__":
    
    import librosa
    import pandas as pd
    from functools import reduce
    
    speakerData = {
        "banri": 30, "gb": 30, "reon": 30, "tari": 30
    }

    dataSetSz = reduce(lambda s,v: s+v, speakerData.values())
    print(dataSetSz)

    train_data = pd.DataFrame()
    
    for sp, sz in speakerData.items():
        
        for t in range(sz):
            
            wf = "../dataset/speech_samples/text_independent/{}/reco{}.wav".format(sp, t)
            y, sr = librosa.load(wf, sr=44100, duration=3.0)
            mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=12)
            
            mfcc_df = pd.DataFrame(mfcc.T)
            
            mfcc_df["speaker"] = sp
            
            train_data = train_data.append(mfcc_df)

    train_data.reset_index(drop=True).to_csv("../dataset/speaker_reco_dataset.csv")