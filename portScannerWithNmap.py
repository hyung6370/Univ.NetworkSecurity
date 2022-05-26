#!/usr/bin/env python3

import sys
import nmap
nm = nmap.PortScanner()

target_host = '127.0.0.1'
target_port = '22'

argc = len(sys.argv)

if argc > 1 and sys.argv[1] != '':
    target_host = sys.argv[1]
if argc > 2 and sys.argv[2] != '':
    target_port = sys.argv[2]

nm.scan(target_host, target_port)

for host in nm.all_hosts():
    print(f'Host: {host} {nm[host].hostname()}')
    print(f'State: {nm[host].state()}')

    for protocol in nm[host].all_protocols():
        print(f'Protocol:{protocol}')
