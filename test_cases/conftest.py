# -*- coding:utf-8 -*-
# @Time : 2022/6/6 21:35
# Auther : shenyuming
# @File : conftest.py
# @Software : PyCharm

import pytest
from time import sleep
from common.comm_driver import Comm_driver
#钩子函数
def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        print(item.nodeid)
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")
        # TODO 调换顺序，去掉某个测试用例


@pytest.fixture(scope='session',autouse=True)  #autouse 默认对本conftest文件及子目录下的所有的测试所有的使用
def  fix_all():
    print('\n宝利商城WEBUI自动化测试开始 ...')
    yield
    print('\n宝利商城WEBUI自动化测试结束 ...')
    commondriver = Comm_driver()
    sleep(3)
    commondriver.driver.quit()
