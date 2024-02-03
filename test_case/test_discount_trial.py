# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: test
@time: 2022/4/13 9:34
"""
import logging

import allure

from base1.base_util import BaseUtil
from common.logger_util import Logger
from common.time_util import after_time
from page_base.discount_trial_page import DiscountTrialPage
from page_base.login_page import LoginPage

log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)

@allure.story('票据秒贴贴现询价')
class TestDiscountTrial(BaseUtil):

    @allure.title('贴现询价成功')
    def test_inquiry_success(self):
        log.logger.info('**********验证贴现询价成功,测试开始**********')
        lg=LoginPage(self.driver)
        lg.login_success_eshop('child','13730870050','230516')
        dt=DiscountTrialPage(self.driver)
        dt.goto_discount_page()
        dt.discount_inquiry(after_time(180),'招商银行')
        actual=dt.check_inquiry_res()
        dt.assertEqual('1.90%',actual)
        log.logger.info('**********验证贴现询价成功,测试结束**********')

    @allure.title('贴现询价失败')
    def test_inquiry_fail_01(self):
        log.logger.info('**********验证贴现询价失败,银行选择错误,测试开始**********')
        lg = LoginPage(self.driver)
        lg.login_success_eshop('child', '13730870050', '230516')
        dt = DiscountTrialPage(self.driver)
        dt.goto_discount_page()
        dt.discount_inquiry(after_time(180), '中国人民银行营业处')
        actual = dt.check_inquiry_fail_res()
        dt.assertEqual('同业银行客户号验证失败: , msg:', actual)
        log.logger.info('**********验证贴现询价失败，银行选择错误,测试结束**********')

    @allure.title('贴现询价成功')
    def test_inquiry_success_02(self):
        log.logger.info('**********验证贴现询价成功，到期日选择当前日期,测试开始**********')
        lg = LoginPage(self.driver)
        lg.login_success_eshop('child', '13730870050', '230516')
        dt = DiscountTrialPage(self.driver)
        dt = DiscountTrialPage(self.driver)
        dt.goto_discount_page()
        dt.discount_inquiry(after_time(0), '招商银行')
        actual = dt.check_inquiry_res()
        dt.assertEqual('2.20%', actual)
        log.logger.info('**********验证贴现询价成功，到期日选择当前日期,测试结束**********')

    @allure.title('贴现询价失败')
    def test_inquiry_fail_03(self):
        log.logger.info('**********验证贴现询价失败，贴现日期选择365天之后,测试开始**********')
        lg = LoginPage(self.driver)
        lg.login_success_eshop('child', '13730870050', '230516')
        dt = DiscountTrialPage(self.driver)
        dt.goto_discount_page()
        dt.discount_inquiry(after_time(365), '招商银行')
        actual = dt.check_inquiry_fail_res()
        dt.assertEqual('请求失败:code:EA3C051 , msg:EA3C051-到期日['+after_time(365)+']只能选择一年范围内', actual)
        log.logger.info('**********验证贴现询价失败，贴现日期选择365天之后,测试结束**********')










