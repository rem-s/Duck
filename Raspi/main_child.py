#モジュールインポート
import cv2
import numpy as np
from sensor.tuning import Tuning
from sensor.pid import *
import usb.core
import usb.util

#自作モジュールインポート
from network.tcp import *
from sensor.ta7291 import *
from sensor.adxl345 import *
from sensor.sonar import *

#socket定義
host_ip = "192.168.111.101"
tcp_image = TCP(host_ip, 8894)
tcp_sonic = TCP(host_ip, 8895)
tcp_acc = TCP(host_ip, 8896)
tcp_sound = TCP(host_ip, 8897)

#カメラ設定
height, width = 128, 416
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 416)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 312)

#センサー定義
dsize = 3
adxl345 = ADXL345()
l_motor = TA7291P(6, 22, 27)
r_motor = TA7291P(24, 23, 17)
sonic = sonar(trigger_pin=19, echo_pin=20)
dev = usb.core.find(idVendor=0x2886, idProduct=0x0018)
if not dev : print("not found")
Mic_tuning = Tuning(dev)
Mic_tuning.set_vad_threshold(0)

#PID設定
KU, PU = 0.65, 0.6
TI, TD = 0.5*PU, 0.125*PU
ALPHA = 0.0005
target = 0 #目的角度 0[theta]
KP, KI, KD = KU, 0.01*KU/TI, KU*TD
params = [0, KP, KI, KD, 0, 0] #DELTA_T, KP, KI, KD, deviation, integral

while True:
	try:
		#画像送信
		flag,img = cam.read()
		img = img[156-64:156+64]
		img = cv2.resize(img, (int(width/2), int(height/2)))
		print(img.shape)
		tcp_image.send(img)

		#加速度送信
		axes = adxl345.getAxes(True)
		for i in range(3): tcp_acc.send(int(axes[i]*100).to_bytes(dsize, byteorder="big", signed=True))

		#距離送信
		distance = int(sonic.get_distance())
		tcp_sonic.send(distance.to_bytes(dsize, byteorder="big"))

		#音送信
		if Mic_tuning.is_voice():
			dir = int(Mic_tuning.direction)
			tcp_sound.send(dir.to_bytes(dsize, byteorder="big"))
		else:
			tcp_sound.send(b"370")

		#推論結果取得
		degree = b""
		while len(degree) < dsize:degree += tcp_image.receive(dsize)
		degree = int.from_bytes(degree, 'big', signed=True)

		#motor control
		DELTA_T = 0.2
		params[0] = DELTA_T
		turn = pid(target, degree, params)
		r = 0.2 + ALPHA*turn
		l = 0.2 + -1*ALPHA*turn

		r_motor.set_motor_pwm(r)
		l_motor.set_motor_pwm(l)

		print(degree, r, l)
	except KeyboardInterrupt:
		cam.release()
		print("released")
		break
print("end")
