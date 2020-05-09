import socket
import numpy as np
import cv2

cam = cv2.VideoCapture(0)
height, width = 60, 80
#height, width = 480, 640

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
	sock.connect(("192.168.10.103", 8889))
	while True:
		flag,img = cam.read()
		if not cam.isOpened():
			print("error")
			break
		
		img = cv2.resize(img, (width, height))
		#print(img.shape)
		result, encimg = cv2.imencode('.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), 80])
		if not result:
			print("encode error")
			break
		
		#print(type(encimg), encimg.shape, encimg)
		#sendimg = bytes(encimg)
		sendimg = img
		print(len(sendimg))
		sock.sendall(sendimg)
		if cv2.waitKey(1) == ord('q'):
			break

cam.release()