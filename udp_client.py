#!/usr/bin/env python3

import socket

s_host = '127.0.0.1'
s_port = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 클라이언트 동작

#print(sock)
msg = b'This is the message.'
sock.sendto(msg, (s_host, s_port))


sock.close()
