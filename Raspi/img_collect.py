#データ収集用プログラム

from network.tcp import *
import numpy as np
import cv2
from PIL import Image
import time

tcp = TCP("192.168.0.88", 8889, server_flag=True)
img_n = 0

while True:

	img_n += 1
	receivedstr=tcp.receive(1024*8) 
	
	narray = np.fromstring(receivedstr,dtype='uint8')  
	data = cv2.imdecode(narray,1).reshape((64, 64, 3))

	cv2.imshow("",data)
	pil_img = Image.fromarray(cv2.cvtColor(data, cv2.COLOR_BGR2RGB))
	pil_img.save('img/img%d.jpg'%(img_n))
	
	k = cv2.waitKey(0)
	if k== 13: 
		break
		
	
	tcp.send(.to_bytes(8, 'big'))
	
cv2.destroyAllWindows()
