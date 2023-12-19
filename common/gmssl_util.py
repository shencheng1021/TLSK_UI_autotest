# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: test
@time: 2022/4/13 9:34
"""
import json
import logging

import requests
from common.logger_util import Logger
from common.yaml_util import YamlUtil
import allure

log=Logger(__name__,CmdLevel=logging.INFO, FileLevel=logging.INFO)

class GmSsl:

    @allure.step("对接口返回的密文进行解密")
    def gmssh_decode(self,data):
        log.logger.info('请求解密接口开始，解密数据为：%s' % data)
        url = "http://172.24.100.74:9921/decrypt"
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Host": "172.24.100.74:9921"
        }
        rep = requests.request("post", url=url,data=data, headers=headers)
        log.logger.info("解密结果为：%s" % rep.json())
        return rep.json()


    @allure.step("对数据进行加密")
    def gmssh_encrypt(self,data):
        data=json.dumps(data)
        log.logger.info('请求加密接口开始，加密数据为：%s' % str(data))
        url='http://172.24.100.74:9921/encrypt'
        headers = {
            "Content-Type": "application/json;charset=UTF-8",
            "Host": "172.24.100.74:9921"
        }
        rep = requests.request("post",url=url,data=data,headers=headers)
        log.logger.info('加密结果为：%s' % rep.json())
        return rep.json()

    @allure.step("获取解密报文中的token，并将token保存到指定yaml文件中")
    def set_token(self,key,data):
        head=GmSsl().gmssh_decode(data)
        token=head['token']
        YamlUtil().write_extract_yaml({'token_'+key: token})
