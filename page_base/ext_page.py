# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: E信通产品详情页面
@time: 2022/4/13 9:34
"""
import time

from selenium.webdriver.common.by import By

from base1.base_page import BasePage


class ExtPage(BasePage):
    # 判断是否登录成功
    login_success_loc = (By.XPATH, "//div[@class='el-dropdown']/div")

    #定位立即申请按钮
    apply_now_button_loc=(By.XPATH,"//span[contains(text(),'立即申请')]")

    #定位数据授权协议
    license_agreement_loc=(By.XPATH,"//span[contains(text(),'E信通业务合作协议')]")

    #定位未实名认证提示
    not_auth_warn_loc=(By.XPATH,"//p[contains(text(),'查询完成,未完成实名认证')]")

    #定位未登录提示框
    not_login_warn_loc=(By.XPATH,"//div[@class='el-message-box__message']/p")

    #登录成功进入E信通产品详情页
    def goto_ext_product_lg_s(self):
        self.quit_iframe()
        self.presence_of_element_located(ExtPage.login_success_loc)
        time.sleep(1)
        self.goto_url('http://172.24.100.75:10006/#/market/detail/e-index')
        self.click(ExtPage.apply_now_button_loc)


    #未登录进入E信通产品详情页
    def goto_ext_product_lg_f(self):
        self.goto_url('http://172.24.100.75:10006/#/market/detail/e-index')
        self.click(ExtPage.apply_now_button_loc)

    #检查是是否弹出校验未登录的弹出窗
    def check_point_not_login(self):
        return self.visibility_of_element_located(ExtPage.not_login_warn_loc)

    #检查是否弹出数据授权协议
    def check_point_license_agreement(self):
        return self.visibility_of_element_located(ExtPage.license_agreement_loc)

    def check_pointt_auth_status(self):
        return self.visibility_of_element_located(ExtPage.not_auth_warn_loc)

