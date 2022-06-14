# -*- coding:utf-8 -*-
# @Time : 2022/6/11 16:20
# Auther : shenyuming
# @File : test_01.py
# @Software : PyCharm

s_1 = '55'
list_1 = ['556','55','5578','3455','66']
# for i in list_1:
#     if s_1 in i:
#         print(i)

## filter 过滤，s_1是否在list_1中
# print(list(filter(lambda x: s_1 in x, list_1)))

#s_1是否在list_1中
for i in list_1:
    if s_1 not in i:
        print('不对')
        break
else:
    print('对')
