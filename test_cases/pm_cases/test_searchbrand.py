# -*- coding:utf-8 -*-
# @Time : 2022/6/11 14:22
# Auther : shenyuming
# @File : test_searchbrand.py
# @Software : PyCharm

'''
跳转到品牌管理
'''
from time import sleep
import random

import allure
import pytest

@allure.epic('保利商城自动化')
@allure.feature('保利商城自动化--品牌管理')
class Test_searchduct:
    @allure.story('搜索品牌')
    def test_searchduct(self,fix_pm_cases):
        ##登录
        test_main = fix_pm_cases
        ## 点击品牌管理进入品牌管理页面
        test_drandmainpage = test_main.goto_branmainpage()
        #调用品牌管理页面的获得全部品牌方法，
        all_drandnames = test_drandmainpage.get_curpage_brandnames()
        # 随机捞一个数据  random.choice 随机获取一个
        choice_randname = random.choice(all_drandnames)
        ##搜索随机品牌
        test_drandmainpage.search_brand(choice_randname)
        ##搜索结果
        sleep(2)
        result_rabdnames = test_drandmainpage.get_curpage_brandnames()
        print('搜索结果',result_rabdnames)

        #断言 方法1
        # for i in result_rabdnames:
        #     if choice_randname not in i:
        #         assert False
        # else:
        #     assert True

        #断言 解法2  filter 过滤，
        # assert len(list(filter(lambda x:choice_randname in x,result_rabdnames))) == len(result_rabdnames)

        # 断言调用封装的解法2
        test_main.assert_excepted_page(choice_randname,result_rabdnames)

if __name__ == '__main__':
    pytest.main(['-sv',__file__])