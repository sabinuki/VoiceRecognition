import subprocess
import socket
import string
import os
import random
import numpy as np
from numpy.random import *
import time


host = "localhost"
port = 10500

p = subprocess.Popen(["sh ../shell/julius_start.sh"], stdout=subprocess.PIPE, shell=True)

# juliusのプロセスID取得
pid = str(p.stdout.read().decode('utf-8'))
time.sleep(5)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((host, port))

    data = ""
    killword = ""

    while True:
        while (1):
            if '</RECOGOUT>¥n' in data:
                strTemp = ""
                for line in data.split('¥n'):
                    index = line.find('WORD="')
                    if index != -1:
                        line = line[index + 6: line.find('"', index + 6)]
                        strTemp += str(line)

                    if strTemp == 'バイバイ':
                        if killword != 'バイバイ':
                            print("Result: " + strTemp)
                            print("<<<please speak>>>")
                            killword = "バイバイ"

                    elif strTemp == 'おはよう':
                        if killword != 'おはよう':
                            print("Result: " + strTemp)
                            print("<<<please speak>>>")
                            killword = "おはよう"

                    else:
                        print("Result: " + strTemp)

                        print("<<<please speak>>>")
                    data =""
    else:
        data += str(sock.recv(1024).decode(utf-8))



