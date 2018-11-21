# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import math

#Content3
print("Content3")
message = "hello world!"
print(message.title())

#Content4
print("\nContent4")
for i in range(0, 6):
    for j in range(0, (5-i)):
        print (" "),
    for j in range(0, 2*i+1):
        print ("*"),
    print("")

#Content5
print("\nContent5")
r = int(input("please write the bottom radius: "))
h = int(input("please write the height       : "))
surfaceArea = math.pi*r*r*2 + 2*math.pi*r*h
print(surfaceArea)
volume = math.pi*r*r*h
print(volume)

#Content6
print("\nContent6")
x = int(input("first   :"))
o = raw_input("operator:")
y = int(input("second  :"))
if o == '+' :
    result = x + y
elif o == '-':
    result = x-y
elif o == '*':
    result = x*y
elif o == '/':
    result = x*1.0/y
print(result)

#Content7
print("\nContent7")
month = input("month: ")
day = input("day  : ")
months={'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 
'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12 }
days = {1:'first',2:'second', 3:'third', 4:'fourth', 5:'fifth', 6:'sixth', 7:'seventh', 
8:'eighth', 9:'ninth', 10:'tenth', 11:'eleventh', 12:'twelfth', 13:'thirteenth', 14:'fourteenth', 
15:'fifteenth', 16:'sixteenth', 17:'seventeenth', 18:'eighteenth', 19:'ninteenth', 20:'twentieth', 
21:'twentyfirst', 22:'twenty-second', 23:'twenty-third', 24:'twenty-fourth', 25:'twenty-fifth', 
26:'twenty-sixth', 27:'twenty-seventh', 28:'twenty-eighth', 29:'twenty-ninth', 30:'thirtieth', 31:'thirty-first' }
for n,m in months.items():
    if m == month:
        print(n + ' '),
for d,n in days.items():
    if d == day:
        print(n)

#Content8
print("\nContent8")
a = 1; b = 1
count = int(input("please write the count: "))
print("1 1 "),
for i in range(count-2):
	a,b = b, a+b
	print(b),







