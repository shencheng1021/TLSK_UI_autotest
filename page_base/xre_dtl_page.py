# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: 信融e产品产品详情页面对象层
@time: 2023/11/13 9:16
"""
import time

import allure
from selenium.webdriver.common.by import By

from base1.base_page import BasePage


class XreDtlPage(BasePage):

    # 定位立即申请按钮
    apply_now_btn_loc=(By.XPATH,"//span[contains(text(),'立即申请')]")

    # 定位数据授权协议
    license_agreement_loc = (By.XPATH, "//span[contains(text(),'信融E数据授权协议')]")

    # 定位未实名认证提示
    not_auth_warn_loc = (By.XPATH, "//p[contains(text(),'请先完成实名认证')]")

    # 定位未登录提示框
    not_login_warn_loc = (By.XPATH, "//p[contains(text(),'系统检测到您尚未登录，或者登录已过期，请先登录以继续操作')]")

    #定位产品操作页面产品名称
    product_name_loc=(By.XPATH,"//div[@class='bigTitle']")

    @allure.step('进入信融e产品介绍页面')
    def goto_xreDtl_page(self):
        time.sleep(3)
        self.goto_url('http://172.24.100.75:10006/#/market/productCommon/index?proType=xreSupply')

    @allure.step('点击立即申请按钮')
    def click_applyBtl(self):
        self.click(XreDtlPage.apply_now_btn_loc)

    @allure.step('检查是否提示未完成实名认证')
    def check_whether_auth(self):
        return self.is_visible(XreDtlPage.not_auth_warn_loc)

    @allure.step('检查是否提示未登录')
    def check_whether_lg(self):
        return self.is_visible(XreDtlPage.not_login_warn_loc)

    @allure.step('检查是否弹出数据授权协议弹窗')
    def check_whether_agreement(self):
        return self.is_visible(XreDtlPage.license_agreement_loc)

    @allure.step('检查产品操作页面的产品名称')
    def check_product_name(self):
        return self.get_text(XreDtlPage.product_name_loc)






