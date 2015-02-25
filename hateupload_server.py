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
    while True:
        #Get file extension
        client.send(":filetype")
        filetype=client.recv(4096)
        #get file data
        client.send(":upload")
        while True:
            fileget=client.recv(4096)
            print "getting file" + str(len(fileget))
            print fileget[9]
            if fileget==":uploaded":
                print "got file"
                break
            f.write(fileget)
        
        #Compare file sizes
        client.send(":fsize")
        fsize=client.recv(4096)
        new_file_fsize=str(os.path.getsize(filename))
        print "local" + new_file_fsize
        print "orig" + fsize
        if(fsize==new_file_fsize):
            shutil.move(filename, "/var/www/daily/" + filename + "." + filetype)
            client.send("hates.life/daily/" + filename + "." + filetype)
            f.close()
            break
serversocket.close()
