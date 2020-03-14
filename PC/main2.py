from network.udp import *
import time

udp = UDP("192.168.0.56","192.168.0.51", 8889, 8888)

udp.send(b'1')
time.sleep(2)

udp.send(b'0')
time.sleep(2)

udp.send(b'-1')
time.sleep(2)

udp.send(b'0')
time.sleep(2)
	