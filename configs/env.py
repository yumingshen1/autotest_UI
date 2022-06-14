# -*- coding:utf-8 -*-
# @Time : 2022/6/5 16:46
# Auther : shenyuming
# @File : env.py
# @Software : PyCharm
'''
配置文件
'''

class ENV:
    BROWSER_TYPE = 'chrome'
    IMPLICITLY_WAIT_TIME = 5
    HEADLESS_FLAGE = False #默认有头
    POLLY_URL = 'http://120.55.190.222:38090/#/login'
    POLLU_URL_PAGE = 'http://120.55.190.222:38090/#/home'
    WEB_DRIVER_WAIT_TIMEOUT = 10 #显示等待最大时间
    POLL_FREQUENCY_TIME = 0.5 #显示等待轮循时间

