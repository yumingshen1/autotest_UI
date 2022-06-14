# -*- coding:utf-8 -*-
# @Time : 2022/6/6 14:57
# Auther : shenyuming
# @File : handle_yaml.py
# @Software : PyCharm

from utils.handle_path import test_datas_path, common_path
import yaml
from pprint import pprint

def get_yaml_data(yaml_file):
    with open(yaml_file,'r',encoding='utf-8') as f:
        return yaml.safe_load(f.read())

if __name__ == '__main__':
    pprint(get_yaml_data(test_datas_path / 'login_failed_data.yml'))
    pprint(get_yaml_data(common_path /'allelements.yml'))