# -*- coding: utf-8 -*-
"""
Created on Sat May 11 11:17:17 2019

@author: Soumya
"""
import re
import pandas as pd

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO

#from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
#from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LTTextBoxHorizontal

document = open("F:\\rohan\\freelancer\\contest.pdf", 'rb')
#Create resource manager
rsrcmgr = PDFResourceManager()
# Set parameters for analysis.
laparams = LAParams()
# Create a PDF page aggregator object.
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)
txt = ""


for pageNumber, page in enumerate(PDFPage.get_pages(document)):
    if pageNumber == 134:
        interpreter.process_page(page)
# receive the LTPage object for the page.
        layout = device.get_result()
        for element in layout:
            if isinstance(element, LTTextBoxHorizontal):
                txt+=element.get_text()

document.close()

'''
filetxt = open("F:\\rohan\\freelancer\\MyFile134.txt",'w')
filetxt.write(txt)
filetxt.close()
'''

p = re.compile("(.*) \| (.*)")
result = p.search(txt)
print(result.group(1))  # column B for odd pgno
print(result.group(2))  # column C for odd pgno

p = re.compile("PAT RIMONIO ADMINIST RADO: (.*)")
result = p.search(txt)
print(result.group(1))

f = open("F:\\rohan\\freelancer\\MyFile135.txt")
lines = f.readlines()
print(lines[12])
f.close()

op = pd.read_excel("F:\\rohan\\freelancer\\Example Output.xlsx")
op