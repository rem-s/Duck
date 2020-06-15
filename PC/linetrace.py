from network.udp import *
from network.tcp import * 
from control.process.image import *
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import cv2
import time
import os

#初期化
fps, img_n = 0, 0
img_dir = "./img"
if not os.path.exists(img_dir): os.mkdir(img_dir)

#情報初期化
height, width, channel = int(480/8), int(640/8), 3
tcp = TCP("192.168.0.60", 8890, server_flag=True)

#インスタンス生成(レコード, モデル[決定木], UDP)
#record = Recorder()
#model = Model()
#model.model_select("K-NN")

#音声認識[前と言ったら動きだす]
#print("start recoding")
#while result:

	#レコードとMFCC
	#outfile = record.record_voice(["a.wav"], overwrite=True)
	#mfcc = MFCC("./control/audioSample/a.wav")
	#features = mfcc.get_mfcc().reshape(1, -1)
	
	#音声認識
	#result = model.predict(features)
	#print(result)

while True:
	
	#TCP画像受信
	start = time.time()
	receivedstr=tcp.receive(1024*4) 
	narray = np.fromstring(receivedstr,dtype='uint8')  
	raw_img = cv2.imdecode(narray,1).reshape((height, width, channel))
	
	#ライン検出
	grayFrame = cv2.cvtColor(raw_img, cv2.COLOR_BGR2GRAY)
	b_img = mean_binarize(grayFrame)
	l_img = labeling(b_img)
	r_img = compare_area(l_img)
	
	#画像から回転角度算出
	#degree, top_feature_point, bottom_feature_point, tip, rear = image_line_degree(r_img)
	degree, grav = grav_degree(r_img)
	tcp.send(int(degree).to_bytes(4, 'big', signed=True))
	
	#画像保存
	img_n += 1
	pil_img = Image.fromarray(cv2.cvtColor(cv2.resize(raw_img, (32, 32)), cv2.COLOR_BGR2RGB))
	pil_img.save('%s/img%d_%d.jpg'%(img_dir, img_n, degree))
	
	#FPS算出
	fps += 1/(time.time()-start)
	print(fps/img_n)

cv2.destroyAllWindows()
