# -*- coding:utf-8 -*-
# @Time : 2022/6/9 10:38
# Auther : shenyuming
# @File : handle_rand_str.py
# @Software : PyCharm

'''
生成 随机数
'''
from string import digits,ascii_letters
import random

def get_rand_str(length):
            #random.sample(ascii_letters+digits,length)
    return ''.join(random.sample(ascii_letters+digits,length))

if __name__ == '__main__':
    print(get_rand_str(5))