# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: 砼联数科官网自动化测试
@description: 链接砼联数科测试环境数据库进行操作得数据库类
@time: 2022/4/24 13:56
"""
import logging

import pymysql

from common.logger_util import Logger

log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)

class MysqlConnection(object):
    '''
    mysql操作类，对mysql数据库进行增删改查
    '''

    def __init__(self,database):
        self.connection=pymysql.Connect(
            host='172.24.100.68',
            user='tlsktest',
            password='tlsk@testadmin123',
            port=3306,
            db=database,
            charset='utf8'
        )
        self.connection.autocommit(True)
        self.cursor=self.connection.cursor()

    def QueryAll(self,sql):
        #查询所有数据
        #数据库断开即重连
        log.logger.info('执行查询sql语句：'+sql)
        self.reConnnect()
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def QueryMany(self,sql,n):
        # 查询几条数据
        # 数据库断开即重连
        log.logger.info('执行查询sql语句：' + sql)
        self.reConnnect()
        self.cursor.execute(sql)
        return self.cursor.fetchmany(n)

    def QueryOne(self,sql):
        # 查询一条数据
        # 数据库断开即重连
        log.logger.info('执行查询sql语句：' + sql)
        self.reConnnect()
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def reConnnect(self):
        #重连机制
        try:
            self.connection.ping()
        except:
            self.connection.connect()

    def Operate(self,sql,params=None,DML=True):
        '''
        数据库操作：增删改查
        DML:insert/update/delete
        '''
        log.logger.info('执行sql语句：' + sql)
        try:
            self.reConnnect()
            self.cursor.execute(sql,params)
            self.connection.commit()
        except Exception as e:
            if DML:
                #涉及到DML操作时，若抛异常需要回滚
                self.connection.rollback()
                print(e)

    def __del__(self):
        """
        MysqlConnection实例对象被释放时调用此方法，用于关闭cursor和connection连接
        """
        self.cursor.close()
        self.connection.close()


if __name__ == '__main__':
    tjf_mange01 = MysqlConnection('tjf_manage01')
    tjf_mange01.Operate("DELETE  FROM `tjf_manage01`.`t_business_identify`  WHERE `busi_lice_no`='91130609MABN36NQXR'")
    tjf_mange01.Operate("DELETE  FROM `tjf_manage01`.`t_trader`  WHERE `name`='河北恩帅贸易有限公司'")
