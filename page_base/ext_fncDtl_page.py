# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: E信通融资详情页面
@time: 2024/1/24 11：19
"""
import allure
from selenium.webdriver.common.by import By

from base1.base_page import BasePage
from common.dir_util import ext_data_dir


class ExtFncdtlPage(BasePage):

    #定位融资详情菜单
    fncdtl_menu_btn=(By.XPATH,"//div[contains(text(),'融资详情')]")

    #定位补充线上融资材料按钮
    fnc_material_btn=(By.XPATH,"//div[@class='container-mf']/div/div[1]/div[3]/table/tbody/tr[1]/td[9]/div/button[2]")

    #定位下一步按钮
    next_step_btn=(By.XPATH,"//span[contains(text(),'下一步')]")

    #定位下一步按钮
    last_tep_btn=(By.XPATH,"//span[contains(text(),'上一步')]")

    #定位合同编号输入框
    contract_number_input=(By.XPATH,"//input[@placeholder='合同编号']")

    # 定位合同签订日期输入框
    contract_signdata_input = (By.XPATH, "//input[@placeholder='选择日期']")

    # 定位合同金额输入框
    contract_amount_input = (By.XPATH, "//input[@placeholder='合同金额']")

    # 定位合同文件上传按钮
    contract_file_upload_btn = (By.XPATH, "//input[@name='file']")

    # 定位发票文件上传按钮
    invoice_file_upload_btn = (By.XPATH, "//input[@multiple='multiple']")

    # 定位提交审核按钮
    submit_audit_btn=(By.XPATH,"//span[contains(text(),'提交审核')]")

    #定位系统提示框
    sys_tips_loc=(By.XPATH,"//p[contains(text(),'操作失败 [发送应收账款信息给银行失败:企业不存在：供应商新101]')]")

    #定位查询条件融信编号输入框
    rx_bumber_input=(By.XPATH,"//input[@placeholder='请输入融信编号']")

    #定位查询按钮
    select_btn=(By.XPATH,"//span[contains(text(),'查询')]")

    #定位融资状态
    financing_status=(By.XPATH,"//div[@class='container-mf']/div/div[1]/div[3]/table/tbody/tr[1]/td[8]/div/span")

    #定位查询结果总数
    totality_loc=(By.XPATH,"//span[@class='el-pagination__total']")

    #定位第二列
    second_line_loc=(By.XPATH,"//div[@class='container-mf']/div/div[1]/div[3]/table/tbody/tr[2]")

    #定位跳转至融通确认按钮
    jump_rt_btn=(By.XPATH,"//span[contains(text(),'跳转至融通确认')]")

    @allure.step('进入E信通融资详情列表')
    def goto_financing_material_page(self):
        self.goto_url('http://172.24.100.75:10006/#/market/eChannelPage')
        self.click(self.fncdtl_menu_btn)

    @allure.step('补充上传融资材料')
    def upload_financing_material(self):
        self.click(self.fnc_material_btn)
        self.click(self.next_step_btn)
        self.clear_send_keys(self.contract_number_input,'TLSK2023')
        self.clear_send_keys(self.contract_signdata_input,'2023-09-01')
        self.clear_send_keys(self.contract_amount_input,'5000000.00')
        self.upload_file(self.contract_file_upload_btn,'融资合同.pdf',ext_data_dir)
        self.click(self.next_step_btn)
        self.upload_file(self.invoice_file_upload_btn,'融资发票.png',ext_data_dir)
        self.click(self.next_step_btn)
        self.click(self.submit_audit_btn)

    @allure.step('检查提交后系统提示')
    def check_submit_result(self):
        return self.get_text(self.sys_tips_loc)

    @allure.step('根据融信编号查询融资流水')
    def select_financing_data(self,rxnumber):
        self.send_keys(self.rx_bumber_input,rxnumber)
        self.click(self.select_btn)
        self.is_not_visible(self.second_line_loc,10)

    @allure.step('获取当前融资流水融资状态')
    def check_financing_status(self):
        return self.get_text(self.financing_status)

    @allure.step('获取查询结果条数')
    def check_select_res_number(self):
        return self.get_text(self.totality_loc)

    @allure.step('点击跳转至融通确认按钮,跳转至建信融通页面')
    def click_jumprt_btn(self):
        self.click(self.jump_rt_btn)
        self.switch_specify_window('建信融通-建设银行旗下融资服务平台')

    @allure.step('获取当前窗口的title')
    def check_window_title(self):
        return self.get_window_title()











