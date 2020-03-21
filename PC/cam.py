from network.tcp import *
from control.process.image import *
import numpy as np
import cv2
import time

tcp = TCP("192.168.0.57", 8889, server_flag=True)

while True:
	
	receivedstr=tcp.receive(1024*8) 
	
	narray = np.fromstring(receivedstr,dtype='uint8')  
	img = cv2.imdecode(narray,1).reshape((240, 320, 3))
	#data = cv2.resize(data, (640, 480))
	height, width, channel = img.shape
	
	grayFrame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	b_img = Otsu(grayFrame)
	l_img = labeling(b_img)
	r_img = under_comarea(l_img)
	img = img.reshape(width*height, channel)
	img[np.where(r_img.reshape(-1) == 1)] = [0, 255, 0] 
	img = img.reshape(height, width, channel)
	
	cv2.imshow("",img)
	k = cv2.waitKey(1)
	if k== 13: 
		break
	tcp.send(b'1')
	
cv2.destroyAllWindows()