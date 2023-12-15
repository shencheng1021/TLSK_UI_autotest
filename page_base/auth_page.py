# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: 添加实名认证页面得动作
@time: 2023/9/11 10:57
"""
import time

import allure
from selenium.webdriver.common.by import By
from base1.base_page import BasePage
from common import dir_util


class AuthBage(BasePage):
    #定位商户中心按钮
    merchants_center_loc=(By.XPATH,"//div[@class='tag-inside']/ul[5]/li")

    #定位企业信息管理按钮
    enterprise_management_loc=(By.XPATH,"//div[contains(text(),'企业信息管理')]")

    #定位修改实名认证按钮
    update_auth_loc=(By.XPATH,"//span[contains(text(),'修改实名认证信息')]")

    #定位营业执照上次传控件
    business_upload_loc=(By.XPATH,"//div[@class='busiLice-list']/div/div/div/input")

    #定位省下拉框
    province_select_loc=(By.XPATH,"//div[@class='distpicker-address-wrapper']/label[1]/select")

    #定位市下拉框
    city_select_loc=(By.XPATH,"//div[@class='distpicker-address-wrapper']/label[2]/select")

    #定位区下拉框
    district_select_loc=(By.XPATH,"//div[@class='distpicker-address-wrapper']/label[3]/select")

    #定位法人身份证正面
    legal_front_loc=(By.XPATH,"//form[@class='el-form']/div[4]/div[1]/div/div/div/div/div/div[1]/div[1]/div/input")

    # 定位法人身份证背面
    legal_backside_loc =(By.XPATH,"//form[@class='el-form']/div[4]/div[1]/div/div/div/div/div/div[2]/div[1]/div/input")

    #定位法人联系电话输入框
    legal_phone_loc=(By.XPATH, "//input[@placeholder='请输入法人手机号']")

    #定位联系人身份证正面
    contactperson_front_loc=(By.XPATH,"//form[@class='el-form']/div[6]/div[1]/div/div/div/div/div/div[1]/div[1]/div/input")

    # 定位联系人身份证背面
    contactperson_backside_loc =(By.XPATH,"//form[@class='el-form']/div[6]/div[1]/div/div/div/div/div/div[2]/div[1]/div/input")

    # 定位联系人联系电话输入框
    contactperson_phone_loc=(By.XPATH, "//input[@placeholder='请输入联系人手机号']")

    #定位客户来源下拉选择框
    customersource_loc=(By.XPATH, "//input[@placeholder='请选择用户来源']")

    #定位选择的目标来源选项
    goal_source_loc=(By.XPATH, "//span[text()='上海公司']")

    #定位实名认证确认按钮
    submmit_loc=(By.XPATH,"//div[@class='btn-middle el-row']/button[1]")

    # 定位实名认证取消按钮
    cancel_loc = (By.XPATH, "//div[@class='btn-middle el-row']/button[1]")

    #定位已认证检查点
    ahth_success_loc=(By.XPATH,"//div[@class='el-result__title']/p")

    #定位重复认证提示
    failtips_loc_=(By.XPATH,"//div[@class='el-message-box__message']/p")

    #定位重复认证提示确认按钮
    failtips_submmit_loc=(By.XPATH,"//div[@class='el-message-box__btns']/button/span")

    #定位图片上传是否成功提示框
    upload_picture_tips_loc=(By.XPATH,"//p[@class='el-message__content']")

    relativepath=dir_util.testcase_dir


    #定义完善企业信息
    @allure.step("完善企业信息")
    def auth_business_shop(self,key,province,city,district):
        self.click(AuthBage.merchants_center_loc)
        self.click(AuthBage.enterprise_management_loc)
        self.click(AuthBage.update_auth_loc)
        self.upload_file(AuthBage.business_upload_loc,key,self.relativepath)
        self.select_value(AuthBage.province_select_loc,province)
        self.select_value(AuthBage.city_select_loc,city)
        self.select_value(AuthBage.district_select_loc,district)

    #定义完善法人信息
    @allure.step("完善法人信息")
    def auth_lagal_shop(self,idcardfront,idcardbackside,phone):
        self.upload_file(AuthBage.legal_front_loc,idcardfront,self.relativepath)
        time.sleep(3)
        self.upload_file(AuthBage.legal_backside_loc,idcardbackside,self.relativepath)
        self.send_keys(AuthBage.legal_phone_loc,phone)

    #定义联系人信息
    @allure.step("完善联系人信息")
    def auth_contactperson_shop(self,idcardfront,idcardbackside,phone):
        self.upload_file(AuthBage.contactperson_front_loc,idcardfront,self.relativepath)
        time.sleep(3)
        self.upload_file(AuthBage.contactperson_backside_loc,idcardbackside,self.relativepath)
        self.send_keys(AuthBage.contactperson_phone_loc,phone)

    #定义维护客户来源
    @allure.step("完善客户来源信息")
    def auth_source_shop(self):
        self.click(AuthBage.customersource_loc)
        self.click(AuthBage.goal_source_loc)
        time.sleep(1)

    #定义保存实名认证信息
    @allure.step("保存实名认证信息")
    def auth_submit(self,key):
        if key=='1':
            self.click(AuthBage.submmit_loc)
            time.sleep(3)
        else:
            self.click(AuthBage.cancel_loc)
            time.sleep(3)

    #进入实名认证页面
    @allure.step("进入实名认证页面")
    def goto_auth_shop(self):
        self.click(AuthBage.merchants_center_loc)
        self.click(AuthBage.enterprise_management_loc)
        time.sleep(3)

    #检查是否实名认证成功
    @allure.step("检查是否实名认证成功")
    def check_point(self):
        expected=self.get_text(AuthBage.ahth_success_loc)
        return expected

    #检查是否出现重复认证提示
    @allure.step("检查是否出现重复认证提示")
    def check_point_2(self):
        failtips=self.get_text(AuthBage.failtips_loc_)
        return failtips






