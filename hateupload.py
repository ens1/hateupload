#!/usr/bin/env python2
import sys
from socket import *
PORT=1337
HOST="localhost"
ADDR=(HOST, PORT)
s=socket(AF_INET, SOCK_STREAM)
s.connect(ADDR)

fileread=open(sys.argv[1], "rb")
breakfile=fileread.read(4096)

while breakfile:
    s.send(breakfile)
    breakfile=fileread.read(4096)

s.close()

