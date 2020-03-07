import RPi.GPIO as GPIO
from network.udp import *
from control.motor.ta7291 import *

r_motor = TA7291P(25, 7, 27)
l_motor = TA7291P(8, 17, 22)
udp = UDP("","", 50000, 50001)

while True:
	msg = udp.receive()
	if int(msg) == 0:
		r_motor.stop()
		l_motor.stop()
	else:
		r_motor.set_motor_pwm(0.5)
		l_motor.set_motor_pwm(0.5)

	