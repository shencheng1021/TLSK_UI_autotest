# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: test
@time: 2022/4/13 9:34
"""
import time

import allure
import pytest

from base1.base_util import BaseUtil
from page_base.ext_page import ExtPage

from page_base.ext_sm_page import ExtSMPage
from page_base.login_page import LoginPage

@allure.feature('E信通产品自动化测试')
class TestExtdetails(BaseUtil):


    @allure.title("E信通二级页面，校验企业是否实名认证")
    def test_extdetails_01(self):
        self.mylogger.info("****************E信通二级页面，校验企业是否实名认证，测试开始****************")

        lg=LoginPage(self.driver)
        lg.slmode_eshop('child','17754856657','230516')
        EP=ExtPage(self.driver)
        EP.goto_ext_product_lg_s()
        actual=EP.check_pointt_auth_status()
        assert actual == "查询完成,未完成实名认证"
        self.mylogger.info("****************E信通二级页面，校验企业是否实名认证，测试结束****************")

    @allure.title("E信通二级页面，校验是否登录")
    def test_extdetails_02(self):
        self.mylogger.info("****************E信通二级页面，校验是否登录，测试开始****************")
        EP=ExtPage(self.driver)
        EP.goto_ext_product_lg_f()
        actual=EP.check_point_not_login()
        assert actual == "系统检测到您尚未登录，或者登录已过期，请先登录以继续操作"
        self.mylogger.info("****************E信通二级页面，校验是否登录，测试结束****************")

    @allure.title("E信通二级页面，校验授权协议弹出窗")
    def test_extdetails_03(self):
        self.mylogger.info("****************E信通二级页面，校验授权协议弹出窗，测试开始****************")
        lg=LoginPage(self.driver)
        lg.slmode_eshop('child','17754856658','230516')
        EP = ExtPage(self.driver)
        EP.goto_ext_product_lg_s()
        actual=EP.check_point_license_agreement()
        assert actual == "E信通业务合作协议"
        self.mylogger.info("****************E信通二级页面，校验授权协议弹出窗，测试结束****************")

    @allure.title("核心企业成功进入E信通产品操作页面")
    def test_extsupplier_04(self):
        self.mylogger.info('**********核心企业成功进入E信通产品操作页面,测试开始*********')
        lg=LoginPage(self.driver)
        lg.slmode_eshop('child','17754124411','230516')
        EP=ExtPage(self.driver)
        EP.goto_ext_product_lg_s()
        Ext_sm=ExtSMPage(self.driver)
        actual=Ext_sm.check_supplier_manage()
        self.mylogger.info("检点点打印："+actual)
        assert actual == "联系人姓名"
        self.mylogger.info("**********核心企业成功进入E信通产品操作页面,测试结束*********")

    @allure.title("新增供应商成功")
    @pytest.mark.usefixtures('supplier_initialization')
    def test_extsupplier_05(self):
        self.mylogger.info('********新增供应商,测试开始**********')
        lg = LoginPage(self.driver)
        lg.slmode_eshop('child', '17754124411', '230516')
        ext_sm=ExtSMPage(self.driver)
        ext_sm.goto_eChannelPage()
        ext_sm.switch_sm_menu()
        ext_sm.click_add_supplier()
        ext_sm.alert_input_supplier_name("重庆帆舟运输有限公司")
        ext_sm.alert_select_supplier_name()
        ext_sm.select_supplier_name()
        ext_sm.alert_confirm_button()
        actual=ext_sm.check_add_success_or_not()
        self.mylogger.info("检查点打印："+str(actual))
        assert actual[0] == 1
        assert actual[1].strftime("%Y%m%d") == time.strftime("%Y%m%d",time.localtime(time.time()))
        self.mylogger.info('********新增供应商,测试结束**********')

    @allure.title("删除新增的供应商")
    def test_extsupplier_06(self):
        self.mylogger.info('********删除供应商,测试开始**********')
        lg = LoginPage(self.driver)
        lg.slmode_eshop('child', '17754124411', '230516')
        ext_sm = ExtSMPage(self.driver)
        ext_sm.selct_supplier_shop('重庆帆舟运输有限公司')
        ext_sm.supplier_del_button()
        ext_sm.del_alert_confirm()
        actual = ext_sm.check_add_success_or_not()
        self.mylogger.info("检查点打印："+str(actual))
        assert actual[0] == 0

    @allure.title("查询存在的供应商")
    def test_extsupplier_07(self):
        self.mylogger.info('********查询供应商，查询结果存在,测试开始**********')
        lg = LoginPage(self.driver)
        lg.slmode_eshop('child', '17754124411', '230516')
        ext_sm = ExtSMPage(self.driver)
        ext_sm.selct_supplier_shop('北京的公司')
        actual = ext_sm.check_select_result(1)
        self.mylogger.info("检查点打印："+str(actual))
        assert actual == '北京的公司'

    @allure.title("查询不存在的供应商")
    def test_extsupplier_08(self):
        self.mylogger.info('********查询供应商，查询结果存在,测试开始**********')
        lg = LoginPage(self.driver)
        lg.slmode_eshop('child', '17754124411', '230516')
        ext_sm = ExtSMPage(self.driver)
        ext_sm.selct_supplier_shop('北京的公司1')
        actual = ext_sm.check_select_result(2)
        self.mylogger.info("检查点打印：" + str(actual))
        assert actual == '暂无数据'



if __name__ == '__main__':
    pytest.main()

