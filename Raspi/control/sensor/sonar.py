import RPi.GPIO as GPIO
import time

from control.sensor import temp

class sonar:
    def __init__(self, trigger_pin=17, echo_pin=27, start_time=0, end_time=0, tempVal=20):
        """
        Parameters
        ----------
        trigger_pin : pin number for trigger pin
        echo_pin    : pin number for echo pin
        start_time  : Store the latest time when get_distance function is started
        end_time    : Store the latest time when get_distance function is ended
        tempVal     : Temperature for calcuration distance
        """
        self.trigger_pin = trigger_pin
        self.echo_pin = echo_pin
        self.start_time = start_time
        self.end_time = end_time
        self.tempVal = tempVal

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trigger_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)

    def get_distance(self):
        """
        Return
        ----------
        dis : distance (cm) float
        """
        # check iteration time > 60[msec]
        iter_time = self.end_time - self.start_time
        if iter_time < 0.060: time.sleep(0.06 - iter_time)

        # 10usec output high [trigger pin]
        self.start_time = time.time()
        GPIO.output(self.trigger_pin, GPIO.HIGH)
        time.sleep(0.000010)
        GPIO.output(self.trigger_pin, GPIO.LOW)

        # waiting for high signal 
        while GPIO.input(self.echo_pin) == 0: t_start = time.time()

        # waiting for finish signal
        while GPIO.input(self.echo_pin) == 1: t_end = time.time()

        # duration
        duration = (t_end - t_start) / 2

        # get temperature for calclation distance
        tempInstance = temp.DHT11(temp_pin=14)
        tempResult = tempInstance.read()
        if tempResult.is_valid():
            self.tempVal = tempResult.temperature

        print("temperature:", self.tempVal)

        # calculation distance
        sound_speed = 331.50 + 0.61 * self.tempVal
        dis = duration*sound_speed*100;
        self.end_time = time.time()
        return dis

if __name__ == "__main__":
    tmp = sonar(trigger_pin=18, echo_pin=23)

    while True:
        distance_cm = tmp.get_distance()
        print("distance:", distance_cm, "cm")
        #tcp.send(int(distance_cm).to_bytes(10, "big"))
        time.sleep(1)
