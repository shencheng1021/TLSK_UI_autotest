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
from page_base.ext_sign_page import ExtSignPage
from page_base.ext_signfor_page import ExtSignforPage

from page_base.ext_sm_page import ExtSMPage
from page_base.login_page import LoginPage
from page_base.process_audit_page import ProcessAuditPage


@allure.feature('E信通产品自动化测试')
class TestExtdetails(BaseUtil):


    @allure.title("E信通二级页面，校验企业是否实名认证")
    def test_extdetails_01(self):
        self.mylogger.info("****************E信通二级页面，校验企业是否实名认证，测试开始****************")

        lg=LoginPage(self.driver)
        lg.login_success_eshop('child','17754856657','230516')
        EP=ExtPage(self.driver)
        EP.goto_ext_product_lg_s()
        actual=EP.check_pointt_auth_status()
        assert actual == "请先完成实名认证"
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
        lg.login_success_eshop('child','17754856658','230516')
        EP = ExtPage(self.driver)
        EP.goto_ext_product_lg_s()
        actual=EP.check_point_license_agreement()
        assert actual == "E信通数据授权协议"
        self.mylogger.info("****************E信通二级页面，校验授权协议弹出窗，测试结束****************")

    @allure.title("核心企业成功进入E信通产品操作页面")
    def test_extsupplier_04(self):
        self.mylogger.info('**********核心企业成功进入E信通产品操作页面,测试开始*********')
        lg=LoginPage(self.driver)
        lg.login_success_eshop('child','17754124411','230516')
        EP=ExtPage(self.driver)
        EP.goto_ext_product_lg_s()
        Ext_sm=ExtSMPage(self.driver)
        actual=Ext_sm.check_supplier_manage()
        self.mylogger.info("检点点打印："+actual)
        assert actual == "E信通"
        self.mylogger.info("**********核心企业成功进入E信通产品操作页面,测试结束*********")

    @allure.title("新增供应商成功")
    @pytest.mark.usefixtures('supplier_initialization')
    def test_extsupplier_05(self):
        self.mylogger.info('********新增供应商,测试开始**********')
        lg = LoginPage(self.driver)
        lg.login_success_eshop('child', '17754124411', '230516')
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
        lg.login_success_eshop('child', '17754124411', '230516')
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
        lg.login_success_eshop('child', '17754124411', '230516')
        ext_sm = ExtSMPage(self.driver)
        ext_sm.selct_supplier_shop('北京的公司')
        actual = ext_sm.check_select_result(1)
        self.mylogger.info("检查点打印："+str(actual))
        assert actual == '北京的公司'

    @allure.title("查询不存在的供应商")
    def test_extsupplier_08(self):
        self.mylogger.info('********查询供应商，查询结果存在,测试开始**********')
        lg = LoginPage(self.driver)
        lg.login_success_eshop('child', '17754124411', '230516')
        ext_sm = ExtSMPage(self.driver)
        ext_sm.selct_supplier_shop('北京的公司1')
        actual = ext_sm.check_select_result(2)
        self.mylogger.info("检查点打印：" + str(actual))
        assert actual == '暂无数据'

    @allure.title("签发融信成功")
    def test_temp_extsign_09(self):
        self.mylogger.info("*******融信签发，签发成功，测试开始********")
        lg = LoginPage(self.driver)
        lg.login_success_eshop('child', '17754124411', '230516')
        sg=ExtSignPage(self.driver)
        sg.goto_ext_creditsign_page()
        sg.click_add_credit()
        sg.input_quota_source()
        sg.input_supplier('供应商新101')
        sg.input_amount('10000')
        sg.input_payment_data('2024-10-10')
        sg.click_confirm_button()
        actual=sg.check_sign_success()
        self.mylogger.info("检查点打印：" + str(actual))
        assert actual == '新增成功'
        self.mylogger.info("*******融信签发，签发成功，测试结束********")

    @allure.title("制单通过")
    @pytest.mark.usefixtures('oa_information_initialization')
    def test_temp_process_audit_10(self):
        self.mylogger.info("*******融信签发，制单通过，测试开始********")
        lg = LoginPage(self.driver)
        lg.login_success_eshop('child', '13730870086', '230516')
        pap=ProcessAuditPage(self.driver)
        pap.goto_process_detail()
        pap.audit_pass_shop()
        actual=pap.check_audit_result()
        self.mylogger.info("检查点打印：" + str(actual))
        assert actual == '审核成功!'
        self.mylogger.info("*******融信签发，制单通过，测试结束********")

    @allure.title('初审审核通过')
    def test_temp_process_first_instance_pass_11(self):
        self.mylogger.info("*******融信签发，初审审核通过，测试开始********")
        lg = LoginPage(self.driver)
        lg.login_success_eshop('child', '13730870086', '230516')
        pap = ProcessAuditPage(self.driver)
        pap.goto_process_detail()
        pap.goto_process_audit_page()
        pap.click_pass_button()
        actual = pap.check_audit_result()
        self.mylogger.info("检查点打印：" + str(actual))
        assert actual == '审核成功!'
        self.mylogger.info("*******融信签发，初审审核通过，测试结束********")

    @allure.title('复核审核通过')
    def test_temp_process_recheck_pass_12(self):
        self.mylogger.info("*******融信签发，复核审核通过，测试开始********")
        lg = LoginPage(self.driver)
        lg.login_success_eshop('child', '13730870086', '230516')
        pap = ProcessAuditPage(self.driver)
        pap.goto_process_detail()
        pap.goto_process_audit_page()
        pap.click_pass_button()
        actual = pap.check_audit_result()
        self.mylogger.info("检查点打印：" + str(actual))
        assert actual == '审核成功!'
        self.mylogger.info("*******融信签发，复核审核通过，测试结束********")

    @allure.title('终审审核通过')
    def test_temp_process_final_instance_pass_13(self):
        self.mylogger.info("*******融信签发，终审审核通过，测试开始********")
        lg = LoginPage(self.driver)
        lg.login_success_eshop('child', '13730870086', '230516')
        pap = ProcessAuditPage(self.driver)
        pap.goto_process_detail()
        pap.goto_process_audit_page()
        pap.click_pass_button()
        actual = pap.check_audit_result()
        self.mylogger.info("检查点打印：" + str(actual))
        assert actual == '审核成功!'
        self.mylogger.info("*******融信签发，终审审核通过，测试结束********")

    @allure.title("签收成功")
    def test_temp_signfor_success_14(self):
        self.mylogger.info("*******融信签收，签收通过，测试开始********")
        lg = LoginPage(self.driver)
        lg.login_success_eshop('child', '17754211111', '230516')
        esp=ExtSignforPage(self.driver)
        esp.goto_signfor_page()
        esp.signfor_shop()
        actual=esp.check_signfor_status()
        self.mylogger.info("检查点打印：" + str(actual))
        assert actual == '签收成功,是否立即发起融资申请'
        self.mylogger.info("*******融信签收，签收通过，测试结束********")

    @allure.title("发起融资申请成功")
    def test_temp_apply_success_15(self):
        self.mylogger.info("*******融资申请，申请成功，测试开始********")
        lg = LoginPage(self.driver)
        lg.login_success_eshop('child', '17754211111', '230516')
        esp=ExtSignforPage(self.driver)
        esp.goto_signfor_page()
        esp.financing_apply_shop()
        actual=esp.check_apply_result_tips()
        self.mylogger.info("检查点打印：" + str(actual))
        assert actual == '融资基础信息您已确认成功，请点击下一步上传融资材料！'
        self.mylogger.info("*******融资申请，申请成功，测试结束********")



if __name__ == '__main__':
    pytest.main()

