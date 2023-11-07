# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: test
@time: 2022/4/13 9:34
"""
import datetime
import os
import time

from datetime import datetime


from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from common.mysql_util import MysqlConnection

# sql="SELECT count(*),create_time FROM tjf_user01.t_core_enterprise_supplier " \
#             "WHERE core_number = 'TN2022042700010413' AND supplier_number = 'TN2023020600025803'"
# result=MysqlConnection('tjf_user01').QueryAll(sql)
# print(result[0][0])
#print(time.localtime(time.time()))
# dt=result[0][0]
# print(dt.strftime("%Y%m%d"))

#qqq=time.strftime('%Y%m%d',result[0][0])
#print(qqq)


driver = webdriver.Chrome()
# #
filepath=os.path.abspath(os.path.dirname(__file__)).split("test_case")[0]
print(filepath)
#
#

#登录
driver.get('http://172.24.100.75:10006/#/login')
driver.implicitly_wait(10)
driver.maximize_window()
driver.switch_to.frame('child')
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='tab-second']").click()
driver.find_element(By.XPATH, "//input[@placeholder='请输入手机号码']").send_keys('17754756654')
driver.find_element(By.XPATH, "//div[@class='c-phonecode-input']/div/input").send_keys('230516')
driver.find_element(By.XPATH, "//span[@class='el-checkbox__inner']").click()
driver.find_element(By.XPATH, "//div[@class='el-tabs__content']/button").click()
driver.switch_to.default_content()
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//div[@class='el-dropdown']/div")))
print(driver.current_url)
#
#E信通供应商融信签发
# driver.get('http://172.24.100.75:10006/#/approveProcess')
# driver.find_element(By.XPATH,"//table[@class='el-table__body']/tbody/tr/td[9]/div/span/button").click()
# driver.find_element(By.XPATH,"//span[@class='el-switch__core']").click()
# driver.find_element(By.XPATH,"//div[@class='oa-info']/div[2]/div[2]/div/div[3]/table/tbody/tr[1]/td[1]/div/label/span/span").click()
# time.sleep(5)
# driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[1]/div/div[3]/div[4]/div[2]/div[2]/div/div[4]/div[2]/table/tbody/tr/td[6]/div/span/button[1]/span').click()
# driver.find_element(By.XPATH,"//div[@class='bottom-text vertical-center']/label/span/span").click()
# driver.find_element(By.XPATH,"//span[contains(text(),'自动盖章')]").click()
# driver.find_element(By.XPATH,"//span[contains(text(),'通过')]").click()

#
# driver.find_element(By.XPATH, "//div[contains(text(),'供应商管理')]").click()
# driver.find_element(By.XPATH, "//div[@class='container-m']/header/form/div[3]/button[1]").click()
# driver.find_element(By.XPATH, "//div[@class='el-dialog__body']/header/form/div/div/input").send_keys("重庆帆舟运输有限公司")
# driver.find_element(By.XPATH, "//div[@class='el-dialog__body']/header/form/div[2]/button").click()
# driver.find_element(
# By.XPATH, '//*[@id="app"]/div[2]/div[1]/div/div[2]/div/div/div[4]/div/div/div[2]/main/div[1]/div[4]/div[2]/table/tbody/tr/td[1]/div/label/span/span').click()
# driver.find_element(By.XPATH, "//div[@class='table-list']/div[4]/div/div/div[3]/span/button[1]").click()






#实名认证
# driver.find_element(By.XPATH,"//div[@class='tag-inside']/ul[7]/li").click()
#
# driver.find_element(By.XPATH,"//div[contains(text(),'企业信息管理')]").click()
# driver.find_element(By.XPATH,"//span[contains(text(),'修改实名认证信息')]").click()
# driver.current_url
# try:
#     WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, "//div[@class='busiLice-list']/div/div/div/input")))
#     print("元素存在")
#     driver.find_element(By.XPATH, "//div[@class='busiLice-list']/div/div/div/input").send_keys(
#         filepath + '/data/营业执照.jpg')
# except:
#     print("元素不存在")
#driver.find_element(By.XPATH,"//div[@class='busiLice-list']/div/div/div/input").send_keys(filepath+'/data/营业执照.jpg')
                             #//div[@class='busiLice-list']/div/div/div/input

#time.sleep(5)

# s=Select(driver.find_element(By.XPATH,"//div[@class='distpicker-address-wrapper']/label[1]/select"))
# s.select_by_value("北京市")
#
# c=Select(driver.find_element(By.XPATH,"//div[@class='distpicker-address-wrapper']/label[2]/select"))
# c.select_by_value("北京市")
#
# t=Select(driver.find_element(By.XPATH,"//div[@class='distpicker-address-wrapper']/label[3]/select"))
# t.select_by_value("朝阳区")
#
# driver.find_element(By.XPATH,"//form[@class='el-form']/div[4]/div[1]/div/div/div/div/div/div[1]/div[1]/div/input").send_keys(filepath+'/data/身份证正面.jpg')
# time.sleep(3)
# driver.find_element(By.XPATH,"//form[@class='el-form']/div[4]/div[1]/div/div/div/div/div/div[2]/div[1]/div/input").send_keys(filepath+'/data/身份证背面.jpg')
# time.sleep(3)
# driver.find_element(By.XPATH,"//input[@placeholder='请输入法人手机号']").send_keys("17785425547")
#
# driver.find_element(By.XPATH,"//form[@class='el-form']/div[6]/div[1]/div/div/div/div/div/div[1]/div[1]/div/input").send_keys(filepath+'/data/身份证正面.jpg')
# time.sleep(3)
# driver.find_element(By.XPATH,"//form[@class='el-form']/div[6]/div[1]/div/div/div/div/div/div[2]/div[1]/div/input").send_keys(filepath+'/data/身份证背面.jpg')
# time.sleep(3)
# driver.find_element(By.XPATH,"//input[@placeholder='请输入联系人手机号']").send_keys("17785425547")
# driver.find_element(By.XPATH,"//input[@placeholder='请选择用户来源']").click()
# driver.find_element(By.XPATH,"//span[text()='上海公司']").click()




