# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: 时间处理的公共模块
@time: 2022/4/13 9:34
"""
import time

#获取格式化后的当前日期
strdate=time.strftime("%Y%m%d",time.localtime(time.time()))

#获取格式化后的当前时间
strtime=time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))



