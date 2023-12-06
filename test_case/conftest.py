# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: test
@time: 2022/4/13 9:34
"""
import logging
import os
import time

import pytest
from selenium import webdriver

from base1.base_page import BasePage
from base1.base_util import BaseUtil
from common.logger_util import Logger
from common.mysql_util import MysqlConnection
import allure

from common.yaml_util import YamlUtil

log=Logger(__name__,CmdLevel=logging.INFO, FileLevel=logging.INFO)

@allure.step('初始化实名认证信息')
@pytest.fixture(scope='function',autouse=False)
def auth_initialization():

    sql1="DELETE  FROM `tjf_manage01`.`t_business_identify`  WHERE `busi_lice_no`='91130609MABN36NQXR'"
    sql2="DELETE  FROM `tjf_manage01`.`t_trader`  WHERE `name`='河北恩帅贸易有限公司'"
    MysqlConnection('tjf_manage01').Operate(sql1)
    MysqlConnection('tjf_manage01').Operate(sql2)
    log.logger.info('***********初始化实名认证信息完成************')


@allure.step("初始化供应商信息")
@pytest.fixture()
def supplier_initialization():
    sql="DELETE FROM tjf_user01.t_core_enterprise_supplier WHERE core_number = " \
        "'TN2022042700010413' AND supplier_number = 'TN2023020600025803'"
    MysqlConnection('tjf_user01').Operate(sql)
    log.logger.info('***********初始化供应商信息完成************')

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
    log.logger.info('***********初始化关联的OA信息完成************')

@allure.step("初始化企业信息")
@pytest.fixture(scope='class',autouse=True)
def business_information():
    YamlUtil().clean_extract_yaml()
    log.logger.info('***********清除extract.yaml文件内容完成************')
    date=time.strftime('%Y%m%d%H%M%S',time.localtime())
    business_name='测试企业'+date
    business_code='YYZZ'+date
    data={'companyName' : business_name,'busiLiceNo':business_code}
    YamlUtil().write_extract_yaml(data)
    log.logger.info('***********初始化企业信息完成************')

# @allure.step("清除extract.yaml文件内容")
# @pytest.fixture(scope='class',autouse=True)
# def clean_extract():
#     YamlUtil().clean_extract_yaml()
#     log.logger.info('***********清除extract.yaml文件内容完成************')




# driver = None
#
# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     res = outcome.get_result()
#     if res.when == "call" and res.failed:
#         mode = "a" if os.path.exists("failures") else "w"
#         with open("failures", mode) as f:
#             # let's also access a fixture for the fun of it
#             if "tmpdir" in item.fixturenames:
#                 extra = " (%s)" % item.funcargs["tmpdir"]
#             else:
#                 extra = ""
#             f.write(res.nodeid + extra + "\n")
#         # 添加allure报告截图
#         if hasattr(driver, "get_screenshot_as_png"):
#             with allure.step('添加失败截图...'):
#                 allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
#
#
# @pytest.fixture(scope='session')
# def browser():
#     global driver
#     if driver is None:
#         # chromedriver 路径已添加到系统环境变量中，所以此处可省略chromedriver路径参数
#         driver = webdriver.Chrome()
#         driver.implicitly_wait(10)
#         driver.get('http://172.24.100.75:10006/#/login')
#         driver.maximize_window()
#         log.logger.info('************************starting run test cases************************')
#     yield driver
#     driver.quit()
#     log.logger.info('************************test case run completed************************')



if __name__ == '__main__':
    auth_initialization()
