#!/usr/bin/env python3

import socket
import sys

target_host = sys.argv[1]

for port in range(0, 10000):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        serviceTcp = socket.getservbyport(port, 'tcp')  # 서버의 포트에 접속해서 포트에 걸려있는 서비스 이름 가져오기 변수 설정
        result = s.connect_ex((target_host, port))  # 참인결과 : 0, 거짓인 경우 : 111
        if result == 0:
            print(f'Port {port} ({serviceTcp}) open!')  # 포트와 서비스 이름 가져오기
    except:
        pass

    s.close()

