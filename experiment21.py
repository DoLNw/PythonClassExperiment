# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

##Content1:
#s1 = input("请输入第一个字符串s1: ")
#s2 = input("请输入第二个字符串s2: ")
#s3 = input("请输入第三个字符串s3: ")
#s = "{}{}{}".format(s3, s2, s1)
#print(s)


##Content2:
#s1 = input("请输入第一个短字符串s1: ")
#s2 = input("请输入第二个短字符串s1: ")
#s3 = input("请输入第一个长字符串s1: ")
#
#for i in range(len(s3)):
#    if s3.startswith(s1, i, len(s3)): #此处是len（s3），再-1是不行的
#        print(i)
#print(s3.replace(s1, s2))


##Content3:
#sum = 0
#n = int(input("请输入相加的个数: "))
#numStr = input("请输入{}个数相加的字符串: ".format(n))
#nums = numStr.split('+')
#for num in nums:
#    sum = sum + int(num)
#    if (nums.index(num)==0): print("{}".format(num), end='')
#    else: print("+{}".format(num), end='')
#print("={}".format(sum), end='')
    

#Content4:
#rawData = input("请输入原始数据: ")
#encryptedData = []
#whiteSpace = 0
#for i in range(len(rawData)):
#    if (rawData[i] == ' '):
#        whiteSpace += 1
#        encryptedData += chr(5+whiteSpace)
#    else:
#        encryptedData += chr(10 + ord(rawData[i]))
#print('加密字符: '+''.join(encryptedData))
#rawData = input("请输入原始数据: ")
#encryptedData = []
#for i in range(len(rawData)):
#    encryptedData += chr(10 + ord(rawData[i]))
#print('加密字符串: '+''.join(encryptedData))
#
#bb = input("请输入加密数据: ")
#aa = []
#for i in range(len(bb)):
#    aa += chr(ord(bb[i])-10)
#print('解密字符串: '+''.join(aa))

#import base64
#rawData = input("请输入原始数据: ")
#s = base64.b64encode(rawData.encode(encoding='utf-8'))
#print(s)


#Content5:
#year = int(input("请输入年份: "))
#month = int(input("请输入月份: "))
#if month == 2:
#    if (year % 4 == 0) or (year % 200 == 0): print("{}年{}月的天数有{}天".format(year, month, 29))
#    else: print("{}年{}月的天数有{}天".format(year, month, 28))
#else:
#    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
#        print("{}年{}月的天数有{}天".format(year, month, 31))
#    else:
#        print("{}年{}月的天数有{}天".format(year, month, 30))

##import calendar
##print(calendar.monthrange(year, month)[1])


def Rank(score):
    if score>=90 and score<=100:
        return 'A'
    elif score>=80 and score<=89:
        return 'B'
    elif score>=70 and score<=79:
        return 'C'
    elif score>=60 and score<=69:
        return 'D'
    if score>=0 and score<=59:
        return 'E'

a = int(input("请输入成绩: "))
print(Rank(a))




