# TCP class
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

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
			self.soc.listen(10)
			
			print("waiting for connection....")
			self.client_soc, self.client_ip = self.soc.accept()
			
		#set and connect client socket
		else:
			self.soc = socket(AF_INET, SOCK_STREAM)
			self.soc.connect((self.server_ip, self.port))
		
		print("connected")
		
	#TCP receive
	def receive(self, size):
		if self.server_flag: return self.client_soc.recv(size)
		else: return self.soc.recv(size)

	#TCP send
	def send(self, data):
		if self.server_flag: self.client_soc.sendall(data)
		else: self.soc.send(data)