# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: 获取路径的公共类
@time: 2022/4/13 9:34
"""
import os
#获取当前系统路径
sys_dir=os.path.dirname(__file__).split('common')[0]

#获取测试数据的路径
testcase_dir=sys_dir+'data/'

#银联认证资料的路径
union_data_dir=sys_dir+'data/union_data/'

chrome_dir=sys_dir+'chrome/data'