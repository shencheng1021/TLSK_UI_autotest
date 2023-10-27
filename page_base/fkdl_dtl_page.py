# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: 付款代理产品详情页面
@time: 2022/4/13 9:34
"""
import time

import allure
from selenium.webdriver.common.by import By
from base1.base_page import BasePage


class FkdlDtlPage(BasePage):

    apply_now_btl_loc=(By.XPATH,"//span[contains(text(),'立即申请')]")

    # 定位数据授权协议
    license_agreement_loc = (By.XPATH, "//div[@class='pro-common-page']/div[6]/div/div/span")

    # 定位未实名认证提示
    not_auth_warn_loc = (By.XPATH, "//p[@class='el-message__content']")

    # 定位未登录提示框
    not_login_warn_loc = (By.XPATH, "//div[@class='el-message-box__message']/p")

    #保理E产品操作页检查点
    ble_title_loc=(By.XPATH,"//div[@class='p-left-box content']/div[1]")

    @allure.step("进入保理E产品介绍页面,点击立即申请按钮")
    def goto_fkdlDtlPage(self):
        time.sleep(3)
        self.goto_url("http://172.24.100.75:10006/#/market/productCommon/index?proType=factorSupply")
        self.click(FkdlDtlPage.apply_now_btl_loc)

    @allure.step("立即申请成功，检查是否进入进入保理E产品操作页面")
    def check_applybtl_success(self):
        return self.get_text(FkdlDtlPage.ble_title_loc)

    @allure.step("检查是否弹出数据授权协议")
    def check_license_agreement(self):
        return self.is_visible_text(FkdlDtlPage.license_agreement_loc)

    @allure.step("未实名认证，检查是否弹出未实名认证提示")
    def check_not_auth_warn(self):
        return self.is_visible_text(FkdlDtlPage.not_auth_warn_loc)

    @allure.step("未登录，检查是否弹出未登录提示")
    def cheak_not_login_warn(self):
        return self.is_visible_text(FkdlDtlPage.not_login_warn_loc)







