# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: 流程审核的页面对象层
@time: 2023/10/15 15:14
"""
import allure
from selenium.webdriver.common.by import By

from base1.base_page import BasePage


class ProcessAuditPage(BasePage):

    #定位流程详情列表中对应的审核按钮
    audit_button_loc=(By.XPATH,"//table[@class='el-table__body']/tbody/tr/td[9]/div/span/button")

    #定位结算单校验启停按钮
    settle_receipt_switch_loc=(By.XPATH,"//span[@class='el-switch__core']")

    # 定位Oa签报第一个复选框
    oa_checkbox_loc = (By.XPATH, "//div[@class='oa-info']/div[2]/div[2]/div/div[3]/table/tbody/tr[1]/td[1]/div/label/span/span")

    #定位付款承诺涵签署按钮
    seal_button_loc=(By.XPATH,'//*[@id="app"]/div[2]/div[1]/div/div[3]/div[4]/div[2]/div[2]/div/div[4]/div[2]/table/tbody/tr/td[6]/div/span/button[1]/span')

    #定位付款承诺涵弹窗中我已认真阅读复选框
    payment_checkbox_loc=(By.XPATH,"//div[@class='bottom-text vertical-center']/label/span/span")

    #自动盖章按钮定位
    auto_seal_button_loc=(By.XPATH,"//span[contains(text(),'自动盖章')]")

    #通过按钮定位
    pass_button_loc=(By.XPATH,"//div[@class='middle-btn']/button[3]/span")

    #拒绝按钮定位
    reject_button_loc=(By.XPATH,"//span[contains(text(),'拒绝')]")

    #审核成功检查点定位
    audit_tips_loc=(By.XPATH,"//p[@class='el-message__content']")

    @allure.step("进入流程详情页面")
    def goto_process_detail(self):
        self.goto_url('http://172.24.100.75:10006/#/approveProcess')

    @allure.step("点击审核按钮进入流程审核页面")
    def goto_process_audit_page(self):
        self.click(ProcessAuditPage.audit_button_loc)

    @allure.step("点击是否开启结算单校验功能开关")
    def click_settle_receipt_switch(self):
        self.click(ProcessAuditPage.settle_receipt_switch_loc)

    @allure.step("选择关联的OA信息")
    def select_oa_info(self):
        self.click(ProcessAuditPage.oa_checkbox_loc)

    @allure.step("点击付款承诺涵签署按钮")
    def click_seal_button(self):
        self.click(ProcessAuditPage.seal_button_loc)

    @allure.step("选择我已阅读付款承诺涵复选框")
    def select_payment_checkbox(self):
        self.click(ProcessAuditPage.payment_checkbox_loc)

    @allure.step("点击自动签署按钮")
    def click_autoseal_button(self):
        self.click(ProcessAuditPage.auto_seal_button_loc)

    @allure.step("点击审核通过")
    def click_pass_button(self):
        self.click(ProcessAuditPage.pass_button_loc)

    @allure.step("点击审核拒绝")
    def click_reject_button(self):
        self.click(ProcessAuditPage.reject_button_loc)

    @allure.step("审核通过操作")
    def audit_pass_shop(self):
        self.click(ProcessAuditPage.audit_button_loc)
        self.click(ProcessAuditPage.settle_receipt_switch_loc)
        self.click(ProcessAuditPage.oa_checkbox_loc)
        self.click(ProcessAuditPage.seal_button_loc)
        self.click(ProcessAuditPage.payment_checkbox_loc)
        self.click(ProcessAuditPage.auto_seal_button_loc)
        self.click(ProcessAuditPage.pass_button_loc)

    @allure.step("检查审核结果")
    def check_audit_result(self):
        return self.get_text(ProcessAuditPage.audit_tips_loc)


