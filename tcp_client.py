#!/usr/bin/env python3

import socket

s_host = "127.0.0.1"
s_port = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.connect((s_host, s_port))  # 서버의 accept() 함수와 대응, 3-Way handshaking

msg = b'This is the message.'
#sock.sendto(msg, (s_host, s_port))
sock.sendall(msg)

#print("CLIENT : ", sock)

sock.close()
