# -*- coding:utf-8 -*-
# @Time : 2022/6/8 16:42
# Auther : shenyuming
# @File : test_addproduct.py
# @Software : PyCharm

'''
1，登录保利商城
2，点击商品管理 -- 新的页面，首页，点击商品管理
3，点击添加商品 -- 新的页面，
    3.1  操作
    3.2 操作
    。。。。
    。。。。
4，点击商品列表，产生新的页面
    4.1 取列表第一个商品用于断言
'''
import pytest,allure,os
from pageObjects.loginPage import LoginPage
from pageObjects.mainPage import MainPage
from configs.env import ENV
from test_datas.login_datas import USERNAME1,PASSWORD1
from utils.handle_rand_str import get_rand_str
from utils.handle_path import report_path
from time import sleep

@allure.epic('保利商城webui自动化-商品')
@allure.feature('保利商城商品管理')
class Test_addproduct():
    @allure.story('添加商品_1')
    def test_addproduct_001(self,fix_pm_cases):
        with allure.step('1,登录'):
            # test_mainpage = LoginPage().open_loginpage(ENV.POLLY_URL).login_polly(USERNAME1,PASSWORD1)
            test_mainpage = fix_pm_cases    ## 调用了fixtrue
        with allure.step('2,跳转到添加商品页面'):
            test_addproduct = test_mainpage.goto_addproductpage()
        # test_mainpage = test_mainpage.open_loginpage(ENV.POLLY_URL)
        # test_addproduct = test_mainpage.login_polly(USERNAME1,PASSWORD1)
        # test_addproduct = test_addproduct.goto_addproductpage()
        with allure.step('3，添加商品'):
            pname = '自动化测试商品001'+get_rand_str(5)
            stitle = '自动化副标题001'+get_rand_str(5)
            test_addproduct.addproduct('1','1',pname,stitle,'1')
        with allure.step('4，回到首页'):
            #点击菜单
            test_addproduct.click_element(test_addproduct.home_button)
        with allure.step('5,进入商品列表并获取列表第一个商品'):
            #点击商品列表页面
            test_productlistpage = test_mainpage.goto_productlistpage()
            expected_name = test_productlistpage.get_first_productname()
        with allure.step('6,断言'):
            ##断言-商品列表第一个商品
            assert expected_name == pname
    sleep(2)
    @allure.story('添加商品_2')
    def test_addproduct_002(self,fix_pm_cases):
        with allure.step('1,登录'):
            # test_mainpage = LoginPage().open_loginpage(ENV.POLLY_URL).login_polly(USERNAME1, PASSWORD1)
            test_mainpage = fix_pm_cases  ## 调用了fixtrue
        with allure.step('2,跳转到添加商品页面'):
            test_addproduct = test_mainpage.goto_addproductpage()
        # test_mainpage = test_mainpage.open_loginpage(ENV.POLLY_URL)
        # test_addproduct = test_mainpage.login_polly(USERNAME1,PASSWORD1)
        # test_addproduct = test_addproduct.goto_addproductpage()
        with allure.step('3，添加商品'):
            pname = '自动化测试商品002' + get_rand_str(5)
            stitle = '自动化副标题002' + get_rand_str(5)
            test_addproduct.addproduct('1', '1', pname, stitle, '1')
        with allure.step('4，回到首页'):
            # 点击菜单
            test_addproduct.click_element(test_addproduct.home_button)
        with allure.step('5,进入商品列表并获取列表第一个商品'):
            # 点击商品列表页面
            test_productlistpage = test_mainpage.goto_productlistpage()
            expected_name = test_productlistpage.get_first_productname()
        with allure.step('6,断言'):
            ##断言-商品列表第一个商品
            assert expected_name == pname


if __name__ == '__main__':
    pytest.main(['test_addproduct.py','-sq','--alluredir',f'{report_path}','--clean-alluredir'])
    os.system(f'allure serve {report_path}')

