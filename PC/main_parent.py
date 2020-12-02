from gui.ps4 import *
from network.tcp import * 
import pygame

ip = "127.0.0.1"
tcp = TCP(ip, 8890, server_flag=True)
controller = PS()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	data = controller.get_ps()
	tcp.send(data)
	tcp.receive(1)
