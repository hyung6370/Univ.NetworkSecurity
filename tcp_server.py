#!/usr/bin/env python3
import socket

host = "127.0.0.1"
port = 12345

parent = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
parent.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
parent.bind((host, port))

parent.listen(10)  # 10대의 클라이언트가 접속 가능하다

(child, address) = parent.accept()

#print("SERVER:parent", parent)
#print("SERVER:child", child)
#(data, address) = child.recvfrom(65565)
data = child.recv(65565)

print(f'received {len(data)} bytes from {address}')

child.close()
parent.close()
