# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: test
@time: 2022/4/13 9:34
"""

import pytest


from common.mysql_util import MysqlConnection
import allure





@allure.step('初始化实名认证信息')
@pytest.fixture(scope='function',autouse=False)
def auth_initialization():

    sql1="DELETE  FROM `tjf_manage01`.`t_business_identify`  WHERE `busi_lice_no`='91130609MABN36NQXR'"
    sql2="DELETE  FROM `tjf_manage01`.`t_trader`  WHERE `name`='河北恩帅贸易有限公司'"
    MysqlConnection('tjf_manage01').Operate(sql1)
    MysqlConnection('tjf_manage01').Operate(sql2)


@pytest.fixture()
def supplier_initialization():
    sql="DELETE FROM tjf_user01.t_core_enterprise_supplier WHERE core_number = " \
        "'TN2022042700010413' AND supplier_number = 'TN2023020600025803'"
    MysqlConnection('tjf_user01').Operate(sql)







@pytest.fixture()
def setup_func(request):
    request.info("测试的撒发生")


