# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 08:08:50 2020

"""

a=10
b=21
c=a+b
print(c)

d=14.5
print(d)
print(d*10) #d value multiplied

e="Hello "
print(e)
print(e * 5)

#welcome to PPIT
a=b=c=d=15
print(a,b,c,d)

a,b,c=10,30,20
print(a,c,b)

#python index starts with 0
a = 'Welcome to Python'
print(a)
print(a[1]) #e
#after : whateve the number is given, -1 from that number is considered
print(a[2:6])#lcom
print(a[4:6])#om
print(a[8:10])#to
##############################################################################
##################       DATA TYPES         ###################
##############################################################################
# Numbers Strings list tuples dictionary

#NUMBERS
#no need to define whether a variable in integer or float
a = 20
b = 10.5
c = 300
print(a,c,b)

#STRINGS
#both double quotes and single quotes allowed
a="Hello"
b='welcome '
print(b,a)
print(b*3)

c = "Hello \
     Abhi "
print(c)
print(c[4:7])
print(c[4:20])

a='''welcome
to
python'''
print(a)

#LIST
#list is like array in JAVA and Vector in R
#one variable multiple values..int char float
#mutable-->can change exsting values and add new values or delete
a=[10,22.15,'Hello']
print(a)

b=[a,10,20]
print(a,b)

print(a[0:2])

a= [a,100]
print(a)
#TUPLES
#non-mutate--> can't change values or can't add new values
a=(10,22.50,'Super')
print(a)
print(a[1])
print(a[1:])

#DICTIONARY
#to store Key Values
a={'name':'Kumar','id':50,'dept':'physics'}
print(a)
print(a[1])
print(a)
print(a.keys())
print(a.values())

 #list-->[]
#tuple-->()
#dictionary-->{}

##############################################################################
##################        OPERATORS          ###################
##############################################################################
#1. Arithmatic
#2. Relational
#3. Assignment
#4. Logical
#5. Membership
#6. Identity
#7. Bitwise

#1. Arithmatic Operators
a=20
b=10
print(a+b)
print(a-b)
print(a*b)
a=10
b= 15
print(a/b)
print(b/a)
print(b//a)# eliminate floating output and print descrete values

print(a%b) #to get the reminder value

print(a*a*a*a)
print(a**4)# ** to get to the power of values

#2. Relational Operators



#3. Assignment Operators
# Assign values to variable
a =  10 # 10 assigned to a

a = a + 2 
print(a)

b = 5
b+=5
print(b)

b = 5
b-=2
print(b)

c = 5
c*=5
print(c)

a=10
a%=3
print(a)

a=10
a/=3
print(a)

a=10
a//=5 #divided by how many times value
print(a)

a=10
a**=3#10*10*10
print(a)


#4. Logical Operators



#5. Membership



#6. Identity


#7. Bitwise


###############################################################################
##################        DECISION MAKING          ###################
###############################################################################
#IF 
#IF ELSE
#IF ELIF
#there is no ENDIF required
a=10
if a==10:
 {print('a Equls to 10')}

a=11
if a!=10:
 print('a NOT Equls to 10')
 
year=2000
if year!=2000:
    print("Not equals to 2000")
else:
     print("Equals to 2000")
     
year=2000
if year!=2000:
    print("Not equals to 2000")
elif year<1000:
     print("year is greater than 1000")
else:
    print("equals to 2000")

###############################################################################
##################        LOOP WHILE        ###################
###############################################################################
#LOOP
num=1
for num in range(1,11):print(num)     
for num in range(1,11):
    print(num)   


#WHILE
num=1
while num<11:
    num=num+1
    print(num)

###############################################################################
##################        TRANSFER Staements          ###################
###############################################################################
#BREAK
#CONTINUE
#PASS

#BREAK
num=1
for num in range(1,11):
    if num==6: break
    print(num)      
        
#CONTINUE
num=1
for num in range(1,11):
    if num==6: continue
    print(num)  

#PASS
num=1
for num in range(1,11):
    if num==3: 
        pass #pass through this line when certain condition met
        print("Hello")
    print(num)  

###############################################################################
##################        Functions or Methods          ###################
###############################################################################
print(abs(-45))
import math
a=10
print(math.exp(a))
print(math.exp(10.23))

b=11.10
print(math.ceil(b))

print(math.floor(b))

print(math.pow(100,2))

print(math.sqrt(2))
print(math.sqrt(4))

print(max(19,10,1,10,111,24,78))
print(min(19,10,1,10,111,24,78))

import random
tuple=(1,2,3,4,5,6,7,8,9,10)
list =[19,10,1,10,111,24,78]
print(random.choice(tuple))
print(random.choice(list))

print(random.random())
#print reandom variable between 1 to 11 with out decimal point
print(random.randrange(1,11,1)


name1 = "hello"
surname1 = "bolo"
print(len(name1))
print(name1.capitalize())
print(surname1.capitalize())

sub="l"
print(name1.find(sub))
sub1="o"
print(name1.find(sub1))#finds the postion of the sub1 in name1

name="Hello"
print(name.isalnum())#check for ALPHANUMERIC

name="Hello"
print(name.isalpha())

name1="Hello@Welcome"
print(name1.isascii())

name1="Hello@Welcome"
print(name1.isalnum())


Name1 = "1234567"
print(name1.isalnum())
