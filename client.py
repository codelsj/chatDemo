#!/usr/bin/env python
 
'''
File: client.py
Author: foglsj@126.com
'''

import socket
import select
import sys


IP = '127.0.0.1'
PORT = 8888

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.connect((IP,PORT))

while True:
    rlist = [sys.stdin,sock]
    read_list,write_list,error_list = select.select(rlist,[],[])
    
    for s in read_list:
        if s == sock:
            data = sock.recv(4096)
            if data  == '':
                print 'disconnected!'
                sys.exit(1)
            else:
                print data

        else:
            msg = sys.stdin.readline()
            sock.send(msg)







