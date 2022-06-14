# -*- coding:utf-8 -*-
# @Time : 2022/6/5 17:12
# Auther : shenyuming
# @File : basePage.py
# @Software : PyCharm
import traceback

import pytest

from common.comm_driver import Comm_driver
from common.elements import Elements
from configs.env import ENV
from test_datas.login_datas import *
import warnings
from time import strftime

from utils.handle_log import log
from utils.handle_path import screenshots_path, common_path
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils.handle_yaml import get_yaml_data


class BasePage():
    """
    打开浏览器
    打开网页
    点击元素
    输入内容
    获取元素内容
    """
    def __init__(self):
        #初始化 获取浏览器
        self.driver = Comm_driver().get_driver()

        ## 获取页面元素 - 1
        self.locators = get_yaml_data(common_path /'allelements.yml')
        ## 获取本页面元素 - 2    获取类名
        self.locators = get_yaml_data(common_path / 'allelements.yml')[self.__class__.__name__]
        ## 获取页面元素 -3 把元素名作为当前实例的属性
        for elemwnrname,locator in self.locators.items():
            setattr(self,elemwnrname,locator) #给self属性设置一个elementname属性值为locator

    def open_url(self,url):
        #打开地址
        self.driver.get(url)

    def get_element(self,locator,desc=None):
        """
        定位元素方法
        :param locator: 元素定位器
        :param desc:当前元素信息描述
        :return:
        """
        try:
            return WebDriverWait(self.driver,ENV.WEB_DRIVER_WAIT_TIMEOUT,ENV.POLL_FREQUENCY_TIME).until(EC.visibility_of_element_located(locator))
            # return self.driver.find_element(*locator)
        except: #如果错误，截图，打印日志
            #时间做为截图命名
            curtime = strftime('%Y%m%d%H%M%S')
            self.driver.save_screenshot(str(screenshots_path / F'{desc}{curtime}.png'))
            log.error(f'{desc}元素定位不到')
            log.error(traceback.format_exc())## 记录堆栈信息

    def input_text_old(self, locator, text,desc=None):
        """
        元素上输入内容
        :param locator:  元素
        :param text:  内容
        :param desc:当前元素信息描述
        :return:
        """
        #  warnings.warn  标记方法老了
        warnings.warn('这个方法太老了，请使用input_text来代替',DeprecationWarning,stacklevel=2)
        self.get_element(locator,desc=desc).send_keys(text)

    def input_text(self,locator,text,append=False,desc=None):
        """
        元素上输入内容
        :param locator:  元素
        :param text:  内容
        :param append 标记是否追加
        :param desc:当前元素信息描述
        :return:
        """
        if not append: #清空写入
            self.get_element(locator,desc=desc).clear()
            self.get_element(locator,desc=desc).send_keys(text)
        else: #追加
            self.get_element(locator,desc=desc).send_keys(text)

    def click_element(self,locator,desc=None):
        """
        点击元素
        :param locator: 元素
        :param desc:当前元素信息描述
        :return:
        """
        self.get_element(locator,desc=desc).click()

    def get_element_text(self,locator):
        """
        获取元素文本
        :param locator:
        :return:
        """
        return self.get_element(locator).text


    def assert_excepted_data(self,locator,except_data):
        """
        断言--登录
        :param local:
        :param except_data:
        :return:
        """
        with pytest.assume:
            # assert self.get_element(locator).text == except_data
            assert self.get_element_text(locator)==except_data

    def assert_excepted_page(self,actualresults,expectedresults):
        """
        断言-- 品牌管理
        :param actualresults:
        :param expectedresults:
        :return:
        """
        assert len(list(filter(lambda x: actualresults in x, expectedresults))) == len(expectedresults)


    def get_elements(self,locator,desc=None):
        """
        定义一组数据
        :param locator:
        :return:
        """
        try:
            mywait = WebDriverWait(self.driver,ENV.WEB_DRIVER_WAIT_TIMEOUT,ENV.POLL_FREQUENCY_TIME)
            return mywait.until(EC.visibility_of_all_elements_located(locator))
        except:
            curtime = strftime('%Y%m%d%H%M%S')
            self.driver.save_screenshot(str(screenshots_path / F'{desc}{curtime}.png'))
            log.error(f'{desc}元素定位不到')
            log.error(traceback.format_exc())  ## 记录堆栈信息

    def get_elements_text(self,locator,desc=None):
        """
        取一组内的数据
        :param locator:
        :param desc:
        :return:
        """
        # return self.get_elements(locator,desc)
        return [ele.text for ele in self.get_elements(locator,desc)] #列表生成式，取除每个数据

if __name__ == '__main__':
    test_basepage = BasePage()
    test_basepage.open_url(ENV.POLLY_URL)
    test_basepage.input_text(Elements.USERNAME_INPUT, USERNAME1,desc='用户名输入框')
    # test_basepage.input_text(Elements.PASSWORD_INPUT, PASSWORD1)
    # test_basepage.click_element(Elements.LOGIN_BUTTON)
