# -*- coding:utf-8 -*-
# @Time : 2022/6/10 21:38
# Auther : shenyuming
# @File : test_login_2.py
# @Software : PyCharm
from common.elements import Elements
from configs.env import ENV
from pageObjects.loginPage import LoginPage
from test_datas.login_datas import *
import pytest,allure,os,pytest_assume
from time import sleep
from utils.handle_path import test_datas_path,report_path
from utils.handle_yaml import get_yaml_data

@allure.epic('保利商城')
@allure.feature('登录模块')
class Test_Login():
    ## 五条用例混合
    test_all_data_v2 = get_yaml_data(test_datas_path / 'login_all_data_v2.yml')
    @pytest.mark.parametrize('casename,username,password,locator,excepted',test_all_data_v2)
    @allure.story('登录测试用例')
    @allure.title('{casename}')
    def test_login_all(self,casename,username,password,locator,excepted):
        '''
        失败用例
        :return:
        '''
        with allure.step('1,打开网页'):
            test_login = LoginPage()
            test_login.open_url(ENV.POLLY_URL)
        with allure.step('2,登录页面'):
            test_login.login_polly(username, password)
        with allure.step('3,断言{locator}值是否等于{excepted}'):

            # with pytest.assume: #pytest.assume 断言失败继续run
            #     assert test_login.get_element_text(locator) == excepted

              test_login.assert_excepted_data(locator,excepted)

        with allure.step('4,断言后的处理，某些用例需要退出'):
            ## 前两条登陆成功需要退出，加判断，driver.current_url 当前url
            if test_login.driver.current_url == ENV.POLLU_URL_PAGE:
                # 用户中心
                test_login.click_element(Elements.PERSONAL_CENTER_BUTTON)
                # 退出
                test_login.click_element(Elements.LOGOUT_BUTTON)  # 目前有bug
                sleep(0.5)


if __name__ == '__main__':
    # pytest.main(['-sv','-k 002',__file__])
    # pytest.main(['-sv', '--allure-severities=normal', __file__]) # 执行--allure-severities=normal等级的用例
    pytest.main(['test_login_2.py','-sq'])
    # pytest.main(['-sv',__file__,'--alluredir',f'{report_path}','--clean-alluredir'])
    # os.system(f'allure serve {report_path}')

