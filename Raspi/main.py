from network.udp import *
#from control.motor.ta7291 import *

ins = UDP("127.0.0.1","127.0.0.1", 50000, 50001)
print(ins.print_debug())
