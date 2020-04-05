# coding: utf-8
import RPi.GPIO as GPIO
import time

BUTTON_PIN = 14

def main():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_PIN,GPIO.IN) 
    #GPIO.add_event_detect(BUTTON_PIN, GPIO.BOTH, callback=callback)

    try:
        while(True):
            time.sleep(1)
            print(GPIO.input(BUTTON_PIN))

    # Keyboard入力があれば終わり
    except KeyboardInterrupt:
        print("break")
        GPIO.cleanup()

def callback(channel):
  print("button pushed")

if __name__ == "__main__":
    main()