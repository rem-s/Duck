from control.motor.ta7291 import *
from control.process.pid import *
from network.udp import *
from network.tcp import * 
import numpy as np
import cv2
import time

#通信初期化
tcp = TCP("192.168.0.50", 8889)
#udp = UDP("192.168.0.50", "192.168.0.139", 8888, 8889)

#モーター初期化
l_motor = TA7291P(8, 25, 27)
r_motor = TA7291P(17, 7, 22)

# PIDパラメーター
KU, PU = 0.65, 0.6
TI, TD = 0.5*PU, 0.125*PU
ALPHA = 0.001
target = 0 #目的角度 0[theta]
KP, KI, KD = KU, 0.01*KP/TI, KP*TD
params = [0, KP, KI, KD, 0, 0] #DELTA_T, KP, KI, KD, deviation, integral

#画像データ取得
cam = cv2.VideoCapture(0)
flag,img = cam.read()
height, width, channel = img.shape
img = cv2.resize(img, (int(width/8), int(height/8)))
result, encimg = cv2.imencode('.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), 80])
jpegstring=encimg.tostring()

while True:	

	#画像データ送信
	tcp.send(jpegstring) 
	
	#画像データ取得
	start_time = time.time()
	flag,img = cam.read()
	height, width, channel = img.shape
	img = cv2.resize(img, (int(width/8), int(height/8)))
	result, encimg = cv2.imencode('.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), 80])
	jpegstring=encimg.tostring()
	
	#ＰＣから画像処理結果取得
	data = tcp.receive(1024)
	data = int.from_bytes(data, byteorder="big", signed=True)
	
	#PID制御による角度調整
	DELTA_T = time.time() - start_time
	params[0] = DELTA_T
	turn = pid(target, data, params)
	
	#ＰＩＤによるモーター制御
	r = 0.2 + ALPHA*turn 
	l = 0.2 + -1*ALPHA*turn
	print(data, '{:.2f}'.format(turn), '{:.2f}'.format(l), '{:.2f}'.format(r))
	
	#閾値の設定
	if r>1.0: r=1.0
	if r<-1.0: r=-1.0
	if l>1.0: l=1.0
	if l<-1.0: l=-1.0

	#モーターPWM出力
	r_motor.set_motor_pwm(r)
	l_motor.set_motor_pwm(l)

cam.releace()
