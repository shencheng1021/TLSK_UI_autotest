# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: 添加实名认证模块自动化测试验证
@time: 2023/9/11 9:34
"""
import logging

import pytest

from base1.base_util import BaseUtil
from common.logger_util import Logger
from page_base.auth_page import AuthBage
from page_base.login_page import LoginPage
import allure

log=Logger(__name__,CmdLevel=logging.INFO, FileLevel=logging.INFO)

@allure.feature('实名认证功能验证')
class TestAuth(BaseUtil):

    @allure.title('认证成功')
    @pytest.mark.usefixtures('auth_initialization')
    def test_auth_01(self):
        '''
        实名认证成功
        :return:
        '''
        lg=LoginPage(self.driver)
        lg.login_success_eshop('child','17754756654','230516')
        log.logger.info("********************登录结束，进入实名认证操作**********************")
        ah=AuthBage(self.driver)
        ah.auth_business_shop('营业执照.jpg',"北京市","北京市","朝阳区")
        ah.auth_lagal_shop('身份证正面.jpg','身份证背面.jpg',"17754254414")
        ah.auth_contactperson_shop('身份证正面.jpg','身份证背面.jpg',"17754254414")
        ah.auth_source_shop()
        ah.auth_submit('1')
        ah.goto_auth_shop()
        assert ah.check_point() == "已认证"
        log.logger.info("***************实名认证测试完成**********************")

    @allure.title('认证失败：营业执照号重复认证')
    def test_auth_02(self):
        '''
        认证失败：营业执照号重复认证
        :return:
        '''
        log.logger.info("********************登录开始**********************")
        lg = LoginPage(self.driver)
        lg.login_success_eshop('child', '17754756655', '230516')
        log.logger.info("********************登录结束，进入实名认证操作*********************")
        ah = AuthBage(self.driver)
        ah.auth_business_shop('营业执照.jpg', "北京市", "北京市", "朝阳区")
        ah.auth_lagal_shop('身份证正面.jpg', '身份证背面.jpg', "17754254414")
        ah.auth_contactperson_shop('身份证正面.jpg', '身份证背面.jpg', "17754254414")
        ah.auth_source_shop()
        ah.auth_submit('1')
        assert ah.check_point_2() == "营业执照号已认证其它企业,请勿重复认证多个企业"
        log.logger.info("***************实名认证测试完成**********************")



if __name__ == '__main__':
    pytest.main()
