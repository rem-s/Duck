import RPi.GPIO as GPIO
import time
import csv
import numpy as np

trigger_pin = 17
echo_pin = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(trigger_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)

class sonar:
    def __init__(self):
        pass

    def send_trigger_pulse():
        GPIO.output(trigger_pin, True)
        time.sleep(0.0001)
        GPIO.output(trigger_pin, False)

    def wait_for_echo(value, timeout):
        count = timeout
        while GPIO.input(echo_pin) != value and count > 0:
            count = count - 1

    def get_distance():
        send_trigger_pulse()
        wait_for_echo(True, 10000)
        start = time.time()
        wait_for_echo(False, 10000)
        finish = time.time()
        pulse_len = finish - start
        distance_cm = pulse_len / 0.0000580
        distance_in = distance_cm / 2.5
        #return (distance_cm, distance_in)
        return distance_cm

if __name__ == "__main__":
    tmp = sonar()

    #f = open('distance.csv', 'w')

    #while True:
    for _ in range(20):
        #print("cm=%f\tinches=%f" % tmp.get_distance())
        distance_cm = tmp.get_distance()
        print("cm=", distance_cm)
        #writer = csv.writer(f, lineterminator='\n')
        #writer.writerow([distance_cm])
        time.sleep(1)

    #f.close()
