#テスト用プログラム
from control.motor.ta7291 import *
from network.tcp import *
import numpy as np
import cv2
import time


tcp = TCP("192.168.0.105", 8889)

#モーター初期化
r_motor = TA7291P(8, 25, 27)
l_motor = TA7291P(17, 7, 22)

while True:

	msg = tcp.receive(1024)	
	msg = int.from_bytes(msg, byteorder="big", signed=True)
	print(msg)
	
	#前進
	if msg == 1:
		r_motor.set_motor_pwm(0.2)
		l_motor.set_motor_pwm(0.2)
		
	#右前
	if msg == 2:
		r_motor.set_motor_pwm(0.1)
		l_motor.set_motor_pwm(0.2)
		
	#左前
	if msg == 3:
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
		r_motor.stop()
		l_motor.stop()

