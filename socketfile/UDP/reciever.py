# -*- coding: utf-8 -*-
"""
Created on 2014/12/13
@author: LEO
"""



from socket import *
import sys
import select


def reciever():
    host="0.0.0.0"
    port = 9999
    s = socket(AF_INET,SOCK_DGRAM)
    s.bind((host,port))

    addr = (host,port)
    buf=1024

    data,addr = s.recvfrom(buf)
    print "Received File:", data.strip()
    f = open('c://reciever.txt','wb')

    data,addr = s.recvfrom(buf)
    try:
        while(data):
            f.write(data)
            s.settimeout(2)
            data,addr = s.recvfrom(buf)

    except timeout:
        f.close()
        s.close()
        print "File Downloaded"


if __name__ == '__main__':
    reciever()
    pass
