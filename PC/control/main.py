from process.mfcc import MFCC
from sensor.mic import Recorder
from model.model import *
from sklearn.externals import joblib

record = Recorder()
model = AudioModel("./audioDataSet.csv")

outfile = record.record_voice()
mfcc = MFCC(outfile)
features = mfcc.get_mfcc().reshape(1, -1)
#features = features.reshape(1, -1)
model.train_model("K-NN")
result = model.predict(features)
print(result)

mname = "audio_model"
joblib.dump(model, mname)