import queue
import socket
import threading
from typing import List

import paramiko

MY_IP = socket.gethostbyname(socket.gethostname())
IP_RANGE = [".".join([*MY_IP.split(".")[:3], str(i)]) for i in range(1, 255)]
PORT = 22
THREAD_NUM = 40

USERNAME = "유저이름"
PASSWORD = "비밀번호"

print(f"IP SCAN RANGE: {IP_RANGE[0]}-{IP_RANGE[-1]}")

socket.setdefaulttimeout(1)
QUE: queue.Queue = queue.Queue()
PRINT_LOCK = threading.Lock()

accept_ip: List[str] = []
accept_ssh: List[str] = []
error_msg: List[str] = []

def scan_ip(ip):
    print(f"\rscanning... {ip}", end="")
    try:
        con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        con.connect((ip, PORT))
        con.send(b'Primal Security \n')
        service_name = con.recv(1024).decode('utf-8').strip()
        ip_hostname = socket.getfqdn(ip)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh.connect(ip, port=22, username=USERNAME, password=PASSWORD)
        stdout = ssh.exec_command("hostname")[1]
        ssh_hostname = stdout.read().decode('utf-8').strip()
        ssh.close()
        with PRINT_LOCK:
            accept_ip.append(f"{ip} ({ip_hostname}): {service_name}")
            accept_ssh.append(f"{ip} ({ssh_hostname})")
    except socket.error as msg:
        error_msg.append(f"{ip}: {msg}")
        con.close()


def result_get():
    while True:
        worker = QUE.get()
        scan_ip(worker)
        QUE.task_done()

if __name__ == '__main__':
    for i in range(THREAD_NUM):
        thread_push = threading.Thread(target=result_get)
        thread_push.daemon = True
        thread_push.start()
    for ip in IP_RANGE:
        QUE.put(ip)
    QUE.join()

    print()
    print("\n".join(error_msg))
    print("\n".join(accept_ip))
    print("\n".join(accept_ssh))
