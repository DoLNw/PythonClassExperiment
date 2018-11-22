# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

##Content2
#store = []
#for i in range(1, 100):
#    if i<10 :
#        if (i == (i*i%10)): store.append(i)
#    else:
#        if (i == (i*i%100)): store.append(i)
#print(store)
#
#
##Content3
#store = []
#for i in range(1, 100):
#    if i<10 :
#        if (i == (i*i%10)): store.append(i)
#    else:
#        if (i == (i*i%100)): store.append(i)
#print(tuple(store))
#
#
##Content4
#number = int(input("请输入一个整数: "))
#store = []
#for i in range(1, number+1):
#    if number % i == 0:
#        store.append(i)
#
#print(store)

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print("hello "+magician+" world!")


motors = ['honda', 'yamaha', 'suzuki']
print(motors)
motors[0] = 'ducati'
motors.append('honda')
#下面这句话只能是h、o、n、d、a一个个加入
motors += 'honda'
motors += ['honda']
motors.insert(1, 'ddd')
print(motors)


cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))
print(cars)


cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)
print(len(cars))