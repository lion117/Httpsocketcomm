# -*- coding: utf-8 -*-
"""
Created on 2014/12/13
@author: LEO
"""


from socket import *
import sys



def sender():
    s = socket(AF_INET,SOCK_DGRAM)
    host ='192.168.117.102'
    port = 9999
    buf =1024
    addr = (host,port)

    file_name='c://test.txt'

    s.sendto(file_name,addr)

    f=open(file_name,"rb")
    data = f.read(buf)
    while (data):
        if(s.sendto(data,addr)):
            print "sending ..."
            data = f.read(buf)
    s.close()
    f.close()



if __name__ == '__main__':
    sender()
    pass
