#!/usr/bin/env python3

import socket

host = 'localhost'
port = 12345

# 소켓 객체 생성
# 1. Socket Family : socket.AF_INET (IPv4)
# 2. Socket Type : SOCK_DGRAM(UDP) or SOCK_STREAM(TCP)
# 3. Socket Protocols : IPPROTO_UDP, IPPROTO_TCP

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Binding
sock.bind((host, port))

# 소켓 서버 동작을 구현
#print(sock)
(data, address) = sock.recvfrom(65565)
print(f'received {len(data)} byte from {address}')


# Close
sock.close()
