# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: 融信签收并发起融资申请的页面对象层
@time: 2023/10/16 10:53
"""
import time

import allure
from selenium.webdriver.common.by import By

from base1.base_page import BasePage


class ExtSignforPage(BasePage):

    # 定位立即申请按钮
    apply_now_button_loc = (By.XPATH, "//span[contains(text(),'立即申请')]")

    #签收按钮定位
    signfor_button_loc = (By.XPATH,"//div[@class='table-list']/div[1]/div[5]/div[2]/table/tbody/tr[1]/td[8]/div[1]/button[1]/span")

    #签收成功弹窗，去融资按钮定位
    alert_gotofinancing_button_loc = (By.XPATH,"//div[@class='el-message-box__btns']/button[1]/span")

    # 签收成功弹窗，取消按钮定位
    alert_cancel_button_loc = (By.XPATH, "//div[@class='el-message-box__btns']/button[2]/span")

    #签收列表操作列，去融资按钮定位
    gotofinancing_button_loc = (By.XPATH,"//div[@class='table-list']/div/div[5]/div[2]/table/tbody/tr[1]/td[8]/div/button[2]")

    #签收列表，签收状态定位
    signfor_status_loc=(By.XPATH,"//div[@class='table-list']/div/div[5]/div[2]/table/tbody/tr[1]/td[6]/div/span")

    #定位融资申请页面，下一步按钮
    nexttep_button_loc = (By.XPATH,"//span[contains(text(),'下一步')]")

    # 定位融资申请页面，上一步按钮
    lasttep_button_loc = (By.XPATH, "//span[contains(text(),'下一步')]")

    #定位融资信息页面，确认资料真实性勾选框
    checkbox_loc = (By.XPATH,"//span[@class='el-checkbox__inner']")

    #定位融资申请页面，提交申请按钮
    submit_apply_button_loc = (By.XPATH,"//span[contains(text(),'提交申请')]")

    #融资申请基础信息确认成功提示定位
    apply_success_tips_loc = (By.XPATH,"//div[@class='el-result__title']/p")


    @allure.step("进入融信签收页面")
    def goto_signfor_page(self):
        time.sleep(1)
        self.goto_url("http://172.24.100.75:10006/#/market/productCommon/index?proType=extSupply")
        self.click(ExtSignforPage.apply_now_button_loc)

    @allure.step("点击融信签收按钮完成签收")
    def signfor_shop(self):
        self.click(ExtSignforPage.signfor_button_loc)
        self.click(ExtSignforPage.alert_cancel_button_loc)

    @allure.step("点击去融资按钮，进行融资申请")
    def financing_apply_shop(self):
        self.click(ExtSignforPage.gotofinancing_button_loc)
        self.click(ExtSignforPage.nexttep_button_loc)
        self.click(ExtSignforPage.checkbox_loc)
        self.click(ExtSignforPage.nexttep_button_loc)
        self.click(ExtSignforPage.submit_apply_button_loc)

    @allure.step("检查是否签收成功")
    def check_signfor_status(self):
        return self.get_text(ExtSignforPage.signfor_status_loc)


    @allure.step("检查融资申请是否成功")
    def check_apply_result_tips(self):
        return  self.get_text(ExtSignforPage.apply_success_tips_loc)


