import os
"""d=xlrd.open_workbook('‪C:\python program\file\linkfile (1).xls')
print(d[0])"""


#Getting the Current working directory
"""d=os.getcwd()
print(d)""" 

#change directry

"""def current_path(): 
    print("Current working directory before") 
    print(os.getcwd()) 
    print() 
    
    
# Driver's code 
# Printing CWD before 
current_path() 
    
# Changing the CWD 
os.chdir('C:\python program\file\linkfile (1).xls') 
    
# Printing CWD after 
current_path()"""

#read file
"""
path=r"C:\python program\addcon.txt"
fd=os.open(path, os.O_RDONLY)
n=50
x=os.read(fd,n)
print(x)
os.close(fd)"""

import pandas as pd
import xlrd

#read xl file with xls formate
a=pd.read_excel(r'C:\python program\file\linkfile (1).xls')

#read excel file line by line     
loc = (r'C:\python program\file\linkfile (1).xls')         
wb = xlrd.open_workbook(loc)     
sheet = wb.sheet_by_index(0)
p=sheet.cell_value(1, 1)
firstsp=os.path.split(p)
secondsp=os.path.split(firstsp[0])
thirdsp=os.path.split(secondsp[0])
print(fs[1])
print(ss[1])
print(ts[1])


#read PDF file
"""x=next(os.walk(r'C:\python program\file\Pdffile'))[2]
print(x)"""










