import RPi.GPIO as GPIO
import time

trigger_pin = 17
echo_pin = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(trigger_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)

start_time ,end_time = 0, 0
GPIO.output(trigger_pin, GPIO.LOW)
while True:
	
	#iteration time > 60[msec]
	iter_time = end_time - start_time
	if iter_time < 0.060: time.sleep(0.06 - iter_time)

	#10usec output high [trigger pin]
	start_time = time.time()
	GPIO.output(trigger_pin, GPIO.HIGH)
	time.sleep(0.000010)
	GPIO.output(trigger_pin, GPIO.LOW)

	#waiting for high signal 
	while GPIO.input(echo_pin) == 0: t_start = time.time()
	
	#waiting for finish signal
	while GPIO.input(echo_pin) == 1: t_end = time.time()
	
	#duration
	duration = (t_end - t_start) / 2
	
	#calculation distance
	# sound_speed = 331.50 + 0.61 * temp
	sound_speed = 331.50 + 0.61 * 15
	# dis = duration*340*100;
	dis = duration*sound_speed*100;
	print(dis)
	
	end_time = time.time()
	


