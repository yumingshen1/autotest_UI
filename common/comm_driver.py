# -*- coding:utf-8 -*-
# @Time : 2022/6/5 16:41
# Auther : shenyuming
# @File : comm_driver.py
# @Software : PyCharm

from selenium import webdriver
from time import sleep
from configs.env import ENV

class Single(object):
    '''
        单例模式，设计模式，直接用，
        理解__init__ __new__
        log，自动化浏览器，配置器，使用
    '''
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

class Single1(object):
    def __new__(cls, *args, **kwargs):
        if hasattr(cls,'_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance


class Comm_driver(Single):
    driver = None   ##浏览器做标记，
    def get_driver(self,broswer_type=ENV.BROWSER_TYPE,headless_flage = ENV.HEADLESS_FLAGE):
        """
        :param broswer_type: 浏览器类型
        :param headless_flage: 用于来使用无头浏览器还是非无头浏览器
        :return:
        """
        if self.driver is None:#浏览器如果没打开，就执行打开
            if not headless_flage:

                if broswer_type == 'chrome':
                    self.driver = webdriver.Chrome()
                elif broswer_type =='firefox':
                    self.driver = webdriver.firefox()
                else:
                    raise print(f'输入失败{broswer_type}')

            else:
                if broswer_type == 'chrome':
                    _options = webdriver.ChromeOptions()
                    _options.s('--headless')
                    self.driver = webdriver.Chrome(options=_options)
                elif broswer_type == 'firefox':
                    _options = webdriver.FirefoxOptions()
                    _options.add_argument('--headless')
                    self.driver = webdriver.Firefox(options=_options)
                else:
                    raise print({f'输入失败{broswer_type}'})

            self.driver.maximize_window()
            print(self.driver.name)
            print(self.driver.title)
            self.driver.implicitly_wait(ENV.IMPLICITLY_WAIT_TIME) #隐式等待时间

        return self.driver      #如果已打开直接返回driver


if __name__ == '__main__':
    test_flage = 3
    if test_flage ==3:
        id3 = Comm_driver().get_driver()
        id4 = Comm_driver().get_driver()
        print(id(id3)==id(id4))

    if test_flage ==2:
        id1 = Comm_driver()
        id2 = Comm_driver()
        print(id(id1)==id(id2))

    if test_flage ==1:
        Comm_driver().get_driver()