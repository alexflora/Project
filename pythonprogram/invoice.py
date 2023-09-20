import pdfplumber
import re


def sample(pdf):
    fromemail=''
    bankcode=''
    pdf = pdfplumber.open(pdf)
    for pages in pdf.pages:
        for line in pages.extract_text().splitlines():
            if 'admin@slicedinvoices.com' in line.lower():
                fromemail=line.split()[-1]
            if 'acc' in line.lower():
                bankcode=line.split()[-2]
            if 'invoice number' in line.lower():
                #print(line.split()[-1])
                pass
    

sample("C:\pythonprogram\invoice1.pdf")

data = {}
with pdfplumber.open("C:\pythonprogram\CsResult.pdf")as pdf:
    for pages in pdf.pages:
        for line in pages.extract_text().splitlines():
            print(line)
            lines = line.split('\n')
            for line in lines:
                pass
        

    #table = pdf.pages[0].extract_tables()
    #delimiter = '|'
    #column_headings = [str(cell) for cell in table]
    #column_headings = '|'.join(column_headings).split(delimiter)
    #for i in column_headings:
     #   print(i)
