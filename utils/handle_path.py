# -*- coding:utf-8 -*-
# @Time : 2022/6/5 21:42
# Auther : shenyuming
# @File : handle_path.py
# @Software : PyCharm

from pathlib import Path

project_path = Path(__file__).parent.parent
configs_path = project_path / 'configs'
outfiles_path = project_path / 'outfiles'
logs_path = outfiles_path / 'logs'
screenshots_path = outfiles_path / 'screenshots'
test_datas_path = project_path / 'test_datas'
report_path = outfiles_path / 'report'
common_path = project_path / 'common'


if __name__ == '__main__':
    print(project_path)
    print(configs_path)
    print(outfiles_path)
    print(logs_path)
    print(screenshots_path)
    print(test_datas_path)
    print(report_path)
    print(common_path)

