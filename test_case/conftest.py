# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: test
@time: 2022/4/13 9:34
"""
import time

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


@allure.step("初始化关联的OA信息")
@pytest.fixture(scope="function",autouse=False)
def oa_information_initialization():
    date=time.strftime("%Y%m%d",time.localtime(time.time()))
    sql="INSERT INTO `tjf_manage01`.`t_company_financing_amount_info` (`flow_code`, " \
       "`company`, `company_code`, `sub_company`, `sub_company_busi_lice_no`, `supplier`," \
       " `supplier_busi_lice_no`, `amount`, `bank`, `bank_verify_status`, `bank_code`, " \
       "`deleted`, `applied_date`, `apply_date`, `remark`, `create_time`, `update_time`) " \
       "VALUES ( '345666', '自动化测试', NULL, '中建西部建设股份有限公司', '916500007318073269', " \
       "'供应商新101', '51142329765987177D', 10000.00, '建设银行', 0, NULL, 0, "+date+", " \
       ""+date+", '手动补充数据', NOW(), NOW());"
    MysqlConnection('tjf_manage01').Operate(sql)



if __name__ == '__main__':
    oa_information_initialization()








@pytest.fixture()
def setup_func(request):
    request.info("测试的撒发生")


