#single inheritance
"""class parent:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def display(self):
        print("A value:",self.a)
        print("B value:",self.b)
class child(parent):
    def __init__(self,a,b):
        parent.__init__(self,a,b)
    def add(self):
        return(self.a+self.b)
    def show(self):
        self.display()
obj=child(5,6)
d=obj.add()
obj.show()
print(d)"""

#override the init function in the child class
"""class getvalue:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print(self.a+self.b)
class solution(getvalue):
    def __init__(self,a,b):
        getvalue.__init__(self,a,b)
    def sub(self):
        return(self.a-self.b)
obj=solution(4,5)
obj.sub()
obj.add()"""


#single inheritence with overriding (27/07/2022)
"""class base:
    def __init__(self,Name,age,percent,grade):
        self.Name=Name
        self.Age=age
        self.percent=percent
        self.grade=grade
    def display(self):
        print("Name of the student:%s"%self.Name)
        print("Age:%s"%self.Age)
        print("percentage:%s"%self.percent)
        print("grade :%s"%self.grade)
        
class drive(base):
    def __init__(self,collagename,dept,percent):
        name = input("Enter the name :")
        age=input("Enter Age :")
        percent=input("Enter the percent :")
        grade=input("Enter the grade :")
        base.__init__(self,name,age,percent,grade)
        
        self.collage=collagename
        self.dept=dept
        self.percent=percent
        
    def display(self):
        super().display()
        print("collage name:%s"%self.collage)
        print("department:%s"%self.dept)
        print("percent:%s"%self.percent)
       
a=input("Enter the Collage name :")
b=input("Enter the department : ")
c=input("Enter the percent : ")
obj2=drive(a,b,c)
obj2.display()"""

#multi level inheritance
"""
class studentinfo:
    def __init__(self,name,age,gender):
        self.Name=name
        self.Age=age
        self.Gender=gender
    def display1(self):
        print("Student name is",self.Name)
        print("Student Age",self.Age)
        print("Student gender",self.Gender)
        
class studentmark(studentinfo):
    def __init__(self,name,age,gender,m1,m2,m3,m4,m5):
        super().__init__(name,age,gender)
        self.M1=m1
        self.M2=m2
        self.M3=m3
        self.M4=m4
        self.M5=m5
    def display2(self):
        super().display1()
        print("Tamil:",self.M1)
        print("English:",self.M2)
        print("Maths:",self.M3)
        print("C#:",self.M4)
        print("C:",self.M5)
        
class findavg(studentmark):
    def find(self):
        Avg=(self.M1+self.M2+self.M3+self.M4+self.M5)/5
        return Avg
    def display(self):
        super().display2()
        
    
Name=input("Enter the name: ")
Age=int(input("Enter the age: "))
Gender=input("Enter the Gender: ")
m1=int(input("Tamil : "))
m2=int(input("English: "))
m3=int(input("Maths: "))
m4=int(input("c# : "))
m5=int(input("C : "))

d=findavg(Name,Age,Gender,m1,m2,m3,m4,m5)
a=d.find()
d.display()
print("Avarage of the student marks:",a)"""

        
        
    
