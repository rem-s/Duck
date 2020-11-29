from tuning import Tuning
import usb.core
import usb.util
import time
 
dev = usb.core.find(idVendor=0x2886, idProduct=0x0018)

if dev:
    Mic_tuning = Tuning(dev)
    data = []
    while True:
        try:
            dir = Mic_tuning.direction
                # if dir > 180
            data.append(dir)
            time.sleep(1)
        except KeyboardInterrupt:
            with open('sound_source.csv') as f:
                f.writelines(data)
            break
    print("done")