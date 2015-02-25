#!/usr/bin/env python2


from socket import *
import random, string, hashlib, os, shutil

PORT=5511
HOST=''
BUFFER=4096
ADDR=('', PORT)
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
    client, addr = serversocket.accept()
    filename=randomname()
    f=open(filename, "wb")
    gotfile=False
    print addr
    while True:
        #Get file extension
        client.sendall(":filetype")
        filetype=client.recv(4096)
        #get file data
        client.sendall(":upload")
        while gotfile==False:
            fileget=client.recv(4096)
            if fileget==":uploaded":
                gotfile=True
                break
            f.write(fileget)
        f.close()
        #Compare file sizes
        client.sendall(":fsize")
        fsize=client.recv(4096)
        new_file_fsize=str(os.path.getsize(filename))
        if(fsize==new_file_fsize):
            shutil.move(filename, "/var/www/daily/" + filename + "." + filetype)
            client.sendall("http://hates.life/daily/" + filename + "." + filetype)
            break
        if(fsize!=new_file_fsize):
            client.sendall(":failed")
            break
serversocket.close()
