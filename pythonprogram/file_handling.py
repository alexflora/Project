#file creating
"""f_open=open("test.txt","w")"""

#single line writing
"""f_open.write("Hello! world")
f_open.colse()"""
#multi line writing
"""contantlist=["Alexander\n","Viriyur\n","sankarapuram Tk\n","kallakurichi Dt"]
f_open.writelines(contantlist)
f_open.close()"""
#write the multi line by using loop
"""contantlist=["Alexander","Viriyur","sankarapuram Tk","kallakurichi Dt"]
for i in contantlist:
    f_open.write(i+"\n")
f_open.tell()
f_open.close()"""

#-------------------------------------------------------------------------------
#file reading
"""r=open("test.txt","r")"""
"""d=r.read()
print(d)
r.close()"""

#single line reading
"""f=r.readline()
r.close()
print(f)"""

#multi line reading
"""s=r.readlines()
for i in s:
    print(i)
s.close()"""

#-------------------------------------------------------------------------------
#seek and tell
"""a=open("test.txt","r")"""
#tell
"""print(a.tell())
a.readline()
print(a.tell())
a.readline()
print(a.tell())"""
#seek
"""a.seek(10)----#move the courser position from one place to another
print(a.tell())
print(a.read())"""
#-------------------------------------------------------------------------------
#remove file 
"""r=open("hello.txt","w")
r.write("hello world")
r.close()
import os
os.remove("text.txt")"""
#-------------------------------------------------------------------------------
#hands on (28/07/2022)
#fatch the phone number and email id from the file which match the pattern
"""a=open("test.txt","w")
c_list=["Alexander","alexander94255@gmail.com","susai","+918124101766 ","susai@dbc.com","+91684734760108",
        "merivin007@dbc.com","9133344567890","9876543210","+916381549406","djsdla@@gmail..com"]
for i in c_list:
    a.writelines(i+"\n")
    
a.close()

import re
s=open("test.txt","r")
a=s.read()
phone=re.findall("\+91*[6-9]{1}[0-9]{9}\s",a)
for i in phone:
    print(i)
print()
email=re.findall(r'\w+[@]\w+[.]\w{2,3}',a)
for i in email:
    print(i)
print()"""
#-----------------------------------------------------------------------------
#hands on (28/07/2022)
#print the pattern in the file
"""import sys
a=sys.stdout
sys.stdout=open("pattern.txt","w")
d=int(input())
for i in range(d+1):
    print(" "*(d-i),"* "*i)
for j in range(d-1,0,-1):
    print(" "*(d-j),"* "*j)
    
sys.stdout=a
print("hello world")
"""
#without using 'sys' module
"""a=open("pattern.txt","w")
d=int(input("Enter the value: "))
for i in range(d+1):
    a.write(" "*(d-i)+"* "*i+"\n")
for j in range(d-1,0,-1):
    a.write(" "*(d-j)+"* "*j+"\n")
a.close()
s=open("pattern.txt","r")
f=s.read()
print(f)
s.close()"""
#-----------------------------------------------------------------------------
#copy the file and paste it another file

"""firstfile=open("test.txt","r")
s=firstfile.read()
firstfile.close()
d=open("test1.txt","w")
d.write(s)
d.close()"""

#------------------------------------------------------------------------------
# add the content inbetween the file
"""e=open("addcon.txt","w")
e.write("i have done my degree in don bosco college at athanavur")
e.flush()
e.write("hello world")
print(e.isatty())"""







