# -*- coding:utf-8 -*-
# @Time : 2022/6/8 16:47
# Auther : shenyuming
# @File : mainPage.py
# @Software : PyCharm

'''
商品添加页面
'''
from common.basePage import BasePage  #导入基类方法
from pageObjects.pm_pageObjects.addProductPage import AddProductPage
from pageObjects.pm_pageObjects.brandManagePage import BrandManagePage
from pageObjects.pm_pageObjects.productListPage import ProductListPage


class MainPage(BasePage):
    ## 找到添加商品页面
    def goto_addproductpage(self):
        #点击左上角菜单栏
        # self.click_element(self.home_button,desc='点击菜单栏')
        #点击商品管理
        self.click_element(self.shop_guanli,desc='点击商品管理')
        #点击添加商品
        self.click_element(self.shop_add,desc='点击添加商品')

        return AddProductPage()

    ## 商品列表页面
    def goto_productlistpage(self):
        #点击菜单
        self.click_element(self.home_button, desc='点击菜单栏')
        #点击商品列表
        self.click_element(self.shop_list)

        return ProductListPage()

    ## 品牌管理
    def goto_branmainpage(self):
        #点击商品管理
        self.click_element(self.shop_guanli)
        #点击品牌管理
        self.click_element(self.shop_anage)

        return BrandManagePage()



if __name__ == '__main__':

    '''
    登录和商品链接方法
    '''
    from pageObjects.loginPage import LoginPage
    test_flage = 2
    if test_flage ==3:
        m1=LoginPage().open_loginpage('http://120.55.190.222:38090/#/login').login_polly('鸿星尔克286', '123456')
        m1.goto_addproductpage()

    if test_flage ==2:
        lp = LoginPage()
        lp.open_loginpage('http://120.55.190.222:38090/#/login')
        m1 = lp.login_polly('鸿星尔克286', '123456')   #LoginPage已返回MainPage实例
        m1.goto_addproductpage()

    if test_flage ==1:
        lp = LoginPage()
        lp.open_loginpage('http://120.55.190.222:38090/#/login')
        lp.login_polly('鸿星尔克286','123456')
        m = MainPage()
        m.goto_addproductpage()





