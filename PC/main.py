from network.udp import *
from PC.control.ai.audio_model import *
from PC.control.process.mfcc import *
from PC.control.sensor.mic import Recorder

#インスタンス生成(レコード, モデル[決定木], UDP)
record = Recorder()
model = Model()
model.model_select("DecisionTree") #model_selectメソッドなくしたい (コンストラクタで指定するほうがわかりやすい)
udp = UDP("192.168.0.56","192.168.0.51", 8889, 8888)

while True:

	#レコードとMFCC
	outfile = record.record_voice(["a.wav"], overwrite=True)
	mfcc = MFCC("./control/audioSample/a.wav")
	features = mfcc.get_mfcc().reshape(1, -1)
	
	#音声認識
	result = model.predict(features)
	
	#認識結果をraspberry piに送信し制御
	udp.send(int(result).to_bytes(1, 'big'))
	zz