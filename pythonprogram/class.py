"""class student:
    def __init__(sam,name,age):
        sam.name=name
        sam.age=age

    def print_data(sam):
        #print(sam)
        print("Name:",sam.name,"\nAge:",sam.age)
stu1=student("A",20)
stu2=student("B",45)

stu1.print_data()
stu2.print_data()
print(stu1)"""


#find givin number is odd or even

"""class Odd_Even:
    def __init__(self,value):
        self.number=value
    def find_oddeven(self):
        if self.number%2==0:
            print("given number is Even")
        else:
            print("given number is Odd")
v=int(input("Enter the value: "))
sample=Odd_Even(v)
sample.find_oddeven()"""


#find the factorial

"""class fact:
    def __init__(self,num):
        self.value=num

    def cal(self):
        fact=1
        for i in range(1,self.value+1):
            fact=fact*i
            i+=1
        return fact

f=int(input("Enter the number: "))
ff=fact(f)
factorial=ff.cal()
print(factorial)"""
