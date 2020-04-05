#テスト用プログラム
from network.tcp import *
import numpy as np
import cv2
import pygame
from PIL import Image
import time
import os

tcp = TCP("192.168.0.105", 8889, server_flag=True)
while True:
	
	data = int(input())
	tcp.send(data.to_bytes(8, 'big'))
	
