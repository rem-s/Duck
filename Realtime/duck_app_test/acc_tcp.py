import socket
import time
import random

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect(("192.168.10.103", 8888))
    sendlist = [0, 0, 0]
    result = []
    while True:
        try:
            for i in range(3):
                sendlist[i] = random.randint(-50, 50)+150
                #sock.send(bytes(str(sendlist[i]), encoding='UTF-8'))
                sendsize = len(str(sendlist[i]))
                sock.send(sendlist[i].to_bytes(sendsize, byteorder="big"))
            #data = sock.recv(1024)
            #print(repr(data))
            time.sleep(60/1000)
            result.append(sendlist)
        except KeyboardInterrupt:
            break
    print(result)