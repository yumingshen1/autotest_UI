# -*- coding:utf-8 -*-
# @Time : 2022/6/5 22:21
# Auther : shenyuming
# @File : loginPage.py
# @Software : PyCharm
from common.basePage import BasePage
from common.elements import Elements
from pageObjects.mainPage import MainPage
import warnings

class LoginPage(BasePage):

    def open_loginpage(self,url):
        self.open_url(url)
        return self     ## 返回自己--可用于链式调用

    def login_polly_old(self,username,password):
        warnings.warn('这个方法太老了，请使用input_text来代替', DeprecationWarning, stacklevel=2)
        self.input_text(Elements.USERNAME_INPUT,username,desc='用户名')
        self.input_text(Elements.PASSWORD_INPUT,password,desc='用户密码')
        self.click_element(Elements.LOGIN_BUTTON)


    #basePage页面初始化了yml值，self.username_input  类属性
    def login_polly(self,username,password):
        self.input_text(self.username_input,username,desc='用户名')
        self.input_text(self.password_input,password,desc='用户密码')
        self.click_element(self.login_button)

        return MainPage()   # 返回商品页面实例，是将登录页面和商品页面链接在一起的方法

if __name__ == '__main__':
    l = LoginPage()
    print(l.username_input)