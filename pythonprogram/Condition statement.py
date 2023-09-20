a=30
b=45
c=50
d=50
e=100
f=100

# if statement
if b>a:
    print("b is grater then a")

# elseif statement

if a>b:
    print("a is grater then b")

elif b>a:
    print("b is grater then a")

# else statement

if a>b:
    print("a is grater then b")

elif b>c:
    print("b is grater then a")

else:
    print("C is grater ")

# And

if(c>b and e==f):
    print("And condition is satisfied")

# OR
if(a>b or c==d):
    print ("OR condition is satisfied")

# short line if condition

print("B")if b>a else print("A")

# short line elif condition

print("a") if a>b else print("b") if b>a else print("c")
 

