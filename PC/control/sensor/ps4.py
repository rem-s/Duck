# ps4 contrller
from socket import socket, AF_INET, SOCK_DGRAM
import pygame
import sys

class PS:

    def __init__(self):
        ###
        self.SCREEN_SIZE = (300, 300)  # 画面サイズ (横/縦)

        pygame.init()

        self.X_CENTER = int(self.SCREEN_SIZE[0]/2)
        self.Y_CENTER = int(self.SCREEN_SIZE[1]/2)
        [self.circle_x, self.circle_y] = [self.X_CENTER, self.Y_CENTER]     #円の初期位置を設定
        pygame.joystick.init()
        self.joy = pygame.joystick.Joystick(0) # create a joystick instance
        self.joy.init() # init instance
        ###

    def get_ps(self):

        self.circle_x = int((self.joy.get_axis(0)+1) * self.X_CENTER)    #joystick(横軸)の方向キーはは-1～1の範囲で取得できる
        self.circle_y = int((self.joy.get_axis(1)+1) * self.Y_CENTER)    #joystick(縦軸)の方向キーはは-1～1の範囲で取得できる
        #print(circle_x,circle_y)

        #上限と下限
        if self.circle_x < 0:
            self.circle_x = 0
        elif self.circle_x > self.SCREEN_SIZE[0]:
            self.circle_x = self.SCREEN_SIZE[0]

        if self.circle_y < 0:
            self.circle_y = 0
        elif self.circle_y > self.SCREEN_SIZE[1]:
            self.circle_y = self.SCREEN_SIZE[1]
    
        data = 0
        #0 1 4
        if self.circle_x > 100 and self.circle_x < 200:
            #0
            if self.circle_y > 100 and self.circle_y < 200:
                data = 0

            #1
            elif self.circle_y >= 0 and self.circle_y <= 100:
                data = 1
    
            #4
            elif self.circle_y >= 200 and self.circle_y <= 300:
                data = 4
        

        #2 5
        if self.circle_x >= 200 and self.circle_x <= 300:
            #2
            if self.circle_y >= 0 and self.circle_y < 150:
                data = 2

            #5
            elif self.circle_y >= 150 and self.circle_y <= 300:
                data = 5


        #3 6
        if self.circle_x >= 0 and self.circle_x <= 100:
            #3
            if self.circle_y >= 0 and self.circle_y < 150:
                data = 3
    
            #6
            elif self.circle_y >= 150 and self.circle_y <= 300:
                data = 6

        return data

controller = PS()
while True:

    # イベント処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    data = controller.get_ps()
    for i in range(data):
        print('DDDDDD  ',end = '')

    print()