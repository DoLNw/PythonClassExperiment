# try:
# 	print(5/0)
# except Exception as e:
# 	print("You can't divide by zero.")
# else:
# 	pass
# finally:
# 	print("sadsa")

# try:
# 	pass
# except Exception as e:
# 	raise
# else:
# 	pass
# finally:
# 	pass

# #Content1
# name = input("请输入你的名字： ")
# age = int(input("请输入你的年龄： "))
# year = (88 - age) + 2018
# print("{}年你的年龄为88岁".format(year))


# #Content3
# import random
# def guessGame():
# 	randomNumber = str(random.randint(1000, 9999))
# 	count = 0
# 	name = input("请输入你的姓名： ")
# 	while True:
# 		cowCount = 0
# 		bullCount = 0
# 		guessNumber = input("请输入你所猜测的四位数：")
# 		try:
# 			for i in range(4):
# 				if randomNumber[i] == guessNumber[i]:
# 					cowCount += 1;
# 				elif guessNumber[i] in randomNumber:
# 					bullCount += 1;
# 		except IndexError:
# 				print("IndexError, 请重新开始")
# 				continue
# 		count += 1;
# 		print("cow: {}, bull: {}".format(cowCount, bullCount))
# 		if randomNumber == guessNumber:
# 			print("恭喜{}猜测正确, 回合数:{}".format(name, count))
# 			return name, count

# def by_score(t):
#     return t[1]

# if __name__ == '__main__':
# 	#字典会把重合的回合数覆盖掉的，所以只能以名字为键值
# 	nameAndCounts = []
# 	cowCount = 0
# 	bullCount = 0
# 	for _ in range(5):
# 		name, count = guessGame()
# 		nameAndCounts.append((name, count))

# 	nameAndCounts = sorted(nameAndCounts, key=by_score)

# 	for name, count in nameAndCounts:
# 		print("姓名： {}, 回合数： {}".format(name, count))

# #Content4
# number11 = int(input("请输入序列1的第1个数字: "))
# number12 = int(input("请输入序列1的第2个数字: "))
# number13 = int(input("请输入序列1的第3个数字: ")) 
# number14 = int(input("请输入序列1的第4个数字: ")) 
# number1 = [number11, number12, number13, number14]
# number21 = int(input("请输入序列2的第1个数字: ")) 
# number22 = int(input("请输入序列2的第2个数字: ")) 
# number23 = int(input("请输入序列2的第3个数字: ")) 
# number24 = int(input("请输入序列2的第4个数字: ")) 
# number2 = [number21, number22, number23, number24]

# min = 65535
# for i in number1:
# 	for j in number2:
# 		if abs(i - j) < min:
# 			min = abs(i - j)
# print("两数列差的最小值为： {}".format(min))



# #Content5
# import math
# from functools import reduce
# def sumAll(x, y):
# 	return x + y

# def convertToInt(x):
# 	return int(x)

# def bzcha(x, y):
# 	return x + (y-average)*(y-average)

# str_ = input("请输入一串序列并用空格隔开: ")
# strs = str_.split()
# nums = list(map(convertToInt, strs))

# count = len(nums)
# sum_ = reduce(sumAll, nums)
# average = sum_ / count
# print("均值： {}".format(average))

# nums.insert(0, 0)
# fcha = (reduce(bzcha, nums)) / count
# print("方差： {}".format(fcha))

# bzcha = math.sqrt(fcha)
# print("标准差： {}".format(bzcha))



nameAndCounts = [[1,3,5,3],[2,43,5,3],[6,5,32,2],[4,56,1,2]]
def by_score(t):
	return t[1]
nameAndCounts = sorted(nameAndCounts, key=by_score)
print(nameAndCounts)


