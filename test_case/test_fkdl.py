# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: 招行付款代理产品UI自动化测试脚本
@time: 2023/10/26 17:34
"""
import logging
import sys

import allure
import pytest

from base1.base_util import BaseUtil
from common.assert_util import AssertUtil
from common.logger_util import Logger
from page_base.fkdl_dtl_page import FkdlDtlPage
from page_base.login_page import LoginPage

log=Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)

@allure.feature('保理E产品功能验证')
class TestFkdl(BaseUtil):

    @allure.title("成功进入保理E产品操作页面")
    def test_fkdldtl_01(self):
        log.logger.info('***********执行用例：'+sys._getframe().f_code.co_name+'开始****************')
        lg=LoginPage(self.driver)
        lg.login_success_eshop('child','13475475547','230516')
        fdp=FkdlDtlPage(self.driver)
        fdp.goto_fkdlDtlPage()
        actual=fdp.check_applybtl_success()
        fdp.assertEqual("保理E",actual)
        log.logger.info('***********执行用例：' + sys._getframe().f_code.co_name + '结束****************')

    @allure.title("点击立即申请，登录账号未实名认证")
    def test_fkdldtl_02(self):
        log.logger.info('***********执行用例：' + sys._getframe().f_code.co_name + '开始****************')
        lg = LoginPage(self.driver)
        lg.login_success_eshop('child', '17754856657', '230516')
        fdp = FkdlDtlPage(self.driver)
        fdp.goto_fkdlDtlPage()
        actual=fdp.check_not_auth_warn()
        fdp.assertEqual("请先完成实名认证", actual)
        log.logger.info('***********执行用例：' + sys._getframe().f_code.co_name + '结束****************')

    @allure.title("点击立即申请，未进行登录")
    def test_fkdldtl_03(self):
        log.logger.info('***********执行用例：' + sys._getframe().f_code.co_name + '开始****************')
        fdp = FkdlDtlPage(self.driver)
        fdp.goto_fkdlDtlPage()
        actual = fdp.cheak_not_login_warn()
        fdp.assertEqual("系统检测到您尚未登录，或者登录已过期，请先登录以继续操作", actual)
        log.logger.info('***********执行用例：' + sys._getframe().f_code.co_name + '结束****************')

    @allure.title("点击立即申请，登录账号未同意数据授权")
    def test_fkdldtl_04(self):
        log.logger.info('***********执行用例：' + sys._getframe().f_code.co_name + '开始****************')
        lg = LoginPage(self.driver)
        lg.login_success_eshop('child', '17754856658', '230516')
        fdp = FkdlDtlPage(self.driver)
        fdp.goto_fkdlDtlPage()
        actual = fdp.check_license_agreement()
        fdp.assertEqual("保理E数据授权协议", actual)
        log.logger.info('***********执行用例：' + sys._getframe().f_code.co_name + '结束****************')

if __name__ == '__main__':
    pytest.main()