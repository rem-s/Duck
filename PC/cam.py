from network.tcp import *
from control.process.image import *
import numpy as np
import cv2
import time

tcp = TCP("192.168.0.88", 8889, server_flag=True)

while True:
	
	receivedstr=tcp.receive(1024*8) 
	
	narray = np.fromstring(receivedstr,dtype='uint8')  
	print(narray.shape)
	img = cv2.imdecode(narray,1).reshape((160, 120, 3))
	height, width, channel = img.shape
	
	grayFrame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	b_img = Mean(grayFrame)
	l_img = labeling(b_img)
	r_img = under_comarea(l_img)
	img = img.reshape(width*height, channel)
	img[np.where(r_img.reshape(-1) == 1)] = [0, 255, 0] 
	img = img.reshape(height, width, channel)
	
	img = cv2.resize(img, (640, 480))
	cv2.imshow("",img)
	k = cv2.waitKey(1)
	if k== 13: 
		break
	tcp.send(b'1')
	
cv2.destroyAllWindows()