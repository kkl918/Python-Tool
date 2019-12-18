import time, datetime, pathlib, sys, os, requests, re
from bs4 import BeautifulSoup
from ftplib import FTP

file = r'C:\Users\RSLAB\Desktop\test.xml'



with open(file, 'r', encoding='utf8') as f:

        soup = BeautifulSoup(f, 'lxml').select('item')
        
        for j in soup[2:]: 
            str   = j['id'].split('@')
            if len(str[0]) > 3 and len(str) > 1:
                # print(os.path.join("D:",str[2][26:]))
                file   = [i for i in str[2].split('/') if len(i) > 1]
                target = os.path.join(r'D:\20190828', os.path.join(file[-3],file[-2],file[-1]))
                # print(os.path.join(file[-3],file[-2],file[-1]))
                # if os.path.isfile(target):
                print(target)