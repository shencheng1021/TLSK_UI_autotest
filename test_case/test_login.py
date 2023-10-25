# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: test
@time: 2022/4/13 9:34
"""
import logging

from common.assert_util import AssertUtil
from common.excel_util import ExcelUtil
from common.logger_util import Logger
from page_base.login_page import LoginPage
from base1.base_util import BaseUtil
import pytest
import allure


log=Logger(__name__,CmdLevel=logging.INFO, FileLevel=logging.INFO)

@allure.epic('砼联数科官网登录模块自动化测试')
@allure.feature('短信登录方式登录验证')
class TestLogin(BaseUtil):

    @allure.title('输入手机号与验证码进行登录验证')
    @pytest.mark.parametrize('index,casename,username,checkcode,result',ExcelUtil().excel_read('login_data'))
    def test_login_01(self,index,casename,username,checkcode,expectation):
        log.logger.info('********登录测试开始,输入用户名：'+str(username)+'输入验证码:'+str(checkcode)+'******')
        self.driver.implicitly_wait(10)
        lp=LoginPage(self.driver)
        lp.slmode_eshop('child',username,checkcode)

        if index == 1:
            lp.goto_merchants_center()
            AssertUtil().assertEqual(expectation,lp.check_point_shop())
            #assert  lp.check_point_shop() == expectation
        elif index == 2 or index == 3 or index == 4:
            AssertUtil().assertEqual(expectation, lp.loginfail_check_shop(lp.username_failwarn_loc))
            #assert lp.loginfail_check_shop(lp.username_failwarn_loc) == expectation
        elif index == 5:
            AssertUtil().assertEqual(expectation,lp.loginfail_check_shop(lp.checkcode_null_loc))
            #assert lp.loginfail_check_shop(lp.checkcode_null_loc) == expectation
        else:
            AssertUtil().assertEqual(expectation,lp.loginfail_check_shop(lp.checkcode_fail_loc))
            #assert lp.loginfail_check_shop(lp.checkcode_fail_loc) == expectation

        log.logger.info('********登录测试结束，测试结果：********')


if __name__ == '__main__':
    pytest.main(['-vs'])
