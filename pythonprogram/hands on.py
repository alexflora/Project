#count the value in dict
"""testdict={"car1":"audi","car2":"BMW","car3":"toyato","car4":"gipci"}
testdict['newlyadded']=[1,2,3,2,4,1,5,6,9,7]
temp={}
print(testdict)
for i in testdict['newlyadded']:
    if(i in temp):
        temp[i]=temp[i]+1

    else:
        temp[i]=1
for i in temp:
    print(i,":",temp[i])
#-----------------------------------------------------------------------------

#factorial (while)

n=5
fact=1
i=1

while i<=n:
    fact=fact*i
    i+=1

print(fact)


# factorial(for)
a=int(input("Enter the value"))
sum=1

if a<0:
    print("could not find the factorial")
elif a==0:
    print("factorial of \"0\"is one or zero")
else:
    for i in range(1,a+1):
        sum=sum*i

    print("factorial of",a,":",sum)

#factorial (function)
    
def factorial(b):
    if b==1:
        return 1
    
    else:
        return (b*factorial(b-1))

    
q=int(input("Enter which value you want to find out the factorial:"))
value = factorial(q)
print(value)


#check the number is +ve or -ve

a=int(input("Enter the value:"))
if a>0:
    print("Given number is +ve")
elif a==0:
    print("Given number is \"0\"")
else:
    print("Given number is -ve")

#---------------------------------------------------------------------------
#Arguments

#1.positional
def position (a,b):
    print(a)
    print("\n")
    print(b)

position("Alex",90)

def position1 (c,d):
    return c,d
s,r=position1(10,20)
print(s,r)

#2.default

def default(e,f="Apple"):
    print("one kg of",f,"Amount is",e)
default(100)

def default1(w,i,o,p="PIN:606402"):
    return w,i,o,p
t,y,u,q=default1("2/146","College street","viriyur")
print(t,y,u,q)

#3.keyword

def keyword(name,age,gender):
    print("",name,"\n",age,"\n",gender)
keyword(name="alex",gender="male",age=20)

#4.variable length argument

def varlenght(*n):
    print(n)
varlenght(1,2,3,"hello",5,6,7,8,9,"world")

#5.variable lenght keyword argument

def varkeylen(**a):
    for k,v in a.items():
        print(k,"=",v)
        
varkeylen(name1="apple",name2="bannana",name3="cat",name4="deer")"""
#------------------------------------------------------------------------------
#get the collection of input from the user
"""collection =[]
while True:
    singleVal=input("Enter the value: ")
    if singleVal:
        collection.append(singleVal)
    else:
        break
print(collection)
new='\n'.join(collection)
print(new)

"""
#-------------------------------------------------------------------------------
"""#1.lambda function:
 we need not give any name for the identification(function name) 

a=int(input("Enter Number"))
l=lambda n:n*n
print(l(a))


#2.filter function:

def find(d):
    if int(d)%2==0:
        return True
    else:
        return False
    
value=input()
list1=value.split()
Filter=list(filter(find,list1))
print("By using normal function:",Filter)


Filter1=list(filter(lambda a:int(a)%2==0,list1))
print("By using lambda:",Filter1)


#3.Map function:

coll=[]
while True:
    singleV=input()
    if singleV:
        coll.append(singleV)
    else:
        break
new=",".join(coll)

def map1(new):
    return  int(new)*int(new)

Map=list(map(map1,coll))
print(Map)"""

#4.Reduce function:

"""from functools import *

r=reduce(lambda a,b:a+b,range(1,10))
print(r)"""

#pattern
"""rows=int(input("enter your number"))
for i in range(0,rows):
        print("*" * i)
for j in range(rows,0,-1):
    print("*" * j)"""
# odd postition print
"""n=int(input("Enter the value: "))
if n%2==0:
    n=n-1
else:
    n=n
for i in range(0,n):
    if i%2!=0:
        #print(" "*(n-1),end="")
        print("* "*i,i)
for j in range(n,0,-1):
    if j%2!=0:
        #print(" "*(n-1),end="")
        print("* "*j,j)"""
# star pattern
"""for i in range(9):
    for j in range(13):
        if i==2 or i==6 or i+j==6 or j-i==6 or i-j==2 or i+j==14:
            print("*",end="")
        else:
            print(" ",end="")
    print()"""

#right side pattern print
"""n=int(input("Enter the value"))
for i in range (n+1):
    print(" *"*i)
for j in range(n-1,0,-1):
    print(" *"*j)"""

#left side pattern print

"""n=int(input("Enter the value: "))
for i in range(n+1):
    print(" "*(n-i),"*"*i)
for j in range(n-1,0,-1):
    print(" "*(n-j),"*"*j)"""
       
#diamond pattern
"""n=int(input("Enter the value: "))
for i in range(n+1):
    print(" "*(n-i),"* "*i)
for j in range(n-1,0,-1):
    print(" "*(n-j),"* "*j)"""

#heart pattern
"""for row in range(6):
    for col in range(7):
        if (row==0 and col%3!=0)or(row==1 and col%3==0)or(row-col==2)or(row+col==8):
            print("*",end="")
        else:
            print(end=" ")
    print()"""

#---------------------------------------------------------------------------------
# Number printing(exam question)
"""
a=int(input("Enter the value: "))
if a>20:
    print("Give the value within 20")
else:
    for i in range(a,0,-1):
        for j in range(a,a-i,-1):
            print(j,end=" ")
        print()"""
#exam question- get the value and print the value like dictionary
"""class arithmatic:
    def __init__(self,a,b):
        self.A=a
        self.B=b
    def find(self):
        d={"sum":self.A+self.B,"difference":self.A-self.B,"product":self.A*self.B,"division":{"q":self.A/self.B,"r":self.A%self.B}}
        return d
obj=arithmatic(6,5)
a=obj.find()
print(a)"""

#regular expresion
#-------------------------------------------------------------------------------

        
#-------------------------------------------------------------------------------
#hands on (23/07/2022)

"""h=eval(input("Enter the value:"))
#print("-")
for x in range(h):
    sp=4*(h-(x+1))
    sp=int(sp/2 if sp else sp)
    print(" "*sp,"*"*(x+x+x+x+1))
for y in range(h,-1,-1):
    sp=4*(h-(y+1))
    sp=int(sp/2 if sp else sp)
    print(" "*sp,"*"*(y+y+y+y+1))"""
#----------------------------------------------------------------------------
#hands on (25/07/2022)
# get the list of value and add it ,display ,avarage
"""class Mark:
    def __init__(self,m1,m2,m3):
        self.M1=m1
        self.M2=m2
        self.M3=m3
    def addMarks(ob1,ob2):
        total=Mark(0,0,0)
        total.a=ob1.M1+ob2.M1
        total.b=ob1.M2+ob2.M2
        total.c=ob1.M3+ob2.M3
        return(total)
    def displayTotalMarks(self):
        print("Mark1 :%s"%self.a)
        print("Mark2 :%s"%self.b)
        print("Mark3 :%s"%self.c)
    def displayAverage(self):
        print("Avg1:%s"%str(self.a/2))
        print("Avg2:%s"%str(self.b/2))
        print("Avg3:%s"%str(self.c/2))
        
Mark1=Mark(50,60,70)
Mark2=Mark(80,90,100)
Total=Mark.addMarks(Mark1,Mark2)
Total.displayTotalMarks()
Total.displayAverage()"""

#get marks from the user and find the total,avg
"""class Mark:
    def __init__(self,m1,m2,m3,m4,m5):
        self.M1=m1
        self.M2=m2
        self.M3=m3
        self.M4=m4
        self.M5=m5
    def addMarks(ob1,ob2,ob3,ob4,ob5):
        total=Mark(0,0,0,0,0)
        total.a=ob1.M1+ob2.M1+ob3.M1+ob4.M1+ob5.M1
        total.b=ob1.M2+ob2.M2+ob3.M2+ob4.M2+ob5.M2
        total.c=ob1.M3+ob2.M3+ob3.M3+ob4.M3+ob5.M3
        total.d=ob1.M4+ob2.M4+ob3.M4+ob4.M4+ob5.M4
        total.e=ob1.M5+ob2.M5+ob3.M5+ob4.M5+ob5.M5
        return(total)
    def displayTotalMarks(self):
        print("Mark1 :%s"%self.a)
        print("Mark2 :%s"%self.b)
        print("Mark3 :%s"%self.c)
        print("Mark4 :%s"%self.d)
        print("Mark5 :%s"%self.e)
    def displayAverage(self):
        print("Avg1:",self.a/5)
        print("Avg2:%s"%str(self.b/5))
        print("Avg3:%s"%str(self.c/5))
        print("Avg4:%s"%str(self.d/5))
        print("Avg5:%s"%str(self.e/5))
        
Mark1=Mark(50,60,70,45,24)
Mark2=Mark(80,90,100,23,56)
Mark3=Mark(35,23,45,78,56)
Mark4=Mark(56,78,89,56,34)
Mark5=Mark(34,45,67,87,98)
Total=Mark.addMarks(Mark1,Mark2,Mark3,Mark4,Mark5)
Total.displayTotalMarks()
Total.displayAverage()"""
#-----------------------------------------------------------------------------
#count the word from the string

"""str="Alex is good boy is good"
for i in str.split():
    print(i,":",str.count(i))"""

"""sam="That's the password password 123 cried the Special Agent.So I fled"
temp={}
for i in sam.split():
    if i in temp:
        temp[i]=temp[i]+1

    else:
        temp[i]=1
for i in temp:
    print(i,":",temp[i])"""

#------------------------------------------------------------------------------
# try catch
# hands on (27/07/2022)
"""num1=4
num1=d
try:
    num1=int(input("Enter the value1 :"))
    num2=int(input("Enter the value2 :"))
    print("Hi")
    print(num1+num2)
except:
    print("Enter the valid value")
finally:
    print("corrcted")
"""
        
#-------------------------------------------------------------------------------
#create Database and create the table and insert the data into the table
"""import psycopg2
con=psycopg2.connect(database="sample",user="postgres",password="postgres",host="localhost",port="5432")
#print("success")
cur=con.cursor()

Itemname=input("Enter the Itemname: ")
Total_quantity =int(input("Enter the Total_quantity: "))
sales=int(input("Enter the sales: "))
inhand=Total_quantity-sales


cur.execute("create table if not exists grocery (Itemname varchar(255),Total_quantity int,sales int,inhand int)")
con.commit()
cur.execute("select *from grocery")
a=cur.fetchall()
print(a)
cur.execute("insert into grocery(Itemname,Total_quantity,sales,inhand)values(Itemname,Total_quantity,sales,inhand)")
con.commit()
cur.execute("select *from grocery")
a=cur.featchall()
print(a)    -----------Not working
cur.colse()
con.colse()"""

#----------------------------------------------------------------------------
#dict key value accses
#condition
"""a=int(input("Enter the value"))
b={True:1,False:0}
print(b[True]) if a%2==1 else print(b[False])  
print(b[a%2==1])
"""
#-------------------------------------------------------------------------------------------
#task (date-24/08/2022)
#source 
"""data = [
    {'department': 'Commerce', 'hostel_data': (0, 0, 0, 32, 0, 36), 'total_count': 68},
    {'department': 'Computer Applications', 'hostel_data': (0, 0, 0, 83, 11, 43), 'total_count': 137},
    {'department': 'Computer Science', 'hostel_data': (0, 0, 0, 26, 7, 23), 'total_count': 56},
    {'department': 'Defense and Strategic Studies', 'hostel_data': (0, 0, 0, 0, 0, 0), 'total_count': 0},
    {'department': 'English', 'hostel_data': (0, 0, 0, 7, 2, 22), 'total_count': 31},
    {'department': 'Management Studies', 'hostel_data': (0, 0, 0, 16, 6, 14), 'total_count': 36},
    {'department': 'Mathematics', 'hostel_data': (0, 0, 0, 2, 3, 4), 'total_count': 9}
]

output
{'hostel_ 1': 0,
'hostel_ 2': 0,
'hostel_ 3': 0,
'hostel_ 4': 166,
'hostel_ 5': 29,
'hostel_ 6': 142
}
"""
data = [
    {'department': 'Commerce', 'hostel_data': (0, 0, 0, 32, 0, 36), 'total_count': 68},
    {'department': 'Computer Applications', 'hostel_data': (0, 0, 0, 83, 11, 43), 'total_count': 137},
    {'department': 'Computer Science', 'hostel_data': (0, 0, 0, 26, 7, 23), 'total_count': 56},
    {'department': 'Defense and Strategic Studies', 'hostel_data': (0, 0, 0, 0, 0, 0), 'total_count': 0},
    {'department': 'English', 'hostel_data': (0, 0, 0, 7, 2, 22), 'total_count': 31},
    {'department': 'Management Studies', 'hostel_data': (0, 0, 0, 16, 6, 14), 'total_count': 36},
    {'department': 'Mathematics', 'hostel_data': (0, 0, 0, 2, 3, 4), 'total_count': 9}
]
"""a={}
for i in range(len(data)):
    a[i]=(data[i]['hostel_data'])
print(a)
for i in range(6):
    print(a[0][i]+a[1][i]+a[2][i]+a[3][i]+a[4][i]+a[5][i]+a[6][i])"""
    
"""a=[i['hostel_data'] for i in data]
print(a)
res=[sum(i) for i in zip(*a)]
name=['hostel_1','hostel_2','hostel_3','hostel_4','hostel_5','hostel_6','hostel_7']
final=[{name:res} for name,res in zip(name,res)]

print(final)"""

#correct method
"""a={}
for  i in data:
    k=1
    for j in i['hostel_data']:
        if ('hostel_ %s'%k) in a:
            a['hostel_ %s'%k]=a['hostel_ %s'%k]+j
        else:
            a['hostel_ %s'%k]=j
        k+=1
print(a)"""

#-----------------------------------------------------------------------------
#hands on (multiply two number without using(*) operator)05/09/2022

"""def multiply(x, y):
    if y < 0:
        return -multiply(x, -y)
    elif y== 0:
        return 0
    elif y == 1:
        return x
    else:
        return x + multiply(x, y - 1)
        
a=int(input("enter the first value"))
b=int(input("enter the second value"))

print(multiply(a,b))

def mul(x,y):
    c=0
    for i in range(1,b+1):
         c=c+a
    return(c)
a=int(input("enter the first value"))
b=int(input("enter the second value"))
z=mul(a,b)
print(z)


a=int(input("enter the first value"))
b=int(input("enter the second value"))
c=(a)/(1/b)
print(c)"""


#------------------------------------------------------------------------------

"""from datetime import date, timedelta
import calendar

def numberOfDays(y, m):
      leap = 0
      if y% 4 == 0:
         leap = 1
      if m==2:
         return 28 + leap
      list = [1,3,5,7,8,10,12]
      if m in list:
         return 31
      return 30

def cal(Today):
      days_in_month = calendar.monthrange(Today.year, Today.month)[1]
      Today=Today + timedelta(days=days_in_month)
      return Today

#---unwantad----
elif y%400 ==0:
            leap=1
      elif y%100 ==0:
            leap=0

y=Today.year;
M=Today.strftime("%b");
D=Today.day;
total_days=numberOfDays(y,M);

todays_date = datetime.date.today()
print("Original Date:", todays_date)
EndDate=Today.replace(day=23,month=2,year=2023)


n=calendar.monthrange(year,M)
print(n) ans(3,31)
#-------end------

Today =date(2020,2,2);
end =date(2022,3,2);
temp=[]
if(end>Today):
      date=Today
      #find year
      year=Today.year
      
      # find name of month
      month=Today.strftime("%b")
      
      #replace day as 1
      #change formate
      s=Today.replace(day=1)
      start=s.strftime("%d-%m-%Y")
      
      
      #count the number of days in a month
      M=Today.month
      num=numberOfDays(year,M)
      
      e=Today.replace(day=num)
      End=e.strftime("%d-%m-%Y")
      
      value={"year":year,'month':month,'Startdate':start ,'EndDate':End,'days':num}
      temp.append(value);

      Today=cal(date)
      print(Today)


      

# Correct way of find out the value

from datetime import datetime,date, timedelta
from dateutil.relativedelta import relativedelta

def numberOfDays(y, m):
      leap = 0
      if y% 4 == 0:
         leap = 1
      if m==2:
         return 28 + leap
      list = [1,3,5,7,8,10,12]
      if m in list:
         return 31
      return 30

#s= str(input("Enter the start date:"))
#e=str(input("Enter the end date:"))
#startDate=datetime.strptime(s,"%m/%d/%y")
#endDate=datetime.strptime(e,"%m/%d/%y")
startDate=date(2022,12,12)
endDate=date(2023,3,2)
addDays = timedelta(days=31)
#print(addDays)

if (startDate>endDate):
    print("Give the Start date leass then the End date")

x = []
while startDate <= endDate:
    #v=startDate+relativedelta(day=31)
    #x.append({'Year':startDate.year,'Month':datetime.strftime(startDate,"%B"),'Start_date':str(startDate.replace(day=1)),'End_date':str(v)})
    total_days= numberOfDays(startDate.year,startDate.month)
    x.append({'Year':startDate.year,'Month':datetime.strftime(startDate,"%B"),'Start_date':str(startDate.replace(day=1)),'End_date':str(startDate.replace(day=total_days)),'TotalDays':total_days})
    startDate =startDate + addDays

for y in x:
      print(y)"""

#-------------------------------------------------------------------------------
#10/09/2022 hand on for find today as birthday and show msg 

"""import datetime

#dob=datetime.date(2022,9,11)
dob=datetime.datetime.strptime("10/09/2022 8:10","%m/%d/%Y %H:%M")
if(dob.day & dob.month == datetime.date.today().day & datetime.date.today().month):
      print(" Today is your brithday")

else:
      print("Today not your birthday")"""

#--------------------------------------------------------------------------------
#12/09/2022 concatenate three dicit value by using (**)unpack oprater

"""a={1:'hello',2:'world'}
b={'one':'apple','two':'bnanana'}
c={'key':'value1','key':'value2'}
#d={'dic1':a,'dic2':b,'dic3':c}
d={**a,**b,**c}
print(d)"""
#https://favtutor.com/blogs/merge-dictionaries-python


#Pair sum (10/09/23)

def pairsum(arr,t):
    count=0
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[i]+arr[j]==t):
                count +=1
            
    return count
arr=[2,4,3,1,3]
t=6
result=pairsum(arr,t)
print(result)





      










    








        
