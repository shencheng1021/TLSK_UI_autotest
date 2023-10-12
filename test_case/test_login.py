# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: test
@time: 2022/4/13 9:34
"""

from common.excel_util import ExcelUtil
from page_base.login_page import LoginPage
from base1.base_util import BaseUtil
import pytest
import allure



@allure.epic('砼联数科官网登录模块自动化测试')
@allure.feature('短信登录方式登录验证')
class TestLogin(BaseUtil):

    @allure.title('输入手机号与验证码进行登录验证')
    @pytest.mark.parametrize('index,casename,username,checkcode,result',ExcelUtil().excel_read('login_data'))
    def test_login_01(self,index,casename,username,checkcode,result):
        self.mylogger.info('********登录测试开始,输入用户名：'+str(username)+'输入验证码:'+str(checkcode)+'******')
        self.driver.implicitly_wait(10)
        lp=LoginPage(self.driver)
        lp.slmode_eshop('child',username,checkcode)

        if index == 1:
            lp.goto_merchants_center()
            assert  lp.check_point_shop() == result
        elif index == 2 or index == 3 or index == 4:
            assert lp.loginfail_check_shop(lp.username_failwarn_loc) == result
        elif index == 5:
            assert lp.loginfail_check_shop(lp.checkcode_null_loc) == result
        else:
            assert lp.loginfail_check_shop(lp.checkcode_fail_loc) == result

        self.mylogger.info('********登录测试结束，测试结果：********')


if __name__ == '__main__':
    pytest.main(['-vs'])
