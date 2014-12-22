# -*- coding: utf-8 -*-
"""
Created on 2014/12/16
@author: LEO
"""

#coding=utf-8
import requests
url = 'http://localhost:8080'
path = u'C:reciever.txt'
print path
files = {'file': open(path, 'rb')}
r = requests.post(url, files=files)
print r.url,r.text



if __name__ == '__main__':

    pass
