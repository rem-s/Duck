# TCP class
import numpy as np
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from socket import socket, AF_INET, SOCK_DGRAM

class TCP:
	def __init__(self, 
				server_ip,
				port,
				server_flag=False):
		
		#set comunication information
		self.server_ip = server_ip
		self.port = port
		self.server_flag = server_flag
		
		#set and connect server socket
		if self.server_flag:
			self.soc = socket(AF_INET, SOCK_STREAM)
			self.soc.bind((self.server_ip, self.port))
			self.soc.listen(10) # wait for 10 sec
			
			print("waiting for connection....")
			self.client_soc, self.client_ip = self.soc.accept()
			
		#set and connect client socket
		else:
			self.soc = socket(AF_INET, SOCK_STREAM)
			self.soc.connect((self.server_ip, self.port))
			self.send(b"1")
			self.receive(1)
		
	#TCP receive
	def receive(self, size):
		if self.server_flag: return self.client_soc.recv(size)
		else: return self.soc.recv(size)

	#TCP send
	def send(self, data):
		if self.server_flag: self.client_soc.sendall(data)
		else: self.soc.sendall(data)


class UDP:
	def __init__(self,
				my_ip,
				you_ip,
				port,
				server_flag=True):
		
		#set comunication information
		self.my_ip = my_ip
		self.you_ip = you_ip
		self.port = port
		
		#set and connect server socket
		self.socket = socket(AF_INET, SOCK_DGRAM)
		if server_flag: self.socket.bind((self.my_ip, self.port))

		#set and connect client socket
		else:
			self.soc = socket(AF_INET, SOCK_STREAM)
			self.soc.connect((self.server_ip, self.port))
		
	#receiving data
	def receive(self, size):
		data, addr = self.socket.recvfrom(size)
		return data
	#sending data
	def send(self, data):
		self.socket.sendto(data, (self.you_ip, self.port))	
	
	#sending data
	def imgsend(self, data):
		if len(data.reshape(-1)) >= 4096:
			for i in np.split(data.reshape(-1), 39936): self.socket.sendto(i, (self.you_ip, self.port))
		else:
			self.socket.sendto(data, (self.you_ip, self.port))
