# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: E信通供应商管理页面对象层
@time: 2022/4/13 9:34
"""
import time

from selenium.webdriver.common.by import By

from base1.base_page import BasePage
import allure

from common.mysql_util import MysqlConnection


class ExtSMPage(BasePage):

    #定位联系人姓名
    contact_name_loc=(By.XPATH,"//thead[@class='has-gutter']/tr/th[3]/div")

    #检查是否进入E信通产品操作页面的定位
    ext_title_loc=(By.XPATH,"//div[@class='e-left-box content']/div")

    #供应商管理菜单定位
    supplier_manage_loc=(By.XPATH,"//div[contains(text(),'供应商管理')]")

    #定位单笔新增供应商按钮
    add_supplier_loc=(By.XPATH,"//div[@class='container-m']/header/form/div[3]/button[1]")

    #定位新增供应商弹出框中供应商名称的输入框
    supplier_input_loc=(By.XPATH,"//div[@class='el-dialog__body']/header/form/div/div/input")

    #定位新增供应商弹出框中查询按钮
    select_button_loc=(By.XPATH,"//div[@class='el-dialog__body']/header/form/div[2]/button")

    #定位新增供应商弹窗中的勾选框
    table_label_loc=(By.XPATH,'//*[@id="app"]/div[2]/div[1]/div/div[2]/div/div/div[4]'
                              '/div/div/div[2]/main/div[1]/div[4]/div[2]/table/tbody/tr/td[1]/div/label/span/span')

    #定位新增供应商弹窗中的确认按钮
    alert_confirm_loc=(By.XPATH,"//div[@class='table-list']/div[4]/div/div/div[3]/span/button[1]")

    #定位供应商管理列表，供应商名称搜索框
    supplier_name_input_loc=(By.XPATH,"//div[@class='container-m']/header/form/div[1]/div/input")

    #定位供应商管理列表,查询按钮
    supplier_select_button_loc=(By.XPATH,"//div[@class='container-m']/header/form/div[2]/button[1]")

    #定位供应商管理列表,删除按钮
    supplier_del_button_loc=(By.XPATH,'//*[@id="app"]/div[2]/div[1]/div/div[2]/div/div/div[1]/div[4]/div[2]/table/tbody/tr/td[6]/div/button[2]')

    #定位删除供应商确认弹窗中的确认按钮
    del_alert_confirm_loc=(By.XPATH,"//div[@class='el-message-box__btns']/button[2]")

    #判断查询结果是否更新的定位:
    select_is_update_loc=(By.XPATH,'//*[@id="app"]/div[2]/div[1]/div/div[2]/div/div/div[1]/div[3]/table/tbody/tr[2]/td[2]')

    #检查点元素定位，定位供应商列表供应商企业名称
    supplier_list_suppliername_loc=(By.XPATH,'//*[@id="app"]/div[2]/div[1]/div/div[2]/div/div/div[1]/div[3]/table/tbody/tr/td[2]/div')

    # 检查点元素定位，定位供应商列表查询无结果时的定位
    supplier_list_result_loc=(By.XPATH,'//*[@id="app"]/div[2]/div[1]/div/div[2]/div/div/div[1]/div[3]/div/span')

    #供应商新增成功的提示定位
    add_supplier_success_tips_loc=(By.XPATH,"//p[contains(text(),'新增成功！')]")


    @allure.step("点击单笔新增供应商按钮")
    def click_add_supplier(self):
        self.click(ExtSMPage.add_supplier_loc)

    @allure.step("进入E信通产品操作页面")
    def goto_eChannelPage(self):
        self.goto_url('http://172.24.100.75:10006/#/market/eChannelPage')

    @allure.step("切换至供应商管理菜单")
    def switch_sm_menu(self):
        self.click(ExtSMPage.supplier_manage_loc)

    @allure.step("单笔新增供应商弹窗:输入供应商名称")
    def alert_input_supplier_name(self,key):
        self.send_keys(ExtSMPage.supplier_input_loc,key)

    @allure.step("单笔新增供应商弹窗:查询供应商")
    def alert_select_supplier_name(self):
        self.click(ExtSMPage.select_button_loc)

    @allure.step("单笔新增供应商弹窗:选择供应商")
    def select_supplier_name(self):
        time.sleep(3)
        self.click(ExtSMPage.table_label_loc)

    @allure.step("单笔新增供应商弹窗:点击确定按钮")
    def alert_confirm_button(self):
        self.click(ExtSMPage.alert_confirm_loc)
        self.is_not_visible(ExtSMPage.add_supplier_success_tips_loc)

    @allure.step("供应商管理列表，输入供应商名称")
    def input_supplier_name(self,key):
        self.send_keys(ExtSMPage.supplier_name_input_loc,key)

    @allure.step("供应商管理列表，点击查询按钮")
    def supplier_select_button(self):
        self.click(ExtSMPage.supplier_select_button_loc)

    @allure.step("供应商管理列表，点击删除按钮")
    def supplier_del_button(self):
        self.click(ExtSMPage.supplier_del_button_loc)

    @allure.step("删除确认弹窗，点击确认按钮")
    def del_alert_confirm(self):
        self.click(ExtSMPage.del_alert_confirm_loc)

    @allure.step("检查是否成功进入E信通供应商管理页面")
    def check_supplier_manage(self):
        return self.get_text(ExtSMPage.ext_title_loc)

    @allure.step("输入供应商名称并查询的动作")
    def selct_supplier_shop(self,key):
        self.goto_url('http://172.24.100.75:10006/#/market/eChannelPage')
        self.click(ExtSMPage.supplier_manage_loc)
        self.send_keys(ExtSMPage.supplier_name_input_loc,key)
        self.click(ExtSMPage.supplier_select_button_loc)
        self.invisibility_of_element_located(ExtSMPage.select_is_update_loc)

    @allure.step("检查供应商是否在供应商列表中")
    def check_add_success_or_not(self):
        sql="SELECT count(*),create_time FROM tjf_user01.t_core_enterprise_supplier " \
            "WHERE core_number = 'TN2022042700010413' AND supplier_number = 'TN2023020600025803'"
        result=MysqlConnection('tjf_user01').QueryAll(sql)
        return result[0]

    @allure.step("检查供应商列表查询结果")
    def check_select_result(self,index):
        result=''
        if index == 1 :
            result=self.get_text(ExtSMPage.supplier_list_suppliername_loc)
        elif index == 2 :
            result=self.get_text(ExtSMPage.supplier_list_result_loc)

        return result
