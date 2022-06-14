# -*- coding:utf-8 -*-
# @Time : 2022/6/11 14:46
# Auther : shenyuming
# @File : brandManagePage.py
# @Software : PyCharm
from common.basePage import BasePage


class BrandManagePage(BasePage):
    def get_curpage_brandnames(self):
        """
        获取当前页面所有品牌名
        :return:
        """
        return self.get_elements_text(self.all_brand_name_txt,desc='品牌名称')

    def search_brand(self,name):
        """
        搜索名称
        :param name:
        :return:
        """
        self.input_text(self.search_input,name)
        self.click_element(self.search_button)
