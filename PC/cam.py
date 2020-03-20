from network.tcp import *
import numpy as np
import cv2
import time

tcp = TCP("192.168.0.57", 8889, server_flag=True)

while True:
	
	receivedstr=tcp.receive(1024*8) 
	
	narray = np.fromstring(receivedstr,dtype='uint8')  
	data = cv2.imdecode(narray,1).reshape((240, 320, 3))
	data = cv2.resize(data, (640, 480))
	
	cv2.imshow("",data)
	k = cv2.waitKey(1)
	if k== 13: 
		break
	tcp.send(b'1')
	
cv2.destroyAllWindows()