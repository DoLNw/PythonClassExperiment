# -*- coding: utf-8 -*-
stu0 = {
'学号':'123456',
'姓名':'李强',
'性别':'男',
'语文成绩':'56',
'数学成绩':'3'
}

stu1 = {
'学号':'113456',
'姓名':'阿三',
'性别':'男',
'语文成绩':'66',
'数学成绩':'57'
}

stu2 = {
'学号':'121456',
'姓名':'美丽',
'性别':'女',
'语文成绩':'96',
'数学成绩':'98'
}

stu3 = {
'学号':'123156',
'姓名':'胖虎',
'性别':'男',
'语文成绩':'47',
'数学成绩':'31'
}

stus = [stu0, stu1, stu2, stu3]

num = 3;
while_condition = True

while while_condition:
    flag1 = 0
    flag2 = 0
    flag3 = 0
    userin = input("请输入你要执行的操作：list/insert/delete/change/quit\n")
    if userin == 'list':
        print(stus)
    elif userin == 'insert':
        num = num + 1
        stus.append('stu'+str(num))
        stus[num] = {}
        stus[num]['学号']= input("请输入添加的学生的学号：\n")
        for k in range(0,num):
            if stus[num]['学号'] == stus[k]['学号']:
                print("输入的学号已存在\n")
                flag = 1
                break   
        if flag==1:
            continue
        stus[num]['姓名']= input("请输入添加的学生的名字：\n")
        stus[num]['性别']= input("请输入添加的学生的性别：\n")
        stus[num]['语文成绩']= input("请输入添加的学生的语文成绩：\n")
        stus[num]['数学成绩']= input("请输入添加的学生的数学成绩：\n")
    elif userin == 'delete':
        number = input("请输入你想删除的学生的学号：\n")
        for k in range(0,num):
            if stus[k]['学号'] == number:
                del stus[k]
                break  
            else:
                flag2 = 1
        if flag2 == 0:
            print("删除成功\n")
        else:
            print("该学号不存在\n")
    elif userin == 'quit':
        while_condition = False
    elif userin == 'change':
        change = input("请输入要修改信息的学生的学号：\n")
        for q in range(0,num):
            if stus[q]['学号'] == change:
                break
            else:
                flag3 = 1
                break
        if flag3 == 1:
            print("该学号不存在\n")
            continue
        changer = input("请输入要修改信息的学生的内容：\n")
        done = input("请输入修改的内容：\n") 
        stus[q][changer] = done
    else:
        print("输入错误请重新输入\n")