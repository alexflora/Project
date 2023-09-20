# String methods

"""a="Alexander"
b="Antonysamy"

l=len(a)
print(l)

con=a+b
print(con)

print(a,b.lower())
print(b.upper())

print(a.replace("Alexander","Mary"))

print(a.index("d"))

print(a[7])

print(a.count("e"))

#print(a.center(b))

print(a.encode())

print(a.find("r"))  """


#numbers methods

"""c=5
d=6.3


print(c+d)
print(c*(c*d))
print(str(c))
print(abs(-20))
print(pow(c,d))
print(min(c,d))
print(max(c,d))
print(round(d))"""


#List methods

"""test1=["Alex",3.2,"merivin","Abin","Arul"]
#print(test)
test2=["vimal","gowtham","arocikaraj","aravndth"]

print(test1+test2)

test1.append("livin")
print(test1)

test3=test1.copy()
print(test3)

test3.clear()
print(test3)

print(test1.count("Abin"))

test4=test1.extend(test2)
print(test4)

print(test1.index("Abin"))

print(test1[3])

test2.insert(3,"joy")
print(test2)

print(test2.pop())
s=test2.pop(0)
print(s)

test1.remove(3.2)
print(test1)

#test5=test2.reverse()
#print(test5)

print(test1.sort())
print(len(test1))

"""
#slice concepts

"""list1=[1,2,3,4,5,6,7,8,9,0]
print(list1[0])
print(list1[0:])
print(list1[2:5])
print(list1[:6])"""



#operators

#Assignment

"""a=2
a+=2
print(a)

a-=1
print(a)
a*=2
print(a)
a/=2
print(a)
a%=2
print(a)"""

#Arithmatic

"""a=8
b=2
print(a//b)
print(a**b)"""

#membership

"""testlist=[1,3,5,2,6,9]
if 1 in testlist:
    print("one is there in the list")
if 1 not in testlist:
    print("bnn")"""
    
# list type
normallist=["alex","abin","arul","mervin","rexin"]
print(normallist)
normallist.append("susai")
print(normallist)

tuplelist=("apple","orange",23,"bannana")
print(tuplelist)
# tuple have no methods to update
print(tuplelist.count(23))
print(tuplelist.index("orange"))

dictlist={"key1":"value1","key2":"value2","key3":"value3","age":23}
print(dictlist["age"])
dictlist["dgree"]=["BCA","CS","MS","B.COM","BBA","BE"]

print(dictlist["dgree"][2])

temp={}

for i in dictlist["dgree"]:
    if i in temp:
        temp[i]=temp[i]+1
    else:
        temp[i]=1
        
for i in temp:
    print(i,":",temp[i])



#set
setlist
