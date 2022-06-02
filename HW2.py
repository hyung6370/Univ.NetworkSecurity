#!/usr/bin/env python3

import socket
import sys

target_host1 = sys.argv[1]  # 첫번째 IP 주소 입력
target_host2 = sys.argv[2]  # 두번째 IP 주소 입력

inputIP_1 = int(".".join([*target_host1.split(".")[3:]]))   # IP주소 뒷자리 세자리만 가져옴
inputIP_2 = int(".".join([*target_host2.split(".")[3:]]))   # IP주소 뒷자리 세자리만 가져옴
ip_addr = ".".join([*target_host2.split(".")[:3]])  # IP주소 뒤 3자리 제외한 주소 

for inputIP_1 in range(inputIP_2) : # 첫번쨰 주소부터 마지막 주소까지 반복
    for port in range(0, 10000): # 포트 10000 까지
        changed_ip = ip_addr + "." + str(inputIP_1)  # connect할 ip 주소
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # TCP
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # 객체 재사용 허용

        try:
            serviceTcp = socket.getservbyport(port, 'tcp')  # 서버의 포트에 접속해서 포트에 걸려있는 서비스 이름 가져오기 변수 설정
            result = s.connect_ex((changed_ip, port))  # 참인결과 : 0, 거짓인 경우 : 111
            if result == 0:
                print("[" + ip_addr + "." + str(inputIP_1) + "]")
                print(f'Port {port} ({serviceTcp}) open!')  # 포트와 서비스 이름 가져오기
            
        except:
            pass

        s.close()
