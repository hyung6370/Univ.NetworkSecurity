#!/usr/bin/env python3

import socket
import sys

target_host1 = sys.argv[1]  # 첫번째 IP 주소 입력
target_host2 = sys.argv[2]  # 두번째 IP 주소 입력

inputIP_1 = int(".".join([*target_host1.split(".")[3:]]))   # IP주소 뒷자리 세자리만 가져옴
inputIP_2 = int(".".join([*target_host2.split(".")[3:]]))   # IP주소 뒷자리 세자리만 가져옴
ip_addr = ".".join([*target_host2.split(".")[:3]])  # IP주소 뒤 3자리 제외한 주소 

def findPort(a):
    for port in range(0, 100): # 포트 100 까지
        print(f'{changed_ip} Port {port} Searching...')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # TCP
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # 객체 재사용 허용
        try:
            serviceTcp = socket.getservbyport(port, 'tcp')  # 서버의 포트에 접속해서 포트에 걸려있는 서비스 이름 가져오기 변수 설정
            result = s.connect_ex((a, port))  # 참인결과 : 0, 거짓인 경우 : 111
            if result == 0:
                print(f'Port {port} ({serviceTcp}) open!')  # 포트와 서비스 이름 가져오기
        except:
            pass
        s.close()

for i in range(inputIP_1, inputIP_2) : # 첫번쨰 주소부터 마지막 주소까지 반복
    changed_ip = ip_addr + "." + str(i)  # connect할 ip 주소
    print("[" + ip_addr + "." + str(i) + "]")   # ip 주소 출력
    findPort(changed_ip)    # findPort함수 실행
        
