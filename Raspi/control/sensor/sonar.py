import RPi.GPIO as GPIO
import time
# import csv
# import numpy as np

# trigger_pin = 17
# echo_pin = 23

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(trigger_pin, GPIO.OUT)
# GPIO.setup(echo_pin, GPIO.IN)

class sonar:
    def __init__(self, trigger_pin=17, echo_pin=23):
        self.trigger_pin = trigger_pin
        self.echo_pin = echo_pin

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(trigger_pin, GPIO.OUT)
        GPIO.setup(echo_pin, GPIO.IN)

    def pulse_in(self, pin, timeout=1.0):
        """
        param pin: ピン番号、またはGPIO 番号(GPIO.setmodeに依存。)
        param timeout: タイムアウト(default:1sec)
        return: パルスの長さ（秒）タイムアウト時は0
        """
        start_time = time.time()
        # 前のパルスが終了するのを待つ
        while GPIO.input(pin) == GPIO.HIGH:
            if time.time() - start_time > timeout:
                return 0

         # パルスが始まるのを待つ
        while GPIO.input(pin) == GPIO.LOW:
            if time.time() - start_time > timeout:
                return 0

        # パルス開始時刻を記録
        start = time.time()

        # パルスが終了するのを待つ
        while GPIO.input(pin) == GPIO.HIGH:
            if time.time() - start_time > timeout:
                return 0

        # パルス終了時刻を記録
        end = time.time()

    return end - start

    def get_distance(self, temp=15):
        """
        temp:温度(default:15度)
        return:距離(cm)タイムアウト時は0
        """
        # 出力を初期化
        GPIO.output(trigger_pin, GPIO.LOW)
        time.sleep(0.3)
        # 出力（10us以上待つ）
        GPIO.output(trigger_pin, GPIO.HIGH)
        time.sleep(0.000011)
        # 出力停止
        GPIO.output(trigger_pin, GPIO.LOW)

        # echoからパルスを取得
        dur = pulse_in(self.echo_pin, 1.0)

        # (パルス時間 X 331.50 + 0.61 * 温度) X (単位をcmに変換) X 往復
        return dur * (331.50 + 0.61 * temp) * 50

if __name__ == "__main__":
    tmp = sonar()

    #f = open('distance.csv', 'w')

    #while True:
    for _ in range(20):
        #print("cm=%f\tinches=%f" % tmp.get_distance())
        distance_cm = tmp.get_distance()
        print("cm=", distance_cm)
        # writer = csv.writer(f, lineterminator='\n')
        # writer.writerow([distance_cm])
        time.sleep(1)

    #f.close()



"""
def send_trigger_pulse(self):
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
"""
