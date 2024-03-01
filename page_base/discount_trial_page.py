# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: 砼秒贴自动化测试
@time: 2024/2/2 14:54
"""
import allure
from selenium.webdriver.common.by import By

from base1.base_page import BasePage
from common.time_util import after_time


class DiscountTrialPage(BasePage):

    #票面金额输入框
    amount_input=(By.XPATH,"//input[@placeholder='请输入票面金额']")

    #请选择票面到期日
    end_date_input=(By.XPATH, "//input[@placeholder='请选择票面到期日']")

    #模糊搜索承兑行
    acceptance_bank_input = (By.XPATH, "//input[@placeholder='模糊搜索承兑行']")

    #点击下拉选择项
    #drop_down_optin=(By.XPATH,"/html/body/div[7]/div[1]/div[1]/ul/li[1]/span")

    #立即询价按钮
    inquiry_btn=(By.XPATH,"//span[contains(text(),'立即询价')]")

    #询价结果提示
    inquiry_tips=(By.XPATH,"//p[@class='el-message__content']")

    #利率显示
    interest_rate=(By.XPATH, "//span[@class='rate-value']")

    #询价失败提示
    inquiry_fail_tip=(By.XPATH,"//div[@class='el-message-box__message']")

    @allure.step('进入砼秒贴页面')
    def goto_discount_page(self):
        self.goto_url('http://172.24.100.75:10006/#/market/detail/billMt')

    @allure.step('贴现询价')
    def discount_inquiry(self,date,bankname):
        self.send_keys(self.amount_input,'1000000.00')
        self.send_keys(self.end_date_input,date)
        self.send_keys(self.acceptance_bank_input,bankname)
        drop_down_optin=(By.XPATH,"//span[contains(text(),'"+bankname+"')]")
        self.click(drop_down_optin)
        self.click(self.inquiry_btn)

    @allure.step('检查询价结果')
    def check_inquiry_res(self):
        self.is_visible(self.inquiry_tips)
        self.is_not_visible(self.inquiry_tips, 10)
        return self.get_text(self.interest_rate)

    @allure.step('检查询价失败结果提示')
    def check_inquiry_fail_res(self):
        return self.get_text(self.inquiry_fail_tip)