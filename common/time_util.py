# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: 时间处理的公共模块
@time: 2022/4/13 9:34
"""
import time
from datetime import date, datetime, timedelta

#获取格式化后的当前日期
strdate=time.strftime("%Y%m%d",time.localtime(time.time()))

#获取格式化后的当前时间
strtime=time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))

def after_time(dates):
    now = datetime.now()
    delta = timedelta(days=dates)  # days可以为正负数，当为负数时，n_days_after 与n_days_forward 的值与正数时相反；
    n_days_after = now + delta
    time=n_days_after.strftime('%Y-%m-%d')
    return time

print(after_time(365))



