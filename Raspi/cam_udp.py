from network.udp import *
import numpy as np
import cv2

#camera set
cam = cv2.VideoCapture(0)
udp = UDP("192.168.0.51","192.168.0.56", 8888, 8889)

while True:
	flag, img = cam.read()
	img = cv2.resize(img, (50, 50))
	udp.send(img.tostring())
