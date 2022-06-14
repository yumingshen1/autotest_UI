# -*- coding:utf-8 -*-
# @Time : 2022/6/10 11:40
# Auther : shenyuming
# @File : conftest.py
# @Software : PyCharm

'''
商品管理页面的 conftest.py
'''
import pytest

from configs.env import ENV
from pageObjects.loginPage import LoginPage
from test_datas.login_datas import PASSWORD1, USERNAME1

@pytest.fixture(scope='session',autouse=False)
def fix_pm_cases(base_url): #base_url 插件，用例处理url,  需要在pytest.ini 文件中，
    print('\n 测试开始--登录')
    test_mainpage = LoginPage().open_loginpage(base_url).login_polly(USERNAME1, PASSWORD1)

    # test_mainpage = LoginPage().open_loginpage(ENV.POLLY_URL).login_polly(USERNAME1, PASSWORD1)

    yield test_mainpage
    print('\n 测试结束--')
