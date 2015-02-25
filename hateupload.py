#!/usr/bin/env python2
import sys
from socket import *
import hashlib, os
PORT=5511
HOST="hates.life"
ADDR=(HOST, PORT)
s=socket(AF_INET, SOCK_STREAM)
s.connect(ADDR)



fileread=open(sys.argv[1], "rb")
fsize=os.path.getsize(sys.argv[1])

while True:
    data=s.recv(4096)
    if data==":filetype":
        s.send(sys.argv[1].split(".")[-1])
    if data==":upload":
        print "uploading file"
        s.sendall(fileread.read())
        s.send(":uploaded")

    if data==":fsize":
        s.send(str(fsize))
        print fsize    
    if "hates.life" in data:
        print data
        break
