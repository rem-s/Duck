from network.tcp import *
from control.process.image import *
import numpy as np
import pygame
import cv2
import time

tcp = TCP("192.168.0.88", 8889, server_flag=True)

SCREEN_SIZE = (300, 300)
pygame.init()

X_CENTER = int(SCREEN_SIZE[0]/2)
Y_CENTER = int(SCREEN_SIZE[1]/2)
[circle_x, circle_y] = [X_CENTER, Y_CENTER]
pygame.joystick.init()
joy = pygame.joystick.Joystick(0)
joy.init()

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
	
	#2 : PSコントロラーの値を取得
	# イベント処理
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	
	#ジョイスティック(アナログバー左スティック)状態の取得
	circle_x = int((joy.get_axis(0)+1) * X_CENTER)
	circle_y = int((joy.get_axis(1)+1) * Y_CENTER)
	print(circle_x, circle_y)
	#上限と下限
	if circle_x < 0: circle_x = 0
	elif circle_x > SCREEN_SIZE[0]: circle_x = SCREEN_SIZE[0]
	
	if circle_y < 0: circle_y = 0
	elif circle_y > SCREEN_SIZE[1]: circle_y = SCREEN_SIZE[1]
		
	data = 0
	if circle_x > 100 and circle_x < 200:
		if circle_y > 100 and circle_y < 200: data = 0
		elif circle_y >= 0 and circle_y <= 100: data = 1
		elif circle_y >= 200 and circle_y <= 300: data = 4
	if circle_x >= 200 and circle_x <= 300:
		if circle_y >= 0 and circle_y < 150: data = 2
		elif circle_y >= 150 and circle_y <= 300: data = 5
	if circle_x >= 0 and circle_x <= 100:
		if circle_y >= 0 and circle_y < 150: data = 3
		elif circle_y >= 150 and circle_y <= 300: data = 6
	print(data)
	tcp.send(data.to_bytes(8, 'big'))
	
cv2.destroyAllWindows()