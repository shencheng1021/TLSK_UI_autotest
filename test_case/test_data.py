# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: test
@time: 2022/4/13 9:34
"""
import pytest

from base1.base_util import BaseUtil
from page_base.login_page import LoginPage


class TestDemo(BaseUtil):

    globals()

    def pageobject(self):
        lg = LoginPage(self.driver)

    def test_demo01(self):
        #lg = LoginPage(self.driver)
        self.lg.slmode_eshop('child', '17754856657', '230516')



if __name__ == '__main__':
    pytest.main()