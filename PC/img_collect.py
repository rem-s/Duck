#データ収集用プログラム

from network.tcp import *
import numpy as np
import cv2
from PIL import Image
import time
import pygame #use for joystick
import sys


###
SCREEN_SIZE = (300, 300)  # 画面サイズ (横/縦)

pygame.init()

X_CENTER = int(SCREEN_SIZE[0]/2)
Y_CENTER = int(SCREEN_SIZE[1]/2)
[circle_x, circle_y] = [X_CENTER, Y_CENTER]     #円の初期位置を設定
pygame.joystick.init()
joy = pygame.joystick.Joystick(0) # create a joystick instance
joy.init() # init instance
###

#1 : IPの変更
tcp = TCP("192.168.0.92", 8889, server_flag=True)# hkato 192.168.0.88
img_n = 0

while True:

	# イベント処理
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	img_n += 1
	receivedstr=tcp.receive(1024*8) 
	
	#narray = np.fromstring(receivedstr,dtype='uint8')  
	#data = cv2.imdecode(narray,1).reshape((64, 64, 3))

	#cv2.imshow("",data)
	#pil_img = Image.fromarray(cv2.cvtColor(data, cv2.COLOR_BGR2RGB))
	#pil_img.save('img/img%d.jpg'%(img_n))
	
	k = cv2.waitKey(0)
	if k== 13: 
		break			
	#2 : PSコントロラーの値を取得
	#ジョイスティック(アナログバー左スティック)状態の取得
	circle_x = int((joy.get_axis(0)+1) * X_CENTER)    #joystick(横軸)の方向キーはは-1～1の範囲で取得できる
	circle_y = int((joy.get_axis(1)+1) * Y_CENTER)    #joystick(縦軸)の方向キーはは-1～1の範囲で取得できる
	print(circle_x,circle_y)
	#上限と下限
	if circle_x < 0:
		circle_x = 0
	elif circle_x > SCREEN_SIZE[0]:
		circle_x = SCREEN_SIZE[0]

	if circle_y < 0:
		circle_y = 0
	elif circle_y > SCREEN_SIZE[1]:
		circle_y = SCREEN_SIZE[1]
		
	data = 0
	#0 1 4
	if circle_x > 100 and circle_x < 200:
		#0
		if circle_y > 100 and circle_y < 200:
			data = 0

		#1
		elif circle_y >= 0 and circle_y <= 100:
			data = 1
		
		#4
		elif circle_y >= 200 and circle_y <= 300:
			data = 4
			

	#2 5
	if circle_x >= 200 and circle_x <= 300:
		#2
		if circle_y >= 0 and circle_y < 150:
			data = 2

		#5
		elif circle_y >= 150 and circle_y <= 300:
			data = 5


	#3 6
	if circle_x >= 0 and circle_x <= 100:
		#3
		if circle_y >= 0 and circle_y < 150:
			data = 3
		
		#6
		elif circle_y >= 150 and circle_y <= 300:
			data = 6
	print(data)
	tcp.send(data.to_bytes(8, 'big'))
	
cv2.destroyAllWindows()
