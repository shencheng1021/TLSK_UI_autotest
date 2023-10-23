# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: 时间处理的公共模块
@time: 2022/4/13 9:34
"""
import time


class TimeUtil:

    def strtime(self):
        nowtime=time.strftime("%Y%m%d",time.localtime(time.time()))
        return nowtime


if __name__ == '__main__':
    tt=TimeUtil().strtime()
    print(time.localtime(time.time()))
    print(tt)