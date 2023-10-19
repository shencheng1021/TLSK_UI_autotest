# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: test
@time: 2022/4/13 9:34
"""
import os
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def locator_element(self,loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            print("页面中未能找到" +str(loc)+ "元素")


    def click(self,loc):
        try:
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.locator_element(loc))).click()
        except:
            print(str(loc)+"元素不可点击")

    def send_keys(self,loc,key):
        self.locator_element(loc).send_keys(key)

    #定义进框架的关键字
    def goto_iframe(self,id):
        self.driver.switch_to.frame(id)
    #定义出框架的关键字
    def quit_iframe(self):
        self.driver.switch_to.default_content()

    def goto_url(self,url):
        self.driver.get(url)

    def get_text(self,loc):
        return self.locator_element(loc).text

    def select_value(self,loc,value):
        s=Select(self.locator_element(loc))
        s.select_by_value(value)

    def upload_file(self,loc,filepath):
        relativepath=os.path.dirname(__file__).split("base1")[0]+'/data/'
        self.send_keys(loc,relativepath+filepath)

    #定义弹窗确认的关键字
    def alert_accept(self):
        alert=self.driver.switch_to.alert
        alert.accept()

    # 定义弹窗取消的关键字
    def alert_dismiss(self):
        alert=self.driver.switch_to.alert
        alert.dismiss()

    # 定义获取弹窗文本的关键字
    def alert_text(self):
        alert = self.driver.switch_to.alert
        return alert.text

    #定义在弹窗上输入内容
    def alert_send_keys(self,key):
        alert = self.driver.switch_to.alert
        alert.send_keys(key)

    #显示等待
    #定义判断某个元素是否被加到了 dom 树里
    def presence_of_element_located(self,loc):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located(loc))

    #判断某个元素中是否不存在于dom树或不可见
    def invisibility_of_element_located(self,loc):
        WebDriverWait(self.driver,10).until(EC.invisibility_of_element_located(loc))

    #定义一直等待某元素可见，默认超时10秒的关键字
    def visibility_of_element_located(self,loc):
        text=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc)).text
        return text






