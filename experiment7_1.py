# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

##Content1:
#class ShaiXuan():
#    """筛选出大于等于2000小于等于3200的所有能被7整除但不能被5整除的数"""
#    
#    def __init__(self, nums):
#        self.nums = nums
#        
#    def shai(self):
#        for i in range(2000, 3201):
#            if ((i%7==0)and(i%5!=0)):
#                self.nums.append(i)
#        return self.nums
#
#nums = []
#shai_xuan = ShaiXuan(nums)
#print(shai_xuan.shai())
#
#
##Content2:
#number = int(input("请输入一个整数： "))
#
#squares = {i:i*i for i in range(1, number+1)}
#print(squares)
#
#
##Content3:
#strs = input("请输入你的列表中的元素并用逗号隔开： ")
#list_ = strs.split(',')
#def str_convert_to_int(x):
#    return int(x)
#numbers = list(map(str_convert_to_int, list_))
#
#a = [numbers[0]]
##你只要自己内心知道它是一个二维数组就可以了，不需要显示声明它是二维数组也不需要类型[[]]就已经算是b[0]=[]了
#b = []
#for i in range(1, len(numbers)):
#    if numbers[i] in a:
#        a.append(numbers[i])
#    else:
#        b.append(a)
#        a = [numbers[i]]
#b.append(a)
#
#for c in b:
#    print(c)


##Content4:
#class Tongji():
#    
#    def __init__(self, comment_row_count, code_row_count, white_row_count):
#        self.comment_row_count = comment_row_count
#        self.code_row_count = code_row_count
#        self.white_row_count = white_row_count
#    
#    def tong(self):
#        with open("testForExperiment7_4.txt") as file_object:
#            for line in file_object:
#                if len(line.lstrip()) == 0:
#                    self.white_row_count += 1
#                elif (line.lstrip())[0] == '#':
#                    self.comment_row_count += 1
#                else:
#                    self.code_row_count += 1
#        return self.comment_row_count, self.code_row_count, self.white_row_count
#tongji = Tongji(0, 0, 0)
#a, b, c = tongji.tong()
#            
#print("注释行数: {}， 代码行数: {}， 空白行数: {}".format(a, b, b))
            

#Content5:
strs = input(r"请输入你的列表中的元素并用逗号隔开： ")
list_ = strs.split(',')
def str_convert_to_int(x):
    return int(x)
numbers = list(map(str_convert_to_int, list_))

i=0
j=len(numbers)-1
leftSum = numbers[i]
rightSum = numbers[j]

while i < j-2 :
    if leftSum > rightSum:
        j -= 1
        rightSum += numbers[j]
    else:
        i += 1
        leftSum += numbers[i]

if leftSum == rightSum:
    print("平衡点存在，平衡点为1,3,5,7,8,25,4,20： {}".format(numbers[i+1]))
else:
    print("平衡点不存在，最接近平衡点的位置索引值为： {}".format(i+1))
print(leftSum)
print(rightSum)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

