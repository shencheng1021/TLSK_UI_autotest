# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: 接口调用的公共方法
@time: 2022/4/13 9:34
"""
import logging

import requests

from common.logger_util import Logger

log=Logger(__name__,CmdLevel=logging.INFO, FileLevel=logging.INFO)

class RequestUtil:

    session=requests.session()

    def send_request(self,method,url,**kwargs):
        log.logger.info("请求地址:%s" % str(url))
        log.logger.info("请求方式:%s" % str(method))
        dh=dict(**kwargs)
        for item in dh.items():
            if item[0]== 'data' or item[0] == 'params' or item[0] == 'json':
                log.logger.info('请求测试数据为：%s' % item[1])
            if item[0] == 'headers':
                log.logger.info('请求头为：%s' % item[1])
        try:
            rep=RequestUtil().session.request(method,url,**kwargs)
        except Exception as e:
            log.logger.exception('接口请求失败',exc_info=True)
            raise e
        else:
            log.logger.info("请求结果状态码：[%s]" % rep.status_code)
            log.logger.info('接口请求结果为：%s' % rep.text)
            return rep.text
