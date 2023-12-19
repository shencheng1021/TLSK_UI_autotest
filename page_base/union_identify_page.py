# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: 银联商户合作认证资料收集页面对象层
@time: 2022/4/13 9:34
"""
import time

import allure
from selenium.webdriver.common.by import By

from base1.base_page import BasePage
from common import dir_util
from common.yaml_util import YamlUtil


class UnionIdentifyPage(BasePage):

    #定位上传资料说明弹窗中标题
    data_description_loc=(By.XPATH,"//h3[contains(text(),'上传资料说明')]")

    #定位我已知悉按钮定位
    understand_button_loc=(By.XPATH,"//button[@class='el-button el-button--primary']")

    #定位修改基础信息按钮
    update_button_loc=(By.XPATH,"//span[contains(text(),'修改基础信息')]")

    #定位上传营业执照按钮
    business_license_upload_loc=(By.XPATH,"//div[@class='company-base']/form/div[1]/div/div/div[2]/div/div[2]/div/div/input")

    #定位弹窗提示文本
    alert_text_loc=(By.XPATH,"//div[@class='el-message-box__message']/p")

    #定位弹窗确认按钮
    alert_button_loc=(By.XPATH,"//div[@class='el-message-box__btns']/button[2]")

    #定位企业名称输入框
    business_name_loc=(By.XPATH,"//input[@placeholder='请输入企业名称']")

    #定位地区省输入框
    province_pulldown_loc=(By.XPATH,"//input[@placeholder='省']")
    province_input_loc=(By.XPATH,"//span[contains(text(),'北京')]")

    # 定位地区市输入框
    city_pulldown_loc=(By.XPATH, "//input[@placeholder='市']")
    city_input_loc = (By.XPATH, "//span[contains(text(),'北京市')]")
    # 定位地区区输入框
    area_pulldown_loc=(By.XPATH, "//input[@placeholder='区']")
    area_input_loc = (By.XPATH, "//span[contains(text(),'朝阳区')]")

    #定位法人正面上传按钮
    legal_front_loc=(By.XPATH,"//div[@class='main-bottom']/div[4]/div/form/div[1]/div/div/div[2]/div/div[2]/div[1]/div/div[1]/input")

    #定位法人背面上传按钮
    legal_back_loc=(By.XPATH,"//div[@class='main-bottom']/div[4]/div/form/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div[1]/input")

    #定位法人手机号输入框
    legal_phone_loc=(By.XPATH,"//div[@class='main-bottom']/div[4]/div/form/div[3]/div[1]/div/div/div/div/input")

    #定位联系人正面上传控件
    contact_front_loc=(
        By.XPATH,"//div[@class='main-bottom']/div[6]/div/form/div[1]/div/div/div[2]/div/div[2]/div[1]/div/div[1]/input")

    # 定位联系人背面上传控件
    contact_back_loc = (
        By.XPATH, "//div[@class='main-bottom']/div[6]/div/form/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div[1]/input")

    #定位联系人手机号
    contact_phone_loc=(By.XPATH,"//div[@class='main-bottom']/div[6]/div/form/div[3]/div[1]/div/div/div/div/input")

    #定位下一步按钮：
    next_step_btn_loc=(By.XPATH,"//div[@class='user-base-info']/div[3]/div")

    #定位账户信息上传控件
    acc_ifm_upload_loc=(By.XPATH,"//div[@class='upload-cl']/div/input")

    #定位银行账户输入框
    bank_acc_input_loc=(By.XPATH,"//input[@placeholder='请输入银行账户']")

    #定位账户名称输入框
    acc_name_input_loc=(By.XPATH,"//input[@placeholder='请输入账户名称']")

    #定位银行行名输入框
    bank_name_input_loc=(By.XPATH,"//input[@placeholder='请输入行名模糊搜索']")

    #定位银行行名下拉第一个选项
    bank_name_select_loc=(By.XPATH,"/html/body/div[2]/div[9]/div/div/div[1]/ul/li[1]/span")

    #定位银行地址输入框
    banl_address_input_loc=(By.XPATH,"//input[@placeholder='请输入银行地址']")

    #定位账户信息下一步页面
    acc_next_step_btn=(By.XPATH,"//div[@class='count-info']/div[2]/div[2]")

    #定位账户信息上一步页面
    acc_up_step_btn = (By.XPATH, "//div[@class='count-info']/div[2]/div[1]")

    #定位场景证明上传控件
    scene_proof_upload_loc=(By.XPATH,"//div[@class='other-info']/form/div[1]/div/div/div[2]/div/div[1]/input")

    #定位办公场所上传控件
    office_space_uoload_loc=(By.XPATH,"//div[@class='other-info']/form/div[2]/div/div/div[2]/div[1]/div/input")

    #定位商品图片上传控件
    product_picture_upload_Loc=(By.XPATH,"//div[@class='other-info']/form/div[2]/div/div/div[2]/div[2]/div/input")

    #定位门头招牌上传控件
    door_upload_loc=(By.XPATH,"//div[@class='other-info']/form/div[2]/div/div/div[2]/div[3]/div/input")

    #定位行业成员资金管理授权确认书上传控件
    auth_confirm_upload_loc=(By.XPATH,"//div[@class='other-info']/form/div[3]/div/div/div[2]/div/div[1]/input")

    #定位经营证明上传控件
    business_certificate_upload_loc=(By.XPATH,"//div[@class='other-info']/form/div[4]/div/div/div[2]/div/div[1]/input")

    #定位平台商家入驻协议上传控件
    agreement_upload_loc=(By.XPATH,"//div[@class='other-info']/form/div[5]/div/div/div[2]/div/div[1]/input")

    #定位代理人商户授权书上传控件
    merchants_auth_upload_loc=(By.XPATH,"//div[@class='other-info']/form/div[6]/div/div/div[2]/div/div[1]/input")

    #定位代理人身份证正面上传控件
    merchants_front_upload_loc=(By.XPATH,"//div[@class='other-info']/form/div[7]/div/div/div[2]/div[1]/div/div[1]/input")

    # 定位代理人身份证背面上传控件
    merchants_back_upload_loc=(By.XPATH, "//div[@class='other-info']/form/div[7]/div/div/div[2]/div[2]/div/div[1]/input")

    #其他补充资料上传控件
    other_upload_loc=(By.XPATH,"//div[@class='other-info']/form/div[8]/div/div/div[2]/div/div[1]/input")

    #定位商户资料提交按钮
    submit_btn_loc=(By.XPATH,"//div[@class='other-info']/div[2]/div[2]")

    #初始化测试文件路径
    relativepath=dir_util.union_data_dir

    #定位提交成功提示
    submit_success_tips_loc=(By.XPATH,"//div[@class='info-text middle-center']")

    #审核退回页面状态
    reject_status_loc=(By.XPATH,"//span[@class='info-status']")

    #营业执照审核退款的提示图片定位
    bl_reject_img_loc=(By.XPATH,"//div[@class='company-base']/form/div[1]/div/div/div[2]/div/div[2]/div/div/img[2]")

    #营业执照审核退回材料状态
    bl_reject_status_loc=(By.XPATH,"//span[contains(text(),'营业执照错误')]")


    @allure.step('进入商户合作资料填报url')
    def goto_identify_page(self):
        url = YamlUtil().read_extract_yaml('identifyPage')
        self.goto_url(url)
    @allure.step('检查是否弹出上传资料说明弹窗')
    def check_data_description_alert(self):
        return self.is_visible_text(self.data_description_loc)

    @allure.step('输入企业相关我信息')
    def input_business_information(self,filename,business_name):
        try:
            self.click(self.understand_button_loc)
        except:
            pass
        self.click(self.update_button_loc)
        self.upload_file(self.business_license_upload_loc,filename,self.relativepath)
        self.click(self.alert_button_loc)
        self.clear_send_keys(self.business_name_loc,business_name)
        self.click(self.province_pulldown_loc)
        self.click(self.province_input_loc)
        self.click(self.city_pulldown_loc)
        self.click(self.city_input_loc)
        self.click(self.area_pulldown_loc)
        self.click(self.area_input_loc)

    @allure.step('输入法人证件相关信息')
    def input_legal_information(self,legal_front,legal_back,phone):
        self.upload_file(self.legal_front_loc,legal_front,self.relativepath)
        self.upload_file(self.legal_back_loc, legal_back,self.relativepath)
        time.sleep(3)
        self.clear_send_keys(self.legal_phone_loc,phone)

    @allure.step('输入联系人证件相关信息')
    def input_contact_person_information(self, contact_front, contact_back, phone):
        self.upload_file(self.contact_front_loc,contact_front,self.relativepath)
        self.upload_file(self.contact_back_loc,contact_back,self.relativepath)
        time.sleep(3)
        self.clear_send_keys(self.contact_phone_loc,phone)

    @allure.step('点击企业信息页面下一步操作')
    def click_next_step_button(self):
        self.click(self.next_step_btn_loc)

    @allure.step('输入银行账户相关信息')
    def input_acc_ifm(self,filename,bank_acc,acc_name,bank_name,banl_address):
        self.upload_file(self.acc_ifm_upload_loc,filename,self.relativepath)
        self.clear_send_keys(self.bank_acc_input_loc,bank_acc)
        self.clear_send_keys(self.acc_name_input_loc,acc_name)
        self.send_keys(self.bank_name_input_loc,bank_name)
        self.click(self.bank_name_select_loc)
        self.clear_send_keys(self.banl_address_input_loc,banl_address)

    @allure.step('银行账户信息页面，点击下一步按钮')
    def click_acc_next_step(self):
        self.click(self.acc_next_step_btn)

    @allure.step('上传场景证明')
    def upload_scene_proof(self,filename):
        self.upload_file(self.scene_proof_upload_loc,filename,self.relativepath)

    @allure.step('上传办公场所照片')
    def upload_office_space(self,filename):
        for file in filename:
            self.upload_file(self.office_space_uoload_loc,file,self.relativepath)

    @allure.step('上传商品照片')
    def upload_product_picture(self,filename):
        for file in filename:
            self.upload_file(self.product_picture_upload_Loc,file,self.relativepath)

    @allure.step('上传门头招牌照片')
    def upload_door(self,filename):
        for file in filename:
            self.upload_file(self.door_upload_loc,file,self.relativepath)

    @allure.step('上传行业成员资金管理授权确认书')
    def upload_auth_confirm(self,filename):
        self.upload_file(self.auth_confirm_upload_loc,filename,self.relativepath)

    @allure.step('上传经营证明')
    def upload_business_certificate(self,filename):
        for file in filename:
            self.upload_file(self.business_certificate_upload_loc,file,self.relativepath)

    @allure.step('上传平台商家入驻协议')
    def upload_agreement(self,filename):
        self.upload_file(self.agreement_upload_loc,filename,self.relativepath)

    @allure.step('上传代理人商户授权书')
    def upload_merchants_auth(self,filename):
        self.upload_file(self.merchants_auth_upload_loc,filename,self.relativepath)

    @allure.step('上传代理人身份证正面')
    def upload_merchants_front(self,filename):
        self.upload_file(self.merchants_front_upload_loc,filename,self.relativepath)

    @allure.step('上传代理人身份证背面')
    def upload_merchants_back(self,filename):
        self.upload_file(self.merchants_back_upload_loc,filename,self.relativepath)

    @allure.step('上传其他资料')
    def upload_other(self,filename):
        for file in filename:
            self.upload_file(self.other_upload_loc,file,self.relativepath)

    @allure.step('点击商户合作资料收集提交按钮')
    def click_submit(self):
        self.click(self.submit_btn_loc)

    @allure.step('商户合作资料重新提交')
    def resubmit_shop(self):
        self.goto_identify_page()
        self.click(self.update_button_loc)
        self.click_next_step_button()
        self.click_acc_next_step()
        self.click_submit()


    @allure.step('检查商户合作资料收集页面状态是否正确')
    def check_reject_status(self):
        page_status=self.is_visible_text(self.reject_status_loc)
        self.move_to_element(self.bl_reject_img_loc)
        bl_status=self.is_visible_text(self.bl_reject_status_loc)
        return page_status,bl_status

    @allure.step('商户认证资料提交申请成功提示检查点')
    def check_submit_success(self):
        return self.is_visible_text(self.submit_success_tips_loc)




