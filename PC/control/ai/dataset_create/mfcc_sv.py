# -*- coding: UTF-8 -*-
#これはdatasetを生成するためのプログラムなので単体動作を想定している
# speaker verificationのためのmfcc dataset生成プログラム
if __name__ == "__main__":
    import librosa
    import glob
    import pandas as pd

    #speakers = {}
    speech_count = 0
    total_speech = len(glob.glob('../dataset/speech_samples/text_dependent/robot_manip/reon/*'))
    print(total_speech)
    
    train_data = pd.DataFrame()

    for speech in sorted(glob.glob('../dataset/speech_samples/text_dependent/robot_manip/reon/*')):
        print(speech_count/float(total_speech)*100.0, 'percent completed')
        #speaker_name = speech.replace('../dataset/speech_samples/text_dependent/robot_manip/reon/', '')
        #speakers.update({speaker_name:speech_count})
        y, sr = librosa.load(speech, sr=44100, duration=3.0)
        mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=12)
        
        mfcc_df = pd.DataFrame(mfcc.T)

        mfcc_df["speaker"] = "reon"
        if speech_count < 40:
            mfcc_df["label"] = "forward"
        else:
            mfcc_df["label"] = "backward"
        
        train_data = train_data.append(mfcc_df)

        speech_count = speech_count + 1

    train_data.reset_index(drop=True).to_csv("../dataset/sv_mfccs.csv")