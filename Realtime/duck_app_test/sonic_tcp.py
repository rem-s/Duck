import socket
import time
import random

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect(("192.168.10.103", 8887))
    sendlist = []
    while True:
        try:
            sendnum = random.randint(0, 100)+100
            #sock.sendall(bytes(str(sendnum), encoding='UTF-8'))
            sendsize = len(str(sendnum))
            sock.send(sendnum.to_bytes(sendsize, byteorder="big"))
            #data = sock.recv(1024)
            #print(repr(data))
            time.sleep(60/1000)
            sendlist.append(sendnum)
        except KeyboardInterrupt:
            break
    print(sendlist)