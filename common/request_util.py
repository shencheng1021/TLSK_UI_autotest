# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: 接口调用的公共方法
@time: 2022/4/13 9:34
"""
import json
import logging

import requests

from common.gmssl_util import GmSsl
from common.logger_util import Logger
from common.yaml_util import YamlUtil

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

    def get_access_token(self,key,username):
        url='http://172.24.100.107:14000/auth/oauth/token?grant_type=mobile&source=PORTAL_CONFIG'
        method= 'post'
        headers={
            'enterCode': 'TLSK',
            'Authorization' : 'Basic dG9uZ0xpYW46dG9uZ0xpYW4=',
            'Content-Type' : 'application/x-www-form-urlencoded',
            'Host' : '172.24.100.107:14000'
        }
        data={
            'mobile': 'SMSCUST%40' + username,
            'code': '230516'
        }
        rep=RequestUtil().send_request(method=method,url=url,headers=headers,data=data)
        result = json.loads(rep)
        YamlUtil().write_extract_yaml({'access_token_'+key: result['access_token']})

    def get_token(self,key,username):
        RequestUtil().get_access_token(key,username)
        url='http://172.24.100.75:10006/expose/website/newLoginByCenter'
        method='get'
        accessToken=YamlUtil().read_extract_yaml('access_token_'+key)
        data={
            'Accept': 'application/json, text/plain, */*',
            'accessToken' : accessToken
        }
        rep=RequestUtil().send_request(method=method,url=url,params=data)
        result = json.loads(rep)
        GmSsl().set_token(key,result['data'])

if __name__ == '__main__':
    res=RequestUtil().get_token('issuer','13475475547')

