import time
import board
import busio
import adafruit_adxl34x

import csv

class acc:
    def __init__(self):
        i2c = busio.I2C(board.SCL, board.SDA)
        accelerometer = adafruit_adxl34x.ADXL345(i2c)

    def get_acceleration(self):
        x_axis, y_axis, z_axis = accelerometer.acceleration
        return [x_axis, y_axis, z_axis]

if __name__ == "__main__":
    tmp = acc()
    f = open('accelerometer.csv', 'w')

    #while True:
    for _ in range(20):
        x_axis, y_axis, z_axis = tmp.get_acceleration()
        #print("%f %f %f"%tmp.get_acceleration())
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow([x_axis, y_axis, z_axis])
        print('{:.6f} {:.6f} {:.6f}'.format(x_axis, y_axis, z_axis))
        time.sleep(1)

    f.close()

