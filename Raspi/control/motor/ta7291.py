#About TA7291 class
import RPi.GPIO as GPIO

class TA7291P:
	def __init__(self, 
				 in1, 
				 in2, 
				 pwm):
				 
		#setting ports
		self.in1 = in1
		self.in2 = in2
		self.pwm = pwm
		self.init_gpio()
		
		#setting state
		self.state = 2
		self.pwm.start(0)
		
	def init_gpio(self):
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.in1, GPIO.OUT)
		GPIO.setup(self.in2, GPIO.OUT)
		GPIO.setup(self.pwm, GPIO.OUT)
		self.pwm = GPIO.PWM(self.pwm, 100)

	def stop(self):
	
		#setting stop motor
		GPIO.output(self.in1, 0)
		GPIO.output(sefl.in2, 0)
		pwm.ChangeDutyCycle(0)
	
		#setting stop mode state
		self.state = 2
		
	def set_motor_pwm(self, 
					  param):
		
		#setting car direction
		now_state = param > 0
		if self.state != now_state:
			if now_state: self.set_straight()
			else: self.set_back()
			self.state = now_state
		
		#setting car speed
		pwm_power = abs(param) * 100
		pwm.ChangeDutyCycle(pwm_power)
		
	def set_straight(self):
	
		#setting straight
		GPIO.output(self.in1, 1)
		GPIO.output(self.in2, 0)
	
	def set_back(self):
	
		#setting back
		GPIO.output(self.in1, 0)
		GPIO.output(self.in2, 1)
		
	#print debug
	def print_debug(self):
		return b"Hello motor"
		