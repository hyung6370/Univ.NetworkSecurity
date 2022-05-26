#!/usr/bin/env python3

import socket

s_host = 'www.google.com'
s_port = 80

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s_ipaddr = socket.gethostbyname(s_host)

sock.connect((s_ipaddr, s_port))

print(sock)
print(f'Socket connected to {s_host} on {s_ipaddr}')

msg = b'GET / HTTP/1.1\r\n\r\n'
sock.sendall(msg)

data = sock.recv(65565)

print("From Google:")
print(data)


sock.close()
