#!/usr/bin/env python2


from socket import *
import random, string

PORT=1337
HOST='localhost'
BUFFER=4096
ADDR=(HOST, PORT)
serversocket = socket(AF_INET,SOCK_STREAM)
serversocket.bind(ADDR)
serversocket.listen(50)



def randomname():
    name=[]
    for i in range(0,7):
        name.append(random.choice(string.ascii_letters + string.digits))
    name=string.join(name, "")
    return name + ".jpg"




while True:
    print "Waiting for connection"
    client, addr = serversocket.accept()
    print addr
    filename=randomname()
    f=open(filename, "wb")
    while True:
        data = client.recv(4096)
        if not data:
            break
        while data:
            f.write(data)
            data = client.recv(4096)
    f.close()
    client.close()
serversocket.close()
