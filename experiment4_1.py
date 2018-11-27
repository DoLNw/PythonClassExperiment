# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

##Content1:
#import random
#guessNumber = random.randint(1,9)
#number = int(input("Please enter a number to guess: "))
#if number > guessNumber:    print("bigger")
#elif number == guessNumber: print("equal")
#else:                       print("less")


##Content2:
#str = input("Please enter multiple elements with the whitespace separation: ")
#strs = str.split(' ')
##strs.reverse()
##print(strs)
#i=len(strs)
#while(i>0):
#    print(strs[i-1], end=' ')
#    i = i-1


##Content2:
#price = int(input("Please enter the price: "))
#if price>=50 and price<=100: price = 0.9*price
#elif price > 100: price = 0.8*price
#
#print("The final price is: {}RMB".format(price))

#Content4:
total = 0
maleTotal = 0
femaleTotal = 0
maleAverage = 0
femaleAverage = 0
female = []
male = []
for i in range(10):
    gender = input("Please enter the gender: ")
    age = int(input("Please enter the age: "))
    if age>=10 and age<=12:
        total = total + 1
        if gender == 'm':
            male.append(age)
            maleTotal = maleTotal + 1
            maleAverage = maleAverage + age
        elif gender == 'f':
            female.append(age)
            femaleTotal = femaleTotal + 1
            femaleAverage = femaleAverage + age
if femaleTotal != 0: femaleAverage = femaleAverage/femaleTotal
if maleTotal != 0: maleAverage = maleAverage/maleTotal

smale = 0
sfemale = 0
for age in male:
    smale = smale + (age-maleAverage)**2
for age in female:
    sfemale = sfemale + (age - femaleAverage)**2

print("Total number: {}".format(total))
print("Male's average age is: {0} and the variance is: {1}".format(maleAverage, smale))
print("Female's average age is: {0} and the variance is: {1}".format(femaleAverage, sfemale))
