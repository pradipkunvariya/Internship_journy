# Generated from: Internship learning.ipynb
# Converted at: 2026-04-20T10:17:13.007Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# # Data Types in Python
# 
# ### -> String 
# 
# ### -> Number Data Types
# 
# ### -> Boolean
# 
# ### -> List
# 
# ### -> Tuple
# 
# ### -> Set 
# 
# ### -> Dictionary
# 
# ### -> Frozenset


# ## 1. String
# 
# ### -> Any text\character represented in single\double quotations(''\"") is called as string.
# 
# ### -> Eg: "hello",'12'.


#pre-defined input
a= "Hello WOrld"
print(a)

print(type(a))

# user defined 
a1 = str(input("enter your text"))
print(a1)
print(type(a1))


# ## 2.Number Datatypes
# 
# ### -> int: All the values will be accepted (+ve,-ve,0) but will not deal with decimal values 
# ###        Eg: -99,+1,5,0
# 
# ### -> float: All the values will be accepted (+ve,-ve,0) and also will deal with decimal values
# ###        Eg: 3-> 3.0,3.2,3.5
# 
# ### -> complex : Consideration of real and imaginary number. These values are also known as arbitary values 
# ###             Eg: 5j+6j+9,8+6j
#             
# 


# ## int


#pre defined input 

i = 5
print(i)
print(type(i))

i = 2
i1 = 5
print(i+i1)
print(i-i1)
print(i*i1)
print(i/i1)
print(i//i1)

#User defined 

i2 = int(input("enter 1st value"))
i3 = int(input("enter 2nd value"))
print(i2+i3*i2/i)
print(i2-i3)
print(i2/i3)

# ## Float


f = 4.5
print(f)
print(type(f))

f1 = float(input("enter your choice"))
print(f1)
print(type(f1))

# ## Complex


 #Predefined 

c = 5+9j+9j+6-5
print(c)
print(type(c))

print(c.real)

print(c.imag)

c1 = complex(input("enter fisrt value"))
c2 = complex(input("enter second value"))
print(c1-c2)

print(c1.real,c1.imag)
print(c2.real,c2.imag)

# ## Boolean


# ### ->It willl support binary  outcomes .(True|False)
# ### ->In python True will be treated as 1,False will be treated as 0.
# ### ->It will support the operators.


t = True
print(t)
print(type(t))

f = False
print(f)
print(type(f))

True+False

True+19

False-True

#user input

b = bool(input("enter the first value"))
print(b)

# ##  List
# 
# ### -> collection of iteams repesented in square parantheses
# 
# ### -> List will allow duplications.
# 
# ### -> List will allow additions.
# 
# ### -> List will allow replacements.
# 
# ### -> This makes list mutable(changeable) in nature


l = ['hello',12,5.3,True,5+6j,True]
print(l)
print(type(l))

l.append(9)
l.append(4)

l

# #### for replacement we have to understand the indexing


l[1] = 5

l

#User input 

l1 = list(input("enetr the values").split(" "))
print(l1)
l1.append(8)
l1[4] = 3
print(l1)
print(type(l1))

# # Assignment 1
# 


#user defined

p = int(input("enter the first value"))
r = float(input("enter second value"))
d = complex(input("enter the third value"))
print(p+r+d)
print(p-r-d)
print(p*r*d)
print(p/r/d)
print(p+r*d-p/r-r*p)

# # Tuple


# ### ->collection of iteams represented in circular brackets'()'.
# ### ->Tuple allows duplications of values.
# ### ->Tuple will not allow any addition.
# ### ->Tuple does not support iteam assignment.
# ### ->This makes tuple immutable (which annot be changed)in nature.


t = ('apple',True,12,21,32,65,98,75)
print(t)
print(type(t))

##User input 

t1 = tuple(input("enter your choie").split(","))
print(t1)
print(type(t1))

# ## Rules to do a coding in python programming 
# 
# ### user cannot assign a keyword or a number as a varible.
# 
# ### One can choose any characater as a variable but not allowed to select python's built-in words or any numeric value.


# # Set


# ### -> set is a series of elements stored in {} braces
# ### -> set will not allow duplicate value 
# ### -> Set allows addition and deletion
# ### -> set allows multiple computation (union,subset,etc)


s = {1,2,3,4,5}
print(s)
print(type(s))

s.add(8)

s

s.remove(8)

s

# ### Union : combination of two given sets and will give union values 
# ### from those two sets


s1 = {1,2,3,4,5}
s2 = {4,5,6}
print(s1.union(s2))
print(s1 | s2)

# ### Intersection -> It prints same elements from given two sets


s3 = {1,2,3,4,5}
s4 = {2,3,4,5,6}
print(s3 & s4)


# ## Subset -> All elements of main\parent set are present in child set 


s5 = {2,3,4,5,6}
s6 = {1,2,3,4,5,6,7,8,9}
print(s5.issubset(s6))

# ## Super set is known to be as a set having elements 
# ### which are present in subset


s5 = {2,3,4,5,6}
s6 = {1,2,3,4,5,6,7,8,9}
print(s6.issuperset(s5))

# #### Difference wrt elements which are unique in s7(not present s8 )


s7 = {3,4,5,6,7,8,9}
s8 = {1,2,3,4,5,6}
print(s7-s8)

print(s7^s8)

# ## Dictionary


# ### -> Dictionary is defined to have key-value pairs diplayed in {} brackets
# ### -> Dictionary will not allowed duplicate values 


d = {'Name':'Pradip Kunvariya','Age': 21,'Course' : 'Data Science', 'Fees':23000 }
print(d)
print(type(d))

# # Frozenset


# ## It will not allow any addition/removal of elements.


fs = frozenset([1,2,3,4])

fs


print(type(fs))

## user defined 

f2 = frozenset(input("enter the choices"))
print(type(f2))

# # Assignment 2
# ### frozenset and set operations


s = {1,2,3,4}
s1 = {3,4,5,6}

# Union
print(s.union(s1))
print(s|s1)

# Intersection
print(s.intersection(s1))
print(s&s1)

# subset
s3 = {3,4}
s4 = {1,2,3,4}
print(s3.issubset(s4))

# Superset
print(s3.issuperset(s4))

# Difference 
print(s3-s4)
print(s4-s3)

# Relative difference
print(s3^s4)

a = (45.3,)
print(type(a))

s5 = set(input("Enter the elements").split(","))
s6 = set(input("enter the elements").split(","))
print(s5 | s6)
print(s5 & s6)
print(s5 - s6)
print(s6 - s5)
print(s5^s6)
print(s5.issubset(s6))
print(s6.issuperset(s5))

s5.add(12)

s5

### consideration of arbitary value:

combination of real and imaginary values.
2+3j+5+8j+9

c = 2+3j+5+8j+9

c

c.real

c.imag

a = 8
b = 5
print(a/b)#->float division
print(a//b)#-> int division

s1 = {}
print(type(s1))

s1 = set()
print(type(s1))

d

d['attendance'] = 'present'


d

d.pop('Age')

d

s = {}
print(type(s))

a = (True,)
print(type(a))

# ## Type casting
# 
# ### -> When user converts one data type into another data type is defined as the method of type casting/type conversion.
# 
# ### ->int->float,float->int


t= ('a',1)
l = list(t)

l

l.append(3)

l

l1 = l
t1 = tuple(l1)

t1

# # Type casting of int
# 
# ## float -> int


f = 4.2556556
i = int(f)
print(i)

f1 = float(input("enter the element"))
i1 = int(f1)
print(i1)

# # str -> Int 


sr = "26"
i3 = int(sr)
print(i3)
print(type(i3))

sr1 = str(input("Enter the element"))
i2 = int(sr1)
print(i2)
print(type(i2))

# ## list -> int


l = [1,2,3]
l1 = l[1]

l1

i4 = int(l1)
i4

print(type(i4))

# ## bool-> int


b = True
i5 = int(b)

i5

# ## Tuple -> int


t = (4,5)
t1 = t[1]
i5 = int(t1)
print(i5)
print(type(i5))

# ## set -> int


st = {1,2,3}
l2 = list(st)

l2

l3 = l2[2]

i6 = int(l3)
print(i6)
print(type(i6))

# ## complex -> int


c = 5+6j+9
i7 = int(c.real)
i8 = int(c.imag)
print(type(i7),i8)

# ## list -> int


l3 = list(input("enter the values").split(","))
l4 = l3[-2]
print(l4)
i9 = int(l4)
print(i9)
print(type(i9))

s4 = set(input("enter the elements").split(","))
print(s4)
l5 = list(s4)
l6 = l5[3]
i10 = int(l6)
print(i10)
print(type(i10))

# ## boolean -> float


b = True
f1 = float(b)
print(type(f1))
f1

b1 = False
f2 = float(b1)
print(f2)
print(type(f2))

# # Type asting of string
# 
# ## int ->string


i12 = 12
sr2 = str(i12)
print(sr2)
print(type(sr2))

# ## float -> string


f13 = 53.656
sr3 = str(f13)
print(sr3)
print(type(sr3))

# ## complex -> string


c1 = 12+6j+9j
sr4 = str(c1)
print(sr4)
print(type(sr4))

# ## list -> string


l7 = ['Pradip',21,23.5]
sr5 = str(l7)
print(sr5)
print(type(sr5))

# ## tuple -> string


t2 = ('Pradip',12,65.6)
sr6 = str(t2)
print(sr6)
print(type(sr6))

# ## set-> string


s2 = {1,2,5,6,8,7}
sr7 = str(s2)
print(sr7)
print(type(sr7))

# ## dictionary -> string


d1 = {'Name':'Pradip','Age':21}
sr8 = str(d1)
print(sr8)
print(type(sr8))

# # Type casting of list
# 
# ## int -> list


i13 = 23
l8 = [i13]
print(l8)

i13

# User input
i14 = int(input("enter the element"))
l9 = [i14]
print(l9)
print(type(l9))

# ## float -> list


f14 = 23.5
l10 = [f14]
print(l10)
print(type(l10))

# ## complex -> list


c2 = 12+6j+9j+32
l11 = [c2]
print(l11)
print(type(l11))

# ## boolean -> list 


b3 = False
l12 = [b3]
print(l12)
print(type(l12))

# ## set -> list


s3 = {1,2,3,4,5,6,7,8,9}
l13 = [s3]
print(l13)
print(type(l13))

# ## dictionary -> list


d2 = {'Name':'Pradip','Age':21}
l14 = list(d2.items())
print(l14)
print(type(l14))

# ## tuple -> list


t3 = (1,'Pradip',23.3)
l15 = [t3]
print(l15)
print(type(l15))

# # Type casting of float


# ## string -> float


sr65 = "23"
f65 = float(sr65)
print(f65)
print(type(f65))

# #### user input type casting


sr56 = str(input("enter the elements"))
f56 = float (sr56)
print(f56)
print(type(f56))

# ## int -> float


i14 = 65
f15 = float(i14)
print(f15)
print(type(f15))


# #### user input typecasting


i15 = int(input("enter the number"))
f16 = float(i15)
print(f16)
print(type(f16))

# ## boolean -> float


b6 = True 
f17 = float(b6)
print(f17)
print(type(f17))

# #### user input typecasting


b7 = bool(input("enter the element"))
f18 = float(b7)
print(f18)
print(type(f18))

# # set -> float


s4 = {5,3,6,8,4,5,1}
f19 = float(list(s4)[1])
print(f19)
print(type(f19))


# #### user input typecasting 


s5 = set(input("enter the elements").split(","))
f20 = float(list(s5)[3])
print(f20)
print(type(f20))


# ## list -> float


l16 = [12,'Pradip',45.3,True]
f21 = float(l16[3])
print(f21)
print(type(f21))

# #### User input typecasting


l17 = list(input("Enter the elements").split(","))
f22 = float(list(l17)[0])
print(f22)
print(type(f22))

# # Type casting of Set


# ## int -> set


i15 = 65
s5 = set([i15])
print(s5)
print(type(s5))

# #### user input type casting


i16 = int(input("enter the elements"))
s6 = set([i16])
print(s6)
print(type(s6))

# ## float -> set


f23 = 23.6
s7 = set([f23])
print(s7)
print(type(s7))

# #### user input typecasting


f24 = float(input("enter the elements"))
s8 = set([f24])
print(s8)
print(type(s8))

# ## complex to set


c3 = 65+9j
s9 = set([c3])
print(s9)
print(type(s9))

# #### user input type casting


c4 = complex(input("enter the element"))
s9 = set([c4])
print(c4)
print(type(s9))

# ## list -> set 


l17 = [12, 'Pradip', 56.9]
s10 = set(l17)
print(s10)
print(type(s10))

# #### user input typecasting


l18 = list(input("enter the elements").split(","))
s11 = set(l18)
print(s11)
print(type(s11))

# ## tuple -> set 


t5 = [12, 'Pradip', 56.9]
s11 = set(t5)
print(s11)
print(type(s11))

# #### user input typecasting


t6 = tuple(input("enter the elements").split(","))
s12 = set(t6)
print(s12)
print(type(s12))

# ## boolean -> set


b9 = False
s13 = set([b9])
print(s13)
print(type(s13))

# #### user input typecasting


b10 = bool(input("Enter your choice"))
s14 = set([b10])
print(s14)
print(type(s14))

# ## dictionary -> set


d3 = {'Name':'Pradip','Age':21}
s15 = set(d3.values())
print(s15)
print(type(s15))

# #### user input type casting


d4 = {}
key = input("enter key:")
value = input("enter value: ")
d4[key] = value
s16 = set(d4.values())
print(d4)
print(s16)
print(type(s16))

# # Type casting of tuple


# ## str -> Tuple


s23 = ("Pradip" .split(" "))
t1 = tuple(s23)
print(t1)
print(type(t1))

# #### user input type casting


s24 = str(input("enter the elements"))
t2 = tuple(s24.split(","))
print(t2)
print(type(t2))


# ## int -> tuple


i23 = 56
sr2 = str(i23)
print(sr2)
print(type(sr2))

t2 = tuple((sr2).split(","))
print(t2)
print(type(t2))

# #### user input typecasting


i24 = int(input("enter the values"))
sr3 = str(i24)
t3 = tuple(sr3)
print(t3)
print(type(t3))

# ## float -> tuple


f5 = 23.65
sr4 = str(f5)
t4 = tuple((sr4).split(","))
print(t4)
print(type(t4))

# #### user defined typecasting


f6 = float(input("enter the value"))
sr5 = str(f6)
t4 = tuple((sr5).split(","))
print(t4)
print(type(t4))

# # conditonal statement in Python:
# 
# ### ->conditional statements in python mainly deals with given situation wrt if and else 
# 
# ### -> condition when gets comleated using if statement then the print of if will be executed othewise else condition will be executed 
# 
# ### -> Three types of condition which a user has to deal with:
# ### 1) If-else (for basic tasks)
# ### 2) Nested if (for a bit complex task but gets executed with few limitations.)
# ### 3) Elif condition (for complex tasks and gets executed smoothly).


age = 26
if age>=18:
    print("user can vote")
else:
    print("user cannot vote")

age1 = 16
if age1>=18:
    print("user can vote")
else:
    print("user cannot vote")

# #### User input 


age2 = int(input("enter user's age"))
if age2>=18:
    print("user can vote")
else:
    print("user cannot vote")

# # 2) Odd-even numbers


num = 56
if num%2==0:
    print("even number")
else:
    print("odd number")

# #### user defined 


num1 = float(input("enter your number"))
if num1%2==0:
    print("Even number")
else:
    print("Odd number")

# # 3)+ve/-ve numbers


value = int(input("enter the value"))
if value>0:
    print("+ve number")
else:
    print("-ve number")

# # Nested if:
# 
# ### ->There will be consideration of outer if and inner if condition
# ### ->Python will first read the main(outer)if condition and then it will read the iner if condition.
# ### Here, first it will check whether the outer if condition id getting pass/executed,ifyes,then only it will
# ### read the inner condition.


age3 = 19
if age3>=18:
    print("Can vote")
    if age3==18:
        print("First time voter")

num2 = -23
if num2>=0:
    print("+ve number")
    if num2==0:
        print("whole number")
else:
     print("-ve number")

# # Nested if-else


speed = 23
if speed <= 60:
    print("normal speed")
    if speed <= -1:
        print("speed sensor error range")
    else:
        print("sensor is in goodcondition ")
else:
    print("Over speed")


# # Elif condition 


# ### -> It is a combination of if and else condition.
# 
# ### -> Since ther will be no execution of inner condition here, every condition will be considered and displayed 


number = int(input("enter the value "))
if number>0:
    print("+ve number")
elif number==0:
    print("whole number")
else:
    print("-ve number")

balance = 100000
transaction = int(input("enter the amount"))
if transaction<balance:
    print("transaction succesfull")
elif transaction==0:
    print("0 transaction not allowed")
else:
    print("Transaction not successfull")

# # AND OR 


#### Truth table
#              AND    OR
# 1  0          0     1
# 0  1          0     1
# 0  0          0     0
# 1  1          1     1

marks = 60
if marks>80:
    print("1st class w distinction")
elif marks<80 and marks>60:
    print("1st class")
elif marks<=60 and marks>35:
    print("second class")
else:
    print("Needs improvement")

# # Assignment 12/01/26


# ### 1) If else 


time = 1300
if time>=1200:
    print("Good Afternoon")
else:
    print("Good Morning")

# #### User input greetings 


time1 = int(input("enter the timing in hrs"))
if time1>=1200:
    print("Good Afternoon")
else:
    print("Good Morning")

# ### 2)if else
# 
# ### owerweight checking for 10 wheel truck


weight = 17000
if weight>=18001:
    print("Overweight truck")
else:
    print("underweight Truck")

# ### user input checking


weight1 = int(input("Enter the weight in KG"))
if weight>=18001:
    print("Overweight truck")
else:
    print("underweight Truck")

# ## 2)Nested if else


# ### 1)speed indicator and sensor checking 


speed = -56
if speed <= 60 :
    print("normal speed")
    if speed <= -1:
        print("speed sensor error range")
    else:
        print("sensor is in good condition ")
else:
    print("Over speed")


# ### 1) speed indicator and sensor checking 


speed1 = int(input("enter the speed in KM/h: "))

if speed1 <= 60:
    print("Normal speed")
    if speed1 <= -1:
        print("Speed sensor error range")
    else:
        print("Sensor is in good condition")
else:
    print("Over speed")


# ### 2)Battery Percentage indicator


battery = 66
if battery <= 20:
    print("Low battery")
    if battery < 0:
        print("Battery sensor error")
    else:
        print("Please charge the battery")
else:
    print("Battery level OK")


# ### 2) Battery Percentage indicator user input


battery = int(input("Enter the BAttery Percentage"))
if battery <= 20:
    print("Low battery")
    if battery < 0:
        print("Battery sensor error")
    else:
        print("Please charge the battery")
else:
    print("Battery level OK")


# # 3)Elif statement 


# ### 1)Traffic signal speed checking 


vehicle_speed = 69
if vehicle_speed <= 60:
    print("You are in speed limit")
elif vehicle_speed == 0:
    print("Vehicle is steady")
else:
    print("Over speeding! Fine should be applied")


# ### 1)Traffic signal speed checking user input 


vehicle_speed = int(input("enter the speed in Km/h"))
if vehicle_speed <= 60:
    print("You are in speed limit")
elif vehicle_speed == 0:
    print("Vehicle is steady")
else:
    print("Over speeding! Fine should be applied")


# ### 2)Attendance checking system


present_days = 60
if present_days > 75:
    print("Attendance is sufficient")
elif present_days == 0:
    print("No attendance recorded")
else:
    print("Attendance is insufficient")


# ### 2)Attendance checking system


total_days = ("Total days:180")
print(total_days)
present_days = int(input("Enter number of days present: "))

if present_days > 75:
    print("Attendance is sufficient")
elif present_days == 0:
    print("No attendance recorded")
else:
    print("Attendance is insufficient")


fuel = '10L'
tank_capacity = str(input("enter the tank_capacity"))
if fuel<tank_capacity and tank_capacity>='1L':
    print("perfect")
elif tank_capacity == '0L':
    print("Atank cannot be empty")
else :
    print("high chance of explosion")

temp = input("Enter the temperature: ")

if temp > "25C":
    print("Warm day")
elif temp >= "10C":
    print("Cold day")
else:
    print("Extreme cold")


print(chr(75))

print(chr(99))

# # Loops in Python
# 
# ### -> Looping simply means any action happening on repeat.
# 
# ### -> There are two types of loop wjich we have to study :
# 
# ### 1)For Loop
# ### 2)While Loop
# 
# ### -> For loop works with range format.
# ### -> A specific range will be given and it will iterate accordingly.
# ### -> While loop will work/will iterate until it finishes the given condition.
# 


# ### For Loop


for i in range(10):
    print(i)

for i in range(2,10,3):
    print(i)

# ## While loop


i=1
while i<=5:
    print(i)
    i+=1

for i in range(10,-2,-2):
    print(i)

start = int(input("enter the start number:"))
stop = int(input("enter the stop number:"))
step = int(input("enter the step number"))
for i in range(start,stop,step):
    print(i)

for i in range(10):
    print(" 💀 "*10)

for i in range(5):
    print(" + "*5)

for i in range(5,1):
    print(" + "*i)

for i in range(1,10,3):
    print(" - "*i)

for i in range(1,10,1):
    print(" * "*i )

for i in range(1,10,1):
    print(" + "*i)
for j in range(10,0,-1):
    print(" + "*j)


n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    print(" + " * i)
for j in range(n, 0, -1):
    print(" + " * j)

n = 5
for i in range(1,11):
    print(n,"X",i,'=',n*i)

#User input Table
n1 = int(input("Enter the no:"))
for i in range(1,11):
    print(n1,"X",i,'=',n1*i)

n2 = 5
for i in range(1,11):
    print(f"{n}X{i}={n*i}")

l = ['apple','kivi','graps']
for l1 in l:
    print(l1)

# ## Pyramid 


n1 = int(input("Enter the start/stop number:"))
for i in range(1,n1+1):
    print(" " * (n1 - i) + "*" * (2*i-1))

n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    print("  " * (n - i) + "*" * (2*i-1))

# ## Diamond


n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "+ " * i)
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "+ " * i)

for i in range(1, 10):
    print( "  "* (9 - i) + "*"* (2*i-1))

d = {}
n = int(input("Enter the key value pair"))
for i in range(n):
    k = input("Enter the keys")
    v = input("Enter the values")
    d[k]=v
print(d)

## nested for loop
for i in range(1,11):
    for j in range(1,11):
        print(i*j,end="\t")
    print()

l1 = [21,23,56,45]
l2 = [89,68,78]
for li in l2:
    for lii in l1:
        print(li+lii,end="\t")
    print()

# ## Break statement in loop


pas = "pradip2004"
for i in range(3):
    ui= input("enter the password")
    if ui == pas:
        print("correct password")
        break
else:
    print("incorrect password")

a = (input('enter the text'))
if a==a[::-1]:
    print("the given text is an palindrome")
else:
    print("it is not an palindrome")

n33 = 7
f = 1
for i in range (1,n33+1):
    f*=i
print(f)

n22 = 23
if n22>1 and all(n22%i!=0 for i in range(2,n22)):
    print("prime")
else:
    print("not a prime")

n33 = 18
if n33>1 and all(n33%i!=0 for i in range(2,n33)):
    print("It is a prime number")
else:
    print("It is not a prime number")

n66= 8
a = 0
b = 1
for i in range(n66):
    c = a + b
    print(c,end=" ")
    a=b
    b=c

n77 = int(input("Enter the number:"))
a = 0
b = 1
print(a, b, end=" ")
for i in range(n77):
    c=a + b
    print(c,end=" ")
    a=b
    b=c

import math

max(-1,-25,-68,-98,-56,-23)

import math

math.ceil(14.0001)

math.floor(14.)

# ### user defined function


def hello():
    print("Welcome to my lab")

hello()

def Area(L,B):
    print("Area of ractangle",L*B,"m^2")

Area(8,9)

def circle(r):
    print("Area of circle:",math.pi*r*r,"M^2")

circle(26)

def T(Text):
    print(len(Text))

T("pradip")

def summation(n1,n2,n3,n4):
    print(sum([n1,n2,n3,n4]))

summation(2,465,79,32)

l2=[2,3,5,6,7]
sum(l2)

def number(n):
    if n>0:
        print("positive number")
    else:
        print("negative number")

number(-65)

def number1(n1,n2):
    print("The minimum number is ",min(n1,n2))
    print("The maximum number is:",max(n1,n2))

number1(45,65)

def p(n2):
    for i in range(n2):
        print("  "*(n2-i),"*"*(2*i+1))

p(9)

l = [1,2,3,4,5,6]
l2=list(map(lambda l3:l3*l3,l))

l2

l = [1,2,3,4,5,6]
l2=list(filter(lambda l3:l3%2,l))

l2

l8 = ['pradip','kunvariya','vishnu','pra']
l9 = list(filter(lambda l7:len(l7)>4,l8))

l9

l10 = ['Apple','45','FRUITS','15.8+Jk','ORANGE','Pradip']
l11 = list(filter(lambda l12:str.isupper(l12),l10))

l11

from functools import reduce

l13 = [56,89,12,33,65,45]
l14 = reduce(lambda x,y:x+y,l13)
l14

l15 = [56,123,45,785,13]
l16 = reduce(lambda a,b:a if a>b else b,l15)

l16

with open("Calculator_ops.py",'w') as c:
    c.write("""
def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def multi(a,b):
    print(a*b)
def fdiv(a,b):
    print(a/b)
def idiv(a,b):
    print(a//b)
""")

import Calculator_ops as c

c.add(23,56)

c.idiv(22,2)

with open(r"C:\Users\Pradip\OneDrive\Desktop\application read.txt",'r') as f:
    data = f.read()
    print(data)

with open(r"C:\Users\Pradip\Downloads\python.jpg",'rb') as f1:
    data1 = f1.read()
    print(data1)

print(len(data1))

with open(r"C:\Users\Pradip\Downloads\Mall_Customers.csv.xls",'rb') as f3:
    data3 = f3.read()
    print(data3)

g4 = [5]
d = {0: g4[0]}
print(d)
type(d)

# # object oriented programming in Python


# ## -> Class -> Blue-print of an object
# ## -> Object -> Repesentation of a blue print(Class)
# ## -> Method ->Defined inside a class
# ## -> An object cannot be created without a class.
# ## -> self -> Object calling class 


class hi():
    def method(self):
        print("Hello")
p = hi()
p.method()

class name():
    def n1(self):
        print('how are you?')
n2=name()
n2.n1()

class Student():
    def __init__(self, name, age,marks):
        self.name = name
        self.age = age
        self.marks = marks
    def detail(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Address:",self.marks)
h = Student("Pradip", 21,55)
h.detail()

h.detail()

class parent():
    def pr(self):
        print("Hello")
class child(parent):
    def ad(self):
        print("Pradip")
h = child()
h.pr()
h.ad()


# # Inheritance in OOPs:
# 
# ## -> Sub-class/Child class will inherit(adopt) the traits from main class (parent class).
# 
# ## -> Types of Inheritance:
# 
# ### 1) Single Inheritance
# 
# ### 2) Multiple Inheritance
# 
# ### 3) Multilevel Inheritance
# 
# ### 4) Hierarchical Inheritance
# 
# ### 5) Hybrid Inheritance


# # 1) Single Inheritance:
# 
# ### Involvement of one parent class (main class) and one child class (sub class).


class parent():
    def p(self):
        print('Parent Class')
class child(parent):
    def c(self):
        print('Child Class')
# Object
c1 = child()
p1 = parent()
c1.c()
c1.p()
p1.p()

class e_commerce():
    def e_c(self):
        print('E-commerce')
class flipkart(e_commerce):
    def f_k(self):
        print('Flipkart is an e-commerce site')

f = flipkart()
f.f_k()
f.e_c()

# # 2).Multiple inheritance


# ### -> Involvement of multiple parent class (main class) and one child class (sub-class).


class father():
    def pr(self):
        print("fathers skills")
class mother():
    def ad(self):
        print("mothers quality")
class child3(father,mother):
    pass
h1 = child3()
h1.pr()
h1.ad()

# # 3).Multilevel Inheritance:


# ## -> There will be an involvement of a main class (eg: class 1) then there will a sub-class 1who will inherit traits from class 1 and another sub-class 2 which will adopt the traitsfrom both the levels.


class grandparent():
    def gp(self):
        print("grandparent class")
class parent(grandparent):
    def p3(self):
        print("Parent class")
class child3(parent):
    def c3(self):
        print("Child class")
h3 = child3()
h4 = parent()
h3.gp()
h3.p3()
h3.c3()
h4.gp()
h4.p3()
    

# # 4).Hierarchical Inheritance
# 
# ### -> There will be involvement of one parent class and multiple sub-classes inheritingtraits from the main class


class vehicle():
    def car(self):
        print("It is a car")
class manual(vehicle):
    def m1(self):
        print("It is a manual car")
class automatic(vehicle):
    def a3(self):
        print("It is a automatic car")
class EV(vehicle):
    def e3(self):
        print("It is a electric car")
v1 = manual()
v2 = automatic()
v3 = EV()
v1.car()
v1.m1()
v2.car()
v2.a3()
v3.car()
v3.e3()

# # 5).Hybrid inheritance
# 
# ## -> It is a combination of multiple and multilevel inheritance.


class Vehicle:
    def car(self):
        print("This is a vehicle")
class Manual(Vehicle):
    def m1(self):
        print("This is a manual car")
class Automatic(Vehicle):
    def a1(self):
        print("This is an automatic car")
class Toyota(Manual, Automatic):
    def brand(self):
        print("Brand is Toyota")
class EV(Vehicle):
    def e1(self):
        print("This is an electric car")
# Object 
t = Toyota()
t.car()
t.m1()
t.a1()
t.brand()
e1 = EV()
e1.e1()

# # Polymorphism
# 
# ## -> Poly -> many
# 
# ## -> morphism -> same method
# 
# ## Here, a user can build a/multiple class where the method will remain same.
# 
# ## Polymorphism even deals with operators by operation overloading method.


class vehicle():
    def v(self):
        print("This all are vehicles")

class car():
    def v(self):
        print("Car:It runs on the road")

class aeroplane():
    def v(self):
        print("Aeroplane:It fly in the Air")

class ship():
    def v(self):
        print("Ship:It floats on the water")

vehicles = [vehicle(),car(),aeroplane(),ship()]
for vehicle in vehicles:
    vehicle.v()

# ## Opeartion Overloading (polymorphism part):
# 
# ## -> It simply overloads from the same constructor and then displays the outcome based on the return statement




# ### Adition operator


class a1():
    def __add__(self,other):
        print(self.value+other.value)
    def __init__(self,value):
        self.value = value

a2 = a1(5)
a3 = a1(6)
a2+a3

# ### subtraction operator


class a3():
    def __sub__(self,other):
        print(self.value-other.value)
    def __init__(self,value):
        self.value = value

a2 = a3(7)
a3 = a3(6)
a2-a3

# ### Multiplication operator


class a4():
    def __mul__(self,other):
        print(self.value*other.value)
    def __init__(self,value):
        self.value = value

a2 = a4(7)
a3 = a4(6)
a2*a3

# ### Division operator


class a5():
    def __truediv__(self,other):
        print(self.value//other.value)
    def __init__(self,value):
        self.value = value

a2 = a5(12)
a3 = a5(6)
a2/a3

# ### Comparition operator


class a6():
    def __gt__(self,other):
        print(self.value>other.value)
    def __init__(self,value):
        self.value = value

a2 = a6(12)
a3 = a6(5)
a2>a3

# # Encapsulation.
# 
# ### > We are simply creating a private variable inside a class which will be only displayed with the help of method called by object.
# 
# ### -> To set any variable private use self.__marks.
# 
# ### -> Simply we are encapsulating the data that it will be only accessed by using the method.


class private():
    def __init__(self,marks):
        self.__marks = marks
    def detail(self):
        return self.__marks

d = private(66)
d.detail()

class Student():
    def __init__(self, name, age,marks):
        self.name = name
        self.age = age
        self.__marks = marks
    def detail(self):
        print("marks:",self.__marks)
h = Student("Pradip", 21,55)
h.detail()
h.name

class Student:
    def __init__(self, name, marks):
        self.__marks = marks      
        self.name = name          
    def get_marks(self):          
        print( self.__marks)
s = Student("Pradip", 85)
s.name         
s.get_marks() 

s = Student("Pradip", 85)       
s.get_marks()
s.name

class pw1():
    def __init__(self,pw):
        self.__pw = pw
    def get(self):
        return self.__pw
    def set(self,newpw):
        if len(newpw)>=8:
            self.__pw=newpw
            print("The new password is:",newpw)
        else:
            print("Invalid password")

p = pw1("58675867")
p.get()

p.set("Pradip5867")

# # Abstraction 
# ### It means hiding the internal implementation and showing only what is necessary to the user
# ### In abstraction we focus on what to do instead of how to do.
# 
# ### In general, we do not focus on the procedure.


from abc import ABC,abstractmethod

class Car(ABC):
    @abstractmethod
    def start(self):
        print("It works on engine ignition")
        
class KIA(Car):
    def start(self):
        print("It starts with the start button")

k = KIA()
k.start()

import pandas as pd

# # Mean


# ### -> Defined as an average of the given data.
# 
# ### -> Mean is denoted by symbol xbar.
# 
# ### xbar = sigma(x)/n
# 
# ### sigma = Total/Sum of given observations
# ### n = number of observations given in data
# 


# # Meadian


# -> Defined as a central tendency which tells at what distance the points are far/nearer from each other.
# -> Symbol is M.
# -> For median we first need to sort the data into ascending order then we have to apply the formula for median
# M = n+1/2
# 
# Example
# 
# 14
# 25
# 8
# 7
# 99
# 
# 7
# 8
# 14
# 25
# 99
# 101
# 
# M = n+1/2
# 6+1/2 = 3.5
# 14+25/2 = 19.5
# 


# # Mode


# 
# Mode is denoted by symbol Z
# 
# -> It is defined as the consideration of those values who are having maximum frequency.
# 
# 


# # Standard Deviation and variance


# ### It lets us know at what actual distance our data points are situated on the basis of difference between the given observation divided by the given number of observations.Sample variance is denoted by sd^2
# ### sd^2 = sigma(x-xbar)^2/n-1
# 
# ### Example
# X       X-xbar
# 45      
# 54
# 25
# 87
# xbar = 52.75
# sd^2 = 668.25
# standard deviation (root of variance)
# sd = 25.85
# 


# # Population stardard deviation and variance


# 
# ### It is denoted by symbol sigma
# 
# ### sigma^2 = summation(x-xbar)^2/N
# 


# # Spearman's Rank Correlation Test
# 
# ### -> Data will be ordinal which simply data will be displayed in a particular order based on their rankings.
# 
# ### -> This test will be denoted by symbol roh.
# 
# ### -> This is also known as non-parametric test.
# 
# ### roh = 1-6summation(d)^2/n(n^2-1)
# 
# ### -> Range will be fixed: -1 to +1.
# 


# ### Regression analysis is a statistical method used to understand and model the relationship between variables.
# ### It helps us predict the value of one variable (called the dependent variable, usually y) based on the value(s) of another variable(s) (called independent variables, usually x).
# ### The simplest type is Simple Linear Regression, where:
# ### y=a+bx
# 
# #### Where:
# 	y= predicted value
# 	x= independent variable
# 	a= intercept (value of ywhen x=0)
# 	b= slope (rate of change of yper unit increase in x)
# 


# # Libraries in Python:
# 
# ### -> Libraries helps us to do tasks in easy format.
# 
# ### -> Python consists of more than approx. 1,30,000 libraries.
# 
# ### -> Popular libraries which we need to study are:
# 
# ### 1) Pandas 
# 
# ### 2) NumPy
# 
# ### 3) Visualisation Libs.
# 
# ### 4) SciPy
# 


# # 1) Pandas :
# 
# ### -> Utilized for data cleaning/data preprocessing.
# 
# ### -> For removing of unwanted columns.
# 
# ### -> For filling/dropping the null values.


# ### Data Collection -> Data Cleaning (most imp) -> Data Visualisation -> Data Predn.


import pandas as pd    #pd -> alias (short-name).

s = pd.Series(['name','age','course'])

print(s)

d = ({
    'name':['a1','a2','a3'],
    'age':[22,20,21],
    'course':['Python','DS','DA']
})

d

df = pd.DataFrame(d)

df

df.head()

df.tail()

df.info()

df.describe()

df

df.rename(columns = {'name':'Name','age':'Age','course':'Course'},inplace = True)

df

df = df.rename(columns = {'Name':'Names'})

df

df.replace({'Python':'PYTHON'})

df.mean(numeric_only = True)

df.median(numeric_only = True)

df.corr(numeric_only = True)

df.std(numeric_only = True)

df.var(numeric_only = True)

df1 = pd.DataFrame({
    'Course':['Python_Programming','DS','DA'],
    'course_fees':[15000,85000,65000]
})

df1

df3 = pd.merge(df,df1,on='Course')

df3

df4 = pd.concat([df,df1],axis=1)

df4

df

df5 = pd.DataFrame({'Dept':['HR','IT','HR','HR','Management','IT','IT'],
                   'Salary':[85000,90000,75000,55000,60000,95000,880000]
                   })

df5

df5.groupby('Dept')['Salary'].sum()

df5.groupby('Dept')['Salary'].count()

df5.groupby('Dept')['Salary'].min()

df5.groupby('Dept')['Salary'].max()

df5.groupby('Dept')['Salary'].agg(['sum','mean','min','max','count','median'])

df5.sort_values('Salary')

df5.sort_values('Salary',ascending=False)

chr(65)

df5.sort_values('Dept')

df5.sort_values('Dept',ascending=False)

df5[df5['Salary']>80000]

df5[(df5['Salary']>90000) & (df5['Dept']=='IT')]

import pandas as pd

df6 = pd.DataFrame({'Name':['a','b',pd.NA,'c'],
                   'Age':[22,23,25,pd.NA]})

df6

df7 = pd.DataFrame({'Name':['a1',pd.NA,'b1',pd.NA,'c1','d1'],
                    'Course' : ['DS',pd.NA,'python',pd.NA,'DA',pd.NA]})

df7

df8 = pd.read_csv(r"C:\Users\Pradip\OneDrive\Desktop\Mall_Customers (1).csv")

df8.head()

df8['Genre'] = df8['Genre'].map({'Male':1,'Female':2})


df8

df8.columns

df8[(df8['Age']>22) & (df8['Spending Score (1-100)']>80)]

df9 = pd.read_csv(r"C:\Users\Pradip\OneDrive\Desktop\Sales.csv")

df9.head()

df9['Sales'] = df9['Quantity']*df9['Amount']

df9.head()

df9[(df9['Product']>'Monitor') & (df9['Sales']>250)]

df9 = df9.drop(columns = ['Cost'])

df9.head()

df9.iloc[3,5]

df9.loc[1,'Product']

df9.reset_index()

# # 2)Numpy
# ## For doing any complex numerical computation which is wrt an array we make 
# 
# ### use of numeric python (numpy).
# 
# ### Here , complex calculations like inverse matrix,  transpose matrix, finding determinant
# 
# ### can be simply evaluated.
# 
# ### List -> collection of heterogeneous elements.
# 
# ### Array -> homogeneous elements are considered. 


# # Import Library


# import the library

import numpy as np

## np is alias of numpy 

a = np.array([1,2,3,4,5,6])

a.dtype

a.shape

a.itemsize

b = np.array([[1,2],[3,4]])
b

np.sum(b)

np.sum(b,axis = 1)

b.mean()

np.median(b)

np.square(b)

np.sqrt(b)

np.min(b)

np.max(b)

b.shape

b1 = np.array([[1,2,3],[3,4,5]])


b1

b1.reshape(3,2)

b.shape

b1.resize(3,2)

b1

e = np.linspace(0,50,5)

e

det = np.array([[5,7],[11,12]])

np.linalg.det(det)

b

np.transpose(b1)

np.linalg.inv(b)

b1.T

b = np.array([[1,2],[3,4]])


np.linalg.inv(b)

value = np.array([[8,9],[2,5]])

np.linalg.det(value)


np.linalg.inv(value)

np.linalg.norm([2,5])

np.dot(b,value)

# ### Alternate way of dot product.


b @ value

b>8

b<8

b[b<8]

arr1 = np.array([1,2,3,np.nan])
arr1

arr1.sum()

np.nansum(arr1)

np.nanvar(arr1)

np.nanstd(arr1)

arr2 = np.array([11,22,33])
b = 10
print(arr2+b)

x = np.array([1,5,6,8])
y = 4*x*x+3*x+5
print(y)

a = np.array([[11,22],[33,44]])
b = np.array([[1,2],[3,4]])

a

a,b


a @ b

print(a*b)

print(a+b)

a-b

np.sum(a+b,axis = 1) # sum of all rows of both matrices

a[1]

a[0,1]

a[0,0]

c = np.array([4,5,7,8,9,6,1])
c

np.cumsum(c)

np.cumproduct(c)

d = np.array([2,3,5,6,8,9,10])

np.cumproduct((c,d))

np.eye(4)

np.ones((3,3))

np.zeros(4)

e = np.array([12,23,56,89])

e

e[1] = 14

e

np.append(e , [5])

a = np.array([[11,22],[33,44]])

np.append(a,[[5,6]],axis = 0)

np.append(a,[[5],[6]],axis = 1)

b = np.array([1,2,3,4])

c = b.copy()
b[2] = 5

c

b

c = b.view()
b[2] = 5

c

b

d1 = np.array([11,22])
d2 = np.array([33,44])

np.vstack((d1,d2))

np.hstack((d1,d2))

d3 = np.array([[11,22,33,44],[33,66,77,88]])

a.flatten()

d3.flatten()