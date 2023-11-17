# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: 测试案例断言的公共类
@time: 2023/10/25 17:34
"""
import logging

from common.logger_util import Logger

log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)

class AssertUtil:

    def assertEqual(self,expectation,actual):
        try:
            assert expectation == actual
        except AssertionError as e:
            log.logger.error("断言失败！预期结果：%s，实际结果：%s" % (expectation,actual),exc_info=True)
            raise e
        else:
            log.logger.info("断言成功！预期结果：%s，实际结果：%s" % (expectation,actual))

    def assertIn(self,expectation,actual):
        try:
            assert expectation in actual
        except AssertionError as e:
            log.logger.error("断言失败！预期结果：%s not in 实际结果：%s" % (expectation,actual),exc_info=True)
            raise e
        else:
            log.logger.info("断言成功！预期结果：%s in 实际结果：%s" % (expectation,actual))
