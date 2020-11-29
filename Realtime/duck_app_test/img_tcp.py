import socket
import numpy as np
import cv2
from tcp_server import TCP

cam = cv2.VideoCapture(1)
height, width = 600, 800
#height, width = 480, 640
host_ip = "192.168.0.192"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
	sock.connect((host_ip, 8889))
	while True:
		try:
			flag,img = cam.read()
			if not cam.isOpened():
				print("error")
				break

			img = cv2.resize(img, (width, height))
			sock.send(img)
		
		except KeyboardInterrupt:
			cam.release()
			print("released")
			break

print("end")
cam.release()