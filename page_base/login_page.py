# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: test
@time: 2022/4/13 9:34
"""
import logging
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from base1.base_page import BasePage
from common.logger_util import Logger

log=Logger(__name__,CmdLevel=logging.INFO, FileLevel=logging.INFO)

class LoginPage(BasePage):
    #定位页面元素
    slmode_loc=(By.ID,'tab-second')
    username_loc=(By.XPATH, "//input[@placeholder='请输入手机号码']")
    password_loc=(By.XPATH, "//div[@class='c-phonecode-input']/div/input")
    checkbox_loc=(By.XPATH, "//span[@class='el-checkbox__inner']")
    loginbutton_loc=(By.XPATH, "//div[@class='el-tabs__content']/button")
    organization_loc=(By.XPATH,"//div[@class='per-top']/span")
    organization_01_loc=(By.XPATH,"//span[contains(text(),'砼联数字科技有限公司')]")
    username_failwarn_loc=(By.XPATH,"//form[@class ='el-form login-form-body']/div[1]/div/div[2]")
    checkcode_fail_loc=(By.XPATH,"//p[@class='el-message__content']")
    checkcode_null_loc = (By.XPATH, "//form[@class ='el-form login-form-body']/div[3]/div/div[2]")

    merchants_center_loc=(By.XPATH,"//div[@class='tag-inside']/ul[5]/li")

    # 判断是否登录成功
    login_success_tips_loc = (By.XPATH, "//p[contains(text(),'登录成功')]")



    #页面的动作
    #登录动作
    def slmode_eshop(self,id,username,password):
        try:
            self.goto_iframe(id)
            time.sleep(1)
            self.click(LoginPage.slmode_loc)
            self.send_keys(LoginPage.username_loc,username)
            self.send_keys(LoginPage.password_loc,password)
            self.click(LoginPage.checkbox_loc)
            self.click(LoginPage.loginbutton_loc)
            time.sleep(3)
        except NoSuchElementException as e:
            print("no such element",e)
        else:
            pass

    def login_success_eshop(self,id,username,password):
        log.logger.info('**********执行登录动作开始**********')
        self.goto_iframe(id)
        time.sleep(1)
        self.click(LoginPage.slmode_loc)
        self.send_keys(LoginPage.username_loc,username)
        self.send_keys(LoginPage.password_loc,password)
        self.click(LoginPage.checkbox_loc)
        self.click(LoginPage.loginbutton_loc)
        self.quit_iframe()
        self.is_visible(LoginPage.login_success_tips_loc)
        #self.is_not_visible(LoginPage.login_success_tips_loc,3)
        log.logger.info('**********执行登录动作结束**********')

    def goto_merchants_center(self):
        try:
            self.quit_iframe()
            self.click(LoginPage.merchants_center_loc)
            time.sleep(3)
        except NoSuchElementException as e:
            print("no such element",e)
        else:
            pass


    #登录成功的检查点动作
    def check_point_shop(self):
        try:
            check_point=self.get_text(LoginPage.organization_loc)
        except NoSuchElementException as e:
            print("no such element",e)
        else:
            return check_point


    #登录失败的检查点动作
    def loginfail_check_shop(self,loc):
        try:
            loginfail_check=self.get_text(loc)
        except NoSuchElementException as e:
            print("no such element",e)
        else:
            return loginfail_check




