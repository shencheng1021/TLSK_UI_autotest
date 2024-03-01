# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: E信通核心企业融信签发页面对象
@time: 2022/4/13 9:34
"""
import time

import allure
from selenium.webdriver.common.by import By

from base1.base_page import BasePage


class ExtSignPage(BasePage):

    #融信签发菜单定位
    creditsign_menu_loc=(By.XPATH,"//div[contains(text(),'融信签发')]")

    #检查是否成功进入融信签发页面
    signpage_check_loc=(By.XPATH,"//span[contains(text(),'批量新增融信签发')]")

    #新增融信签发按钮定位
    sign_button_loc=(By.XPATH,"//div[@class='container-melting']/header/form/div[6]/button[3]/span")

    #新增融信签发额度来源输入框定位
    quota_source_input_loc=(By.XPATH,"//input[@placeholder='请选择额度来源']")

    #额度来源下拉选项
    quota_souce_option_loc=(By.XPATH,'/html/body/div[5]/div[1]/div[1]/ul/li/div')

    #新增融信签发供应商名称输入框定位
    supplier_name_input_loc=(By.XPATH,"//input[@placeholder='请选择供应商']")

    #供应商下拉选项定位
    supplier_name_option_loc=(By.XPATH,"/html/body/div[6]/div[1]/div[1]/ul/li[5]/div")

    #新增融信签发融信金额输入框定位
    credit_amount_input_loc=(By.XPATH,"//input[@placeholder='请输入金额']")

    #新增融信签发承诺付款日期输入框定位
    payment_date_loc=(By.XPATH,"//input[@placeholder='请选择日期']")

    #新增融信签发确认按钮定位
    confirm_button_loc=(By.XPATH,'//*[@id="app"]/div[2]/div[1]/div/div[2]/div/div/div[5]/div/div/div[3]/span/button[1]')

    #单笔新增融信签发签发成功提示定位
    sign_success_tips_loc=(By.XPATH,"//p[contains(text(),'新增成功')]")

    @allure.step("进入E信通产品融信签发页面")
    def goto_ext_creditsign_page(self):
        self.goto_url('http://172.24.100.75:10006/#/market/eChannelPage')
        self.click(ExtSignPage.creditsign_menu_loc)

    @allure.step("点击单笔新增融信签发按钮")
    def click_add_credit(self):
        self.click(ExtSignPage.sign_button_loc)

    @allure.step("选择额度来源")
    def input_quota_source(self):
        self.click(ExtSignPage.quota_source_input_loc)
        self.click(ExtSignPage.quota_souce_option_loc)

    @allure.step("选择供应商")
    def input_supplier(self, key):
        self.send_keys(ExtSignPage.supplier_name_input_loc, key)
        self.click(ExtSignPage.supplier_name_option_loc)

    @allure.step("输入金额")
    def input_amount(self, key):
        self.send_keys(ExtSignPage.credit_amount_input_loc, key)

    @allure.step("输入承诺付款日期")
    def input_payment_data(self, key):
        self.send_keys(ExtSignPage.payment_date_loc, key)
        self.click(ExtSignPage.credit_amount_input_loc)

    @allure.step("点击单笔新增融信签发确认按钮")
    def click_confirm_button(self):
        self.click(ExtSignPage.confirm_button_loc)


    @allure.step("检查融信签发是否新增成功")
    def check_sign_success(self):
        return self.get_text(ExtSignPage.sign_success_tips_loc)










