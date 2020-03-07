# UDP class
from socket import socket, AF_INET, SOCK_DGRAM

class UDP:
	def __init__(self,
				master_ip,
				slave_ip,
				sport,
				rport):
				
		#set comunication information
		self.master_ip = master_ip
		self.slave_ip = slave_ip
		self.sport = sport
		self.rport = rport
		
		#set and connect socket
		self.socket = socket(AF_INET, SOCK_DGRAM)
		self.socket.bind((self.slave_ip, self.rport))
		
	def receive(self):
		
		#receiving data
		data, addr = self.socket.recvfrom(1024)
		return data
		
	def send(self, data):
	
		#sending data
		self.socket.sendto(data, (self.slave_ip, self.sport))
		