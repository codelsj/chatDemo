#!/usr/bin/env python
 
'''
File: server.py
Author: foglsj@126.com
'''


import socket
import select


PORT = 8888

socket_list = []
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(('0.0.0.0',PORT))
server_sock.listen(10)
socket_list.append(server_sock)

print 'listen in %s'%PORT


def broadcast(from_socket,data):
    for so in socket_list:
        if so != server_sock and so != from_socket:
            so.send(data)


while 1:
    read_sockets,write_socket,error_sockets = select.select(socket_list,[],[])
    for s in read_sockets:
        if s == server_sock:
            #new info
            cl_socket,addr = server_sock.accept()
            socket_list.append(cl_socket)
            print 'new client connected [%s %s]'% addr
            broadcast(cl_socket,'[%s:%s] in:'%addr)
        else:
            #other msg
            data = s.recv(4096)
            if data:
                broadcast(s,'[' + str(s.getpeername()) +']'+ data)
