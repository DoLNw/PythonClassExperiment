# -*- coding: UTF-8 -*-


# #Content1:
# import sqlite3
# def convert(value):
#     if value.startswith('~'):
#         return value.strip('~')
#     if not value:
#         value = '0'
#     return float(value)

# conn = sqlite3.connect('food.db')
# curs = conn.cursor()
# curs.execute('''DROP TABLE IF EXISTS food''')
# curs.execute('''
#     CREATE TABLE food(
#         id      TEXT  PRIMARY KEY,
#         desc    TEXT,
#         water   FLOAT,
#         kcal    FLOAT,
#         protein FLOAT,
#         fat     FLOAT,
#         carbs   FLOAT,
#         fiber   FLOAT,
#         ash     FLOAT,
#         Ca      FLOAT,
#         P       FLOAT,
#         Fe      FLOAT,
#         S       FLOAT,
#         K       FLOAT
#     )
#     ''')
# query = r'INSERT INTO food VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
# with open('ABBREV.TXT') as file_object:
# 	for line in file_object:
# 		fields = line.split('^')
# 		vals = [convert(f) for f in fields[0:14]]
# 		curs.execute(query,vals)

# conn.commit()
# conn.close()





# #Content2:
# import sqlite3
# conn = sqlite3.connect('food.db')
# curs = conn.cursor()

# print('显示前10行: ')
# for line in list(curs.execute('SELECT * FROM food LIMIT 0,10')):
# 	print(line)

# print('修改id为01001的desc为None')
# curs.execute("UPDATE food SET desc='None' WHERE id='01001' ")

# print('删除id为01002的数据行')
# curs.execute('DELETE FROM food WHERE id="01002"')

# print('添加id为11111的数据行')
# query = r'INSERT INTO food VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
# curs.execute(query, ['11111','None',0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2])

# print('查询id为11111的数据: ')
# print(list(curs.execute('SELECT * FROM food WHERE id="11111"')))

# print('增删改查之后: ')
# for line in list(curs.execute('SELECT * FROM food LIMIT 0,10')):
# 	print(line)

# conn.commit()  #注意没有commit之前结束后不会保存修改
# conn.close()







# #Content3:
# import sqlite3
# conn = sqlite3.connect('food1.db') #若不存在会新建一个，但是没有创建表单的话，后面插入什么的会抛出错误，此处不会抛出异常
# curs = conn.cursor()


# print('添加id为11111的数据行')
# query = r'INSERT INTO food VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
# print('加捕获异常： ')
# try:
# 	curs.execute(query, ['11111','None',0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.2])
# except sqlite3.Error:
# 	print('Insert failed!')

# # print('不加捕获异常： ')
# # curs.execute(query, ['11111','None',0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.2])

# curs.close()







#Content4:
#用的这个pip install mysql-connector或pip install pymysql
#因为用pip install MySQL-python在py3貌似有另外的包的命名改变问题或者py3被抛弃了，可以使用mysql.connector或者pymysql？
# import pymysql
# conn = pymysql.connect(host="localhost", port=3306, user="root", passwd='0717wjcWJCv', db='mysql') 
# cur = conn.cursor()
# cur.execute('SELECT * FROM user')
# for r in cur.fetchall(): 
# 	print(r) 
# conn.close()

#专门创建了另一个一个数据库JiaChengFirst: create database JiaChengFirst, 在⁨Macintosh HD⁩ ▸ ⁨usr⁩ ▸ ⁨local⁩ ▸ ⁨var⁩ ▸ ⁨mysql里面。
#专门创建了另一个用户JiaCheng： create user JiaCheng@localhost identified by '1234abcd';
#							 grant all privileges on *.* to JiaCheng@localhost;
import pymysql
# conn = pymysql.connect(host="localhost", port=3306, user="root", passwd='0717wjcWJCv', db='mysql')
conn = pymysql.connect(host="localhost", port=3306, user="JiaCheng", passwd='1234abcd', db='JiaChengFirst')
curs = conn.cursor()

# curs.execute("DROP TABLE IF EXISTS JiaChengTable1")
# sql = """CREATE TABLE JiaChengTable1 (
#          FIRST_NAME  CHAR(20) NOT NULL,
#          LAST_NAME  CHAR(20),
#          AGE INT,  
#          SEX CHAR(1),
#          INCOME FLOAT )"""
# curs.execute(sql)


# SQL 插入语句
sql = """INSERT INTO JiaChengTable1(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('JiaCheng', 'Wang', 20, 'F', 5000)"""
try:
   curs.execute(sql)
   conn.commit()
except:
   conn.rollback()

sql = "UPDATE JiaChengTable1 SET AGE = AGE+1 WHERE SEX = '%c'" % ('F')
try:
   curs.execute(sql)
   conn.commit()
except:
	print('failed')
	conn.rollback()


curs.execute('SELECT * FROM JiaChengTable1')
for r in curs.fetchall(): 
	print(r)

conn.close()









