# -*- coding:utf-8 -*-
# @Time : 2022/6/8 20:43
# Auther : shenyuming
# @File : productListPage.py
# @Software : PyCharm
from common.basePage import BasePage


class ProductListPage(BasePage):
    """
    获得商品列表的第一个商品的名称
    """
    def get_first_productname(self):
        return self.get_element_text(self.first_productname)