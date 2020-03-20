from network.tcp import *
import numpy as np
import cv2
import time

tcp = TCP("192.168.0.57", 8889)
cam = cv2.VideoCapture(0)

while True:
	flag,img = cam.read()
	img = cv2.resize(img, (320, 240))
	result, encimg = cv2.imencode('.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), 40])
	jpegstring=encimg.tostring()
	tcp.send(jpegstring) 
	
	k = cv2.waitKey(1)
	if k== 13: 
		break
	a = tcp.receive()

cam.releace()