# -*- coding: utf-8 -*-
"""
Created on Wed May  1 19:59:37 2019

@author: Soumya
"""

#import PyPDF2 as pdf

import pdfminer
import re


from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO

#from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
#from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LTTextBoxHorizontal

'''for pageNumber, page in enumerate(PDFDocument.get_pages()):
    if pageNumber == 42:'''

def convert_pdf_to_txt(path, pgno):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
    fstr = ''
    
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    
    for pageNumber, page in enumerate(PDFPage.get_pages(fp)):
        if pageNumber == pgno:
            interpreter.process_page(page)

            # receive the LTPage object for the page.
            layout = device.get_result()
            for element in layout:
                if isinstance(element, LTTextBoxHorizontal):
                    return element.get_text()
            
            '''str = retstr.getvalue()
            fstr += str'''
    
    '''for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages,    password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

        str = retstr.getvalue()
        fstr += str'''

    '''fp.close()
    device.close()
    retstr.close()
    return fstr'''

text = convert_pdf_to_txt("F:\\rohan\\freelancer\\contest.pdf", 43)

p = re.compile("(.*) \| (.*)\n")
result = p.search(text)
print(result.group(1))  # column B for odd pgno
print(result.group(2))  # column C for odd pgno

print(text[0:75])

p = re.compile("\n(.+?)\n")
result = p.search(text)
print(result.group(1))  # # column D for odd pgno

p = re.compile("Inversionistas ")
result = p.search(text)
print(result.group(1))