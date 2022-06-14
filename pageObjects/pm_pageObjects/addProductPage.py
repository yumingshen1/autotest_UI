# -*- coding:utf-8 -*-
# @Time : 2022/6/8 20:42
# Auther : shenyuming
# @File : addProductPage.py
# @Software : PyCharm
from common.basePage import BasePage


class AddProductPage(BasePage):
    def addproduct(self,kid1,kid2,pname,stitle,idx1):
        #点击商品分类
        self.click_element(self.product_kind_select,desc='商品分类')
        #选择一级分类 , 处理一级选择
        self.product_kind_select_index1[-1] = self.product_kind_select_index1[-1].format(kid1)
        self.click_element(self.product_kind_select_index1,desc='一级分类')
        #选择二级分类 , 处理二级选择
        self.product_kind_select_index2[-1] = self.product_kind_select_index2[-1].format(kid2)
        self.click_element(self.product_kind_select_index2,desc='二级分分类')
        #输入商品名称
        self.input_text(self.product_name,pname,desc='商品名称')
        #输入副标题
        self.input_text(self.product_subtitle,stitle,desc='副标题')
        #点击商品品牌
        self.click_element(self.product_brand_select,desc='商品品牌')
        #点击品牌一级列表
        self.product_brand_select_idx[-1] = self.product_brand_select_idx[-1].format(idx1)
        self.click_element(self.product_brand_select_idx,desc='品牌一级列表')
        #点击下一步，填写促销商品
        self.click_element(self.next_commodity_promotion_btn)
        #点击下一步，填写商品属性
        self.click_element(self.next_product_attribute_btn)
        #点击下一步，选择商品关联
        self.click_element(self.netxt_product_related_btn)
        #完成，提交商品
        self.click_element(self.comple_button)
        #确定
        self.click_element(self.subit_button)

