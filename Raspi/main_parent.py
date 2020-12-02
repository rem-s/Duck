from sensor.ta7291 import *
from network.tcp import *
import numpy as np

tcp = TCP("192.168.111.101", 8890)

#センサ初期化
l_motor = TA7291P(8, 25, 27)
r_motor = TA7291P(7, 17, 22)

while True:

	#ＰＣから画像処理結果取得
	data = tcp.receive(1)

	r = 0.22 + 0.05
	l = 0.22 + 0.05
	if data == b'0':
		r_motor.stop()
		l_motor.stop()
		tcp.send(b"1")
		continue
	if data == b"1":
		r = 0.22 + 0.05
		l = 0.22 + 0.05
	if data == b'3':
		r = 0.22 + 0.1
		l = 0.22 - 0.1
	if data == b'2':
		r = 0.22 - 0.1
		l = 0.22 + 0.1
	if data == b"4":
		r = -0.22
		l = -0.22
	if data == b"6":
		r = -0.22 - 0.1
		l = -0.22 + 0.1
	if data == b'5':
		r = -0.22 + 0.1
		l = -0.22 - 0.1
	tcp.send(b"1")
	#モーターPWM出力
	r_motor.set_motor_pwm(r)
	l_motor.set_motor_pwm(l)
r_motor.stop()
l_motor.stop()
