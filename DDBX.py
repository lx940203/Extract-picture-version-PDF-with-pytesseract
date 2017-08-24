# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 17:09:16 2017

@author: lx940
"""
from PyPDF2.pdf import PdfFileReader
from pytesseract import *
import pytesseract
from PIL import Image
import os
import csv
from PyPDF2 import  PdfFileWriter


path=r'J:/桌面/输出'
csvfile = open('J:/桌面/RA/BCFFOUTPUT'+'/'+'lmq.csv', 'w', newline='')
writer = csv.writer(csvfile)   
fns=[os.path.join(root,fn) for root,dirs,files in os.walk(path) for fn in files]
row=[]
for f in fns: 
    image = Image.open(f)
    ltext= pytesseract.image_to_string(image)
    outstring=ltext[567:]
    outstring=outstring[:outstring.find('\n\n')]
    tem1=outstring.split('\n')
    for item in tem1:
        ccc=item.split()
        writer.writerow(ccc)     

csvfile.close()