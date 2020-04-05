from control.motor.ta7291 import *
from network.tcp import *
import numpy as np
import cv2
import time

tcp = TCP("192.168.0.105", 8889)
cam = cv2.VideoCapture(0)

#モーター初期化
r_motor = TA7291P(8, 25, 27)
l_motor = TA7291P(17, 7, 22)

while True:
	flag,img = cam.read()
	img = cv2.resize(img, (120, 90))
	result, encimg = cv2.imencode('.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), 80])
	jpegstring=encimg.tostring()
	tcp.send(jpegstring) 
	
	data = tcp.receive(1024)
	msg = int.from_bytes(data, byteorder="big", signed=True)
	print(msg)
	
	#前進
	if msg == 1:
		print("forward")
		r_motor.set_motor_pwm(0.2)
		l_motor.set_motor_pwm(0.2)
		
	#右前
	if msg == 3:
		r_motor.set_motor_pwm(0.1)
		l_motor.set_motor_pwm(0.2)
		
	#左前
	if msg == 2:
		r_motor.set_motor_pwm(0.2)
		l_motor.set_motor_pwm(0.1)
		
	#後進
	if msg == 4:
		r_motor.set_motor_pwm(-0.2)
		l_motor.set_motor_pwm(-0.2)
		
	#右後
	if msg == 5:
		r_motor.set_motor_pwm(-0.1)
		l_motor.set_motor_pwm(-0.2)
		
	#左後
	if msg == 6:
		r_motor.set_motor_pwm(-0.2)
		l_motor.set_motor_pwm(-0.1)
		
	#ストップ	
	if msg == 0:
		print("stop")
		r_motor.stop()
		l_motor.stop()

cam.releace()
