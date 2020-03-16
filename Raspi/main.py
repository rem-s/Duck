import RPi.GPIO as GPIO
from network.udp import *
from control.motor.ta7291 import *

r_motor = TA7291P(25, 7, 27)
l_motor = TA7291P(8, 17, 22)
udp = UDP("192.168.0.51","192.168.0.56", 8888, 8889)

while True:
	msg = udp.receive()
	print(int(msg))
	if int(msg) == 0:
		r_motor.stop()
		l_motor.stop()
	elif int(msg) == -1:
		#print(10101)
		r_motor.set_motor_pwm(-0.5)
		l_motor.set_motor_pwm(-0.5)
	else:
		r_motor.set_motor_pwm(0.5)
		l_motor.set_motor_pwm(0.5)

	
