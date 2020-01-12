from socket import socket, AF_INET, SOCK_DGRAM
import RPi.GPIO as GPIO

HOST = '172.21.11.163'   
PORT = 5000

s = socket(AF_INET, SOCK_DGRAM)
s.bind((HOST, PORT))

while True:
    msg, address = s.recvfrom(8192)
    print(msg, type(msg))

s.close()