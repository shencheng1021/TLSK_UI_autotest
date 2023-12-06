# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: 读取yaml文件的工具类
@time: 2022/4/13 9:34
"""
import logging
import os

import yaml

from common import dir_util
from common.logger_util import Logger

log=Logger(__name__,CmdLevel=logging.INFO, FileLevel=logging.INFO)

class YamlUtil:

    #读取yaml文件中的内容
    def read_yaml(self,path,filename):
        try:
            with open(path+filename,mode='r',encoding='UTF-8') as file:
                value=yaml.load(stream=file,Loader=yaml.FullLoader)
        except Exception as e:
            log.logger.exception("读取%s文件中测试用例数据失败" % filename,exc_info=True)
            raise e
        else:
            log.logger.info("读取%s文件中测试用例数据成功" % filename)
            return value

    #读取extract文件中的数据
    def read_extract_yaml(self,key):
        log.logger.info("读取extract.yml文件中key为: %s 的数据" % key)
        try:
            with open(dir_util.sys_dir+'extract.yml',mode='r',encoding='UTF-8') as file:
                value=yaml.load(stream=file,Loader=yaml.FullLoader)
        except Exception as e:
            log.logger.exception('读取extract文件中key值为[%s]的数据失败' % key,exc_info=True)
            raise e
        else:
            log.logger.info('extract文件中key值为[%s]的数据为[%s]' % (key,value[key]))
            return value[key]
    #插入数据至extract文件中
    def write_extract_yaml(self,data):
        log.logger.info('写入extract.yaml文件内容，数据为：%s' % data)
        try:
            with open(dir_util.sys_dir+'extract.yml',mode='a',encoding='UTF-8') as file:
                yaml.dump(data=data,stream=file,allow_unicode=True)
        except Exception as e:
            log.logger.exception('写入extract.yaml文件失败',exc_info=True)
            raise e
        else:
            log.logger.info('写入extract.yaml文件成功')

    #清除extract文件数据
    def clean_extract_yaml(self):
        log.logger.info('清除extract.yaml文件内容')
        try:
            with open(dir_util.sys_dir+'extract.yml',mode='w',encoding='UTF-8') as file:
                file.truncate()
        except Exception as e:
            log.logger.exception('清除extract.yaml文件内容失败', exc_info=True)
        else:
            log.logger.info('清除extract.yaml文件内容成功')
if __name__ == '__main__':
    # data={'data':'2131231','gasda':'131233'}
    # YamlUtil().write_extract_yaml(data)
    #YamlUtil().clean_extract_yaml()
    res=YamlUtil().read_extract_yaml('data')
    print(res)