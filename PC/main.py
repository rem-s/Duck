from PC.control.ai.audio_model import *
from PC.control.process.mfcc import *
from PC.control.sensor.mic import Recorder
#from sklearn.externals import joblib

#make an instance of Recoder
record = Recorder()
#make list of wav file and record them, with options such as dst, overwrite 
outfile = record.record_voice(["a.wav"], overwrite=True)

#debug print for list of output files
#print(outfile, record.get_audio_file_list())
#get device info as dict. you have to look up this beforehand and make sure you choose correct device
#print(record.show_deviceinfo())

#make an instance of MFCC taking argument of wav file
mfcc = MFCC("./control/audioSample/a.wav")
#get feature vector which has 12 dimensions as list
features = mfcc.get_mfcc().reshape(1, -1)

#make an instance of Model
model = Model()

#you can choose some algorithms you will use
model.model_select("K_NN")
#predict result with model we provide
result = model.predict(features)
print(result)