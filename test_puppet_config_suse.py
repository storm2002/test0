#!/usr/bin/env python3
import paramiko
import getpass
import os
import sys

name = input("Please enter the Username: ")
password = getpass.getpass("Please enter the Password: ")

commands = sys.argv[1]
ips = sys.argv[2]

with open(commands) as com:
    com = com.read().splitlines()

with open(ips) as ip:
    ip = ip.read().splitlines()

for add in ip:

    for i in com:
            ssh_c = paramiko.SSHClient()
            ssh_c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_c.connect(hostname=add, username=name, password=password, timeout=3) #allow_agent=False,look_for_keys=False
            stdin, stdout, stderr = ssh_c.exec_command(i)
            data = stdout.read() + stderr.read()
            print(data)
            ssh_c.close()

