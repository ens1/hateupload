#!/usr/bin/env python2


from socket import *
import random, string, hashlib, os

PORT=5511
HOST=socket.gethostname()
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
    return name



while True:
    print "Waiting for connection"
    client, addr = serversocket.accept()
    print addr
    filename=randomname()
    f=open(filename, "wb")
    while True:
        #Get file extension
        client.send(":filetype")
        filetype=client.recv(4096)
        print filetype
        #get file data
        client.send(":upload")
        while True:
            fileget=client.recv(4096)
            f.write(fileget)
            if len(fileget) < 4096:
                break
        f.close() 
        print "file got"
        
        #Compare file sizes
        client.send(":fsize")
        fsize=client.recv(4096)
        new_file_fsize=str(os.path.getsize(filename))
        if(fsize==new_file_fsize):
            os.rename(filename, "/var/www/daily/" + filename + "." + filetype)
            client.send("hates.life/daily/" + filename + "." + filetype)
            break
serversocket.close()
