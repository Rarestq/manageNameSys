# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 09:26:34 2018

@author: rarestzhou
"""

# 名字管理系统 --> list的增删改查

# 1. 打印功能提示
print ('='*20)
print ('----名字管理系统----')
print (' 1.添加一个新的名字')
print (' 2.删除一个名字')
print (' 3.修改一个名字')
print (' 4.查询一个名字')
print (' 5.退出系统')
print ('='*20)

names = [] #定义一个列表用来存储新添加的名字
while True:  
    # 2. 获取用户选择
    num = int(input('请输入您要操作的功能序号(1 - 5):'))
    
    # 3. 根据用户选择，执行相应的功能
    if num == 1:                              # 添加名字
        new_name = input('请输入名字：')
        if new_name not in names:
            names.append(new_name)
            print (names)
        else:
            print ('名字已存在，请重新输入')
    elif num == 2:                              # 删除名字
        delete_name = input('请输入你要删除的名字：')
        if delete_name in names:
            names.remove(delete_name)
            print ('删除成功，删除的名字是：%s'%delete_name)
            print (names)
        else:
            print ('对不起，您要删除的名字不存在，请重新输入')
    elif num == 3:                          # 修改名字
        print ('名字列表长度为:%d'%len(names))
        update_name_index = int(input('请输入要修改的名字的下标:'))
        if update_name_index <= len(names):
            update_name = input('请输入要修改的名字：')
            print ('您要修改的名字是:%s'%names[update_name_index])
            names[update_name_index] = update_name
            print('修改后的名字是:%s'%names[update_name_index])
            print (names)
             
    elif num == 4:                          # 查找名字
        find_name = input('请输入要查询的名字：')
        if find_name in names:
            print ('找到了你想找的人：%s'%find_name)
        else:
            print ('查无此人')
    elif num == 5:
        break
    else:
        print ('您的输入有误请重新输入：')
        num = int(input())
