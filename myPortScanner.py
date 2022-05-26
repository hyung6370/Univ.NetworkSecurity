#!/usr/bin/env python3

import socket
import sys

target_host = sys.argv[1]

for port in range(0, 1024):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
       #result = s.connect((target_host, port)) #return이 None
        result = s.connect_ex((target_host, port))  #참인결과 : 0, 거짓인 경우: 111
        if result == 0:
            print(f'Port {port} open!')
    except:
        pass

    s.close()
