from network.tcp import *
from control.process.image import *
import numpy as np
import pygame
import cv2
import time

#画像インデックス取得
height = 90
width = 120
channel = 3
target_height = int(height/3*2)
indexs_flat, indexs_dim = target_indexs(height, width, target_height=target_height)

tcp = TCP("192.168.0.105", 8889, server_flag=True)
print("connected")

while True:
	
	receivedstr=tcp.receive(1024*8) 

	narray = np.fromstring(receivedstr,dtype='uint8')  
	img = cv2.imdecode(narray,1).reshape((height, width, channel))
	
	grayFrame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	b_img = mean_binarize(grayFrame, indexs=indexs_flat)
	l_img = labeling(b_img, indexs=indexs_dim)
	r_img = compare_area(l_img)
	degree, top_feature_point, bottom_feature_point, tip, rear = image_line_degree(r_img)
	
	img = img.reshape(width*height, channel)
	img[np.where(r_img.reshape(-1) == 1)] = [0, 255, 0]
	img = img.reshape(height, width, channel)
	
	img[top_feature_point-1:top_feature_point+1, tip-1:tip+1, :] = [0, 0, 0]
	img[bottom_feature_point-1:bottom_feature_point+1, rear-1:rear+1, :] = [0, 0, 0]
	img = cv2.line(img, (tip,top_feature_point), (rear,bottom_feature_point), (255,0,0), thickness = 1)
	
	""" 対象LINE表示
	#img = cv2.line(img, (f1(np.array(height), height, width),height), (f1(np.array(target_height), height, width), target_height), (0,0,0), thickness = 1)
	#img = cv2.line(img, (f2(np.array(height), height, width),height), (f2(np.array(target_height), height, width), target_height), (0,0,0), thickness = 1)
	#img = cv2.line(img, (f1(np.array(target_height), height, width), target_height), (f2(np.array(target_height), height, width), target_height), (0,0,0), thickness = 1)
	"""
	
	img = cv2.resize(img, (width*2, height*2))
	img = cv2.putText(img, '%d'%(degree), (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
	cv2.imshow("",img)
	
	k = cv2.waitKey(1)
	if k== 13: 
		break

	#ls = int(input())
	data = 1
	tcp.send(data.to_bytes(8, 'big'))
	
cv2.destroyAllWindows()