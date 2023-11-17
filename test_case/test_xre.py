# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: 信融E产品UI自动化测试脚本
@time: 2023/11/13 10:29
"""
import logging

import allure
import pytest

from base1.base_util import BaseUtil
from common.assert_util import AssertUtil
from common.logger_util import Logger
from page_base.login_page import LoginPage
from page_base.xre_dtl_page import XreDtlPage

log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)

@allure.feature("信融E产品UI自动化测试")
class Test_Xre(BaseUtil):

    @allure.story('信融E产品详情测试')
    @allure.title('验证未登录提示信息')
    def test_not_lg_tips(self):
        log.logger.info('**********验证未登录提示信息,测试开始**********')
        xreDtl=XreDtlPage(self.driver)
        xreDtl.goto_xreDtl_page()
        xreDtl.click_applyBtl()
        actual=xreDtl.check_whether_lg()
        xreDtl.assertEqual(True,actual)
        log.logger.info('**********验证未登录提示信息,测试结束**********')

    @allure.story('信融E产品详情测试')
    @allure.title('验证未实名认证提示信息')
    def test_not_auth_tips(self):
        log.logger.info('**********验证未实名认证提示信息,测试开始**********')
        lg=LoginPage(self.driver)
        lg.login_success_eshop('child','17754856657','230516')
        xreDtl = XreDtlPage(self.driver)
        xreDtl.goto_xreDtl_page()
        xreDtl.click_applyBtl()
        actual=xreDtl.check_whether_auth()
        xreDtl.assertEqual(True,actual)
        log.logger.info('**********验证未实名认证提示信息,测试结束**********')

    @allure.story('信融E产品详情测试')
    @allure.title('验证是否弹出信融E数据授权协议')
    def test_not_agreement_alert(self):
        log.logger.info('**********验证是否弹出信融E数据授权协议,测试开始**********')
        lg = LoginPage(self.driver)
        lg.login_success_eshop('child', '17754856658', '230516')
        xreDtl = XreDtlPage(self.driver)
        xreDtl.goto_xreDtl_page()
        xreDtl.click_applyBtl()
        actual=xreDtl.check_whether_agreement()
        xreDtl.assertEqual(True, actual)
        log.logger.info('**********验证是否弹出信融E数据授权协议,测试结束**********')

    @allure.story('信融E产品详情测试')
    @allure.title('验证核心企业账户进入信融E产品操作页面')
    def test_goto_xre_product(self):
        log.logger.info('**********验证核心企业账户进入信融E产品操作页面,测试开始**********')
        lg = LoginPage(self.driver)
        lg.login_success_eshop('child', '17569854475', '230516')
        xreDtl = XreDtlPage(self.driver)
        xreDtl.goto_xreDtl_page()
        xreDtl.click_applyBtl()
        actual=xreDtl.check_product_name()
        xreDtl.assertEqual('信融E', actual)
        log.logger.info('**********验证核心企业账户进入信融E产品操作页面,测试结束**********')



if __name__ == '__main__':
    pytest.main()