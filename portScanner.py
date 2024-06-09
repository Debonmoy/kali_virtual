
# CyberScecurity tool 
# A simple port scanner script in Python

import socket

def scan (ipaddr, port):
    try:
        s = socket.socket()
        s.settimeout(0.5)
        s.connect((ipaddr,port))
        print("[**]Port "+ str(port) +" is Open")
    except:
        pass

ip =  input('[*]Enter the ip address:: ')
for port in range (0,100):
    scan (ip,port)
