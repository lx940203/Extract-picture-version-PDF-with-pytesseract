# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 11:23:28 2017

@author: lx940
"""

from PyPDF2.pdf import PdfFileReader
from pdfminer.pdfinterp import PDFResourceManager,process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
import csv
import re
import os
from PyPDF2 import  PdfFileWriter



def readPDF(pdffile):
    rsrcmgr=PDFResourceManager()
    retstr=StringIO()
    laparams=LAParams()
    device=TextConverter(rsrcmgr,retstr,laparams=laparams)
    process_pdf(rsrcmgr,device,pdffile)
    device.close()
    content=retstr.getvalue()
    retstr.close()
    return content

def read2010_2011(page):
    pdf = PdfFileReader(open(f, 'rb'))
    Page1 = pdf.getPage(page).rotateClockwise(90)
    output = PdfFileWriter()
    output.addPage(Page1)
    outputStream = open('J:/桌面/RA/GetGreenBook/GS-2010.pdf', "wb")
    output.write(outputStream)
    outputStream.close()
    pdffile=open('J:/桌面/RA/GetGreenBook/GS-2010.pdf','rb')
    outputString=readPDF(pdffile)
    ExtractString=outputString[outputString.find('Changes in Prices and Costs'):]
    Year1=set(re.findall("20[0,1][0-9]", ExtractString))
    Year2=list(Year1)
    Year2.sort()
    Year=[]
    for i in range(0,3):
        Year.append(Year2[i])
        Year.append(Year2[i])
        Year.append(Year2[i])
        Year.append(Year2[i])
                         
                    
    Extract1String1=ExtractString[ExtractString.find('GDP chain-wt'):ExtractString.find('PCE chain-wt')]
    GDP1=re.findall("\-?[0-9]?\.[0-9]", Extract1String1)
    GDP=GDP1[:12]
    
    Extract1String1=ExtractString[ExtractString.find('PCE chain-wt'):]
    GDP1=re.findall("\-?[0-9]?\.[0-9]", Extract1String1)
    PCE=GDP1[:12]    
    
    Extract1String1=ExtractString[ExtractString.find('CPI'):]
    GDP1=re.findall("\-?[0-9]?\.[0-9]", Extract1String1)
    CPI=GDP1[:12]
    
    for i in range(0,len(GDP)):
        rowtem=[GreenBookTime[0:4],GreenBookTime[5:7],Year[i],Quater[i],GDP[i],PCE[i],CPI[i]]
        row.append(rowtem)

row=[['Report Year','Report Month','Year','Quater','GDP chn.-wt','PCE chn.-wt','CPI']]
Quater=[]
for i in range(0,5):
    Quater.append('Q1')
    Quater.append('Q2')
    Quater.append('Q3')
    Quater.append('Q4')

path=r'J:/桌面/RA/Greenbook/'
tem0=[]

fns2=['2005-09', '2005-11', '2005-12', '2006-01', '2006-03', '2006-05', '2006-06', '2006-08', '2006-09', '2006-10', '2006-12', '2007-01', '2007-03', '2007-05', '2007-06', '2007-08', '2007-09', '2007-10', '2007-12', '2008-01', '2008-03', '2008-04', '2008-06', '2008-08', '2008-09', '2008-10', '2008-12', '2009-01', '2009-03', '2009-04', '2009-06', '2009-08', '2009-09', '2009-11', '2009-12']
fns3=['2010-04', '2010-06', '2010-03','2010-01']
fns5=['2010-08','2010-09','2010-10','2010-12','2011-01','2011-03','2011-04','2011-06','2011-08','2011-09','2011-10','2011-12']


fns=[os.path.join(root,fn) for root,dirs,files in os.walk(path) for fn in files]

for f in fns:
    GreenBookTime=re.findall("[1,2]\d\d\d\-[0-9][0-9]", f)[0]
    if GreenBookTime in fns2:
        pdf = PdfFileReader(open(f, 'rb'))
        extractedText = pdf.getPage(13).extractText()
        if extractedText.find('GDP chain-wt')==-1:
            extractedText = pdf.getPage(14).extractText()
            if extractedText.find('GDP chain-wt')==-1:
                extractedText = pdf.getPage(15).extractText() 
                if extractedText.find('GDP chain-wt')==-1:
                    extractedText = pdf.getPage(16).extractText() 
                    if extractedText.find('GDP chain-wt')==-1:
                        extractedText = pdf.getPage(17).extractText() 
                        if extractedText.find('GDP chain-wt')==-1:
                            extractedText = pdf.getPage(17).extractText() 
                            if extractedText.find('GDP chain-wt')==-1:
                                extractedText = pdf.getPage(18).extractText() 
                                if extractedText.find('GDP chain-wt')==-1:
                                    extractedText = pdf.getPage(19).extractText() 
                                    if extractedText.find('GDP chain-wt')==-1:
                                        extractedText = pdf.getPage(19).extractText() 
                                        if extractedText.find('GDP chain-wt') ==-1:
                                            extractedText = pdf.getPage(33).extractText() 
                                            if  extractedText.find('GDP chain-wt') ==-1 or not extractedText.find('Q1'):
                                                extractedText = pdf.getPage(34).extractText() 
                                                if  extractedText.find('GDP chain-wt') ==-1 or not extractedText.find('Q1'):
                                                    extractedText = pdf.getPage(35).extractText() 
                                                    if  extractedText.find('GDP chain-wt') ==-1 or not extractedText.find('Q1'):
                                                        extractedText = pdf.getPage(36).extractText() 
                                                        if  extractedText.find('GDP chain-wt') ==-1 or not extractedText.find('Q1'):
                                                            extractedText = pdf.getPage(37).extractText() 
                                    
                                    
                                    
                                    
                                
        Year1=set(re.findall("20[0,1][0-9]", extractedText))
        Year2=list(Year1)
        Year2.sort()
        ExtractString=extractedText[extractedText.find('GDP chain'):]
        GDPTotal=ExtractString[:ExtractString.find('Previous')]
        GDP=re.findall("\-?[0-9]?\.[0-9]", GDPTotal)[:12]

        ExtractString=extractedText[extractedText.find('PCE chain'):]
        PCETotal=ExtractString[:ExtractString.find('Previous')]
        PCE=re.findall("\-?[0-9]?\.[0-9]", PCETotal)[:12]
        
        ExtractString=extractedText[extractedText.find('CPI'):]
        CPITotal=ExtractString[:ExtractString.find('Previous')]
        CPI=re.findall("\-?[0-9]?\.[0-9]", CPITotal)[:12]
             
             
             
        Year=[]
        for i in range(0,3):
            Year.append(Year2[i])
            Year.append(Year2[i])
            Year.append(Year2[i])
            Year.append(Year2[i])
            
        Quater=[]
        for i in range(0,3):
            Quater.append('Q1')
            Quater.append('Q2')
            Quater.append('Q3')
            Quater.append('Q4')
        
            
        for i in range(0,len(GDP)):
            rowtem=[GreenBookTime[0:4],GreenBookTime[5:7],Year[i],Quater[i],GDP[i],PCE[i],CPI[i]]
            row.append(rowtem)   

    else:
        if not GreenBookTime in fns3:
            if not GreenBookTime in fns5:
                pdf = PdfFileReader(open(f, 'rb'))
                extractedText = pdf.getPage(9).extractText()+pdf.getPage(10).extractText()+pdf.getPage(11).extractText()+pdf.getPage(12).extractText()+pdf.getPage(13).extractText()+pdf.getPage(14).extractText()+pdf.getPage(15).extractText()
                extractedText=extractedText[extractedText.find('QUARTERLY VALUES'):]
                ExtractString=extractedText[extractedText.find('-wt'):]
                if not GreenBookTime in['2003-09','2003-10','2003-12','2004-01','2004-03','2004-05','2004-06','2004-08','2004-09','2004-11','2004-12','2005-02' ,'2005-03','2005-05','2005-06','2005-08'] :
                    Year=re.findall("20[0,1][0-9]|1999", extractedText)[1:]
                else:
                    Year=re.findall("20[0,1][0-9]|1999", extractedText)     
                Quarter=re.findall("Q[1-4]", extractedText)
                GDPTotal=ExtractString[:ExtractString.find('\n')]
                GDP=re.findall("\-?\d\.\d", GDPTotal)
                ExtractString=ExtractString[ExtractString.find('PCE'):]
                PCETotal=ExtractString[:ExtractString.find('\n')]
                PCE=re.findall("\-?\d\.\d", PCETotal)
                ExtractString=ExtractString[ExtractString.find('CPI'):]
                CPITotal=ExtractString[:ExtractString.find('\n')]
                CPI=re.findall("\-?\d\.\d", CPITotal)
                for i in range(0,len(GDP)):
                    rowtem=[GreenBookTime[0:4],GreenBookTime[5:7],Year[i],Quarter[i],GDP[i],PCE[i],CPI[i]]
                    row.append(rowtem)  
                
                extractedText=extractedText[1:]
                if 'QUARTERLY VALUES' in extractedText:
                    extractedText=extractedText[extractedText.find('QUARTERLY VALUES'):]
                    ExtractString=extractedText[extractedText.find('PRICES AND COSTS'):]
                    if not GreenBookTime in ['2003-09','2003-10','2003-12','2004-01','2004-03','2004-05','2004-06','2004-08','2004-09','2004-11','2004-12','2005-02' ,'2005-03','2005-05','2005-06','2005-08'] :
                        Year=re.findall("20[0,1][0-9]|1999", extractedText)[1:]
                    else:
                        Year=re.findall("20[0,1][0-9]|1999", extractedText)
                    Quater=re.findall("Q[1-4]", extractedText)
                    GDPTotal=ExtractString[:ExtractString.find('\n')]
                    GDP=re.findall("\-?\d\.\d", GDPTotal)
                    ExtractString=ExtractString[ExtractString.find('PCE'):]
                    PCETotal=ExtractString[:ExtractString.find('\n')]
                    PCE=re.findall("\-?\d\.\d", PCETotal)
                    ExtractString=ExtractString[ExtractString.find('CPI'):]
                    CPITotal=ExtractString[:ExtractString.find('\n')]
                    CPI=re.findall("\-?\d\.\d", CPITotal)
                    for i in range(0,len(GDP)):
                        rowtem=[GreenBookTime[0:4],GreenBookTime[5:7],Year[i],Quater[i],GDP[i],PCE[i],CPI[i]]
                        row.append(rowtem) 
            else:
                if GreenBookTime=='2010-08':
                    read2010_2011(47) 
                if GreenBookTime=='2010-09':
                    read2010_2011(39)
                if GreenBookTime=='2010-10':
                    read2010_2011(37)
                if GreenBookTime=='2010-12':
                    read2010_2011(31)
                if GreenBookTime=='2011-01':
                    read2010_2011(26)
                if GreenBookTime=='2011-03':
                    read2010_2011(31)   
                if GreenBookTime=='2011-04':
                    read2010_2011(25)   
                if GreenBookTime=='2011-06':
                    read2010_2011(27)    
                if GreenBookTime=='2011-08':
                    read2010_2011(24)   
                if GreenBookTime=='2011-09':
                    read2010_2011(27) 
                if GreenBookTime=='2011-10':
                    read2010_2011(27)   
                if GreenBookTime=='2011-12':
                    read2010_2011(26) 
                    
                    
        else:
            if not GreenBookTime=='2010-01':
                pdf = PdfFileReader(open(f, 'rb'))
                Page1 = pdf.getPage(16).rotateClockwise(90)
                Page2 = pdf.getPage(39).rotateClockwise(90)    
                output = PdfFileWriter()
                output.addPage(Page1)
                output.addPage(Page2)
                outputStream = open('J:/桌面/RA/GetGreenBook/GS-2010.pdf', "wb")
                output.write(outputStream)
                outputStream.close()
                pdffile=open('J:/桌面/RA/GetGreenBook/GS-2010.pdf','rb')
                outputString=readPDF(pdffile)
                ExtractString=outputString[outputString.find('Changes in Prices and Costs'):]
                Year1=set(re.findall("20[0,1][0-9]", ExtractString))
                Year2=list(Year1)
                Year2.sort()
                Year=[]
                for i in range(0,3):
                    Year.append(Year2[i])
                    Year.append(Year2[i])
                    Year.append(Year2[i])
                    Year.append(Year2[i])
                         
                    
                Extract1String1=ExtractString[ExtractString.find('GDP chain-wt'):ExtractString.find('PCE chain-wt')]
                GDP1=re.findall("\-?[0-9]?\.[0-9]", Extract1String1)[0::2]
                GDP=GDP1[:12]
                
                Extract1String1=ExtractString[ExtractString.find('PCE chain-wt'):]
                GDP1=re.findall("\-?[0-9]?\.[0-9]", Extract1String1)[0::8]
                PCE=GDP1[:12]    
                
                Extract1String1=ExtractString[ExtractString.find('CPI'):]
                GDP1=re.findall("\-?[0-9]?\.[0-9]", Extract1String1)[0::4]
                CPI=GDP1[:12]
                    
                for i in range(0,len(GDP)):
                    rowtem=[GreenBookTime[0:4],GreenBookTime[5:7],Year[i],Quater[i],GDP[i],PCE[i],CPI[i]]
                    row.append(rowtem)
                        
            else:
                pdf = PdfFileReader(open(f, 'rb'))
                Page1 = pdf.getPage(16).rotateClockwise(90)   
                output = PdfFileWriter()
                output.addPage(Page1)
                outputStream = open('J:/桌面/RA/GetGreenBook/GS-2010.pdf', "wb")
                output.write(outputStream)
                outputStream.close()
                pdffile=open('J:/桌面/RA/GetGreenBook/GS-2010.pdf','rb')
                outputString=readPDF(pdffile)
                ExtractString=outputString[outputString.find('Changes in Prices and Costs'):]
                Year1=set(re.findall("20[0,1][0-9]", ExtractString))
                Year2=list(Year1)
                Year2.sort()
                Year=[]
                for i in range(0,3):
                    Year.append(Year2[i])
                    Year.append(Year2[i])
                    Year.append(Year2[i])
                    Year.append(Year2[i])
                         
                    
                Extract1String1=ExtractString[ExtractString.find('GDP chain-wt'):]
                GDP1=re.findall("\-?[0-9]?\.[0-9]", Extract1String1)
                c=[]
                for item in GDP1:
                    c.append(item)
                GDP=[1.9,0,0.4,0.8,1.9,1.1,1.2,1.1,1.2,1.1,1,1]
                PCE=[-1.5,1.4,2.6,2.9,2,1.2,1.3,1.3,1.2,1.1,1.1,1.1,]
                CPI=[-2.4,1.3,3.6,3.4,2.4,1.3,1.5,1.5,1.4,1.3,1.3,1.3]
            
            
                for i in range(0,len(GDP)):
                    rowtem=[GreenBookTime[0:4],GreenBookTime[5:7],Year[i],Quater[i],GDP[i],PCE[i],CPI[i]]
                    row.append(rowtem)


csvfile = open('J:/桌面/RA/GetGreenBook'+'/'+'GreenBookTime666.csv', 'w', newline='')
writer = csv.writer(csvfile)
for item in row:
    writer.writerow(item)

csvfile.close()


