# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: test
@time: 2022/4/13 9:34
"""
import logging
import os
import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.logger_util import Logger

log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)


class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def locator_element(self,loc):
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located(loc))
        except:
            log.logger.exception("页面中未能找到 %s 元素" % str(loc),exc_info=True)
            raise
        else:
            log.logger.info("成功定位 %s 元素" % str(loc))
            return self.driver.find_element(*loc)

    def click(self,loc):
        try:
            element=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.locator_element(loc)))
        except:
            log.logger.exception(str(loc)+"元素不可点击",exc_info=True)
            #print(str(loc)+"元素不可点击")
            raise
        else:
            log.logger.info("成功点击"+str(loc)+"元素")
            element.click()


    def send_keys(self,loc,key):
        try:
            self.locator_element(loc).send_keys(key)
        except Exception:
            log.logger.exception(str(loc)+"元素输入框，无法输入值",exc_info=True)
            raise
        else:
            log.logger.info("[%s]元素输入框，输入值[%s]" % (str(loc),key))
    #定义进框架的关键字
    def goto_iframe(self,id):
        self.driver.switch_to.frame(id)

    #定义出框架的关键字
    def quit_iframe(self):
        self.driver.switch_to.default_content()

    #定义进入指定url的关键字
    def goto_url(self,url):
        try:
            self.driver.get(url)
            assert self.get_url() == url
        except Exception as e:
            log.logger.exception("打开[%s]链接失败" % url,exc_info=True)
            raise e
        else:
            log.logger.info("打开[%s]链接成功" % url)
    def get_text(self,loc):
        try:
            value=self.locator_element(loc).text
            # return self.locator_element(loc).text
        except Exception:
            log.logger.exception("[%s]获取文本失败",exc_info=True)
            raise
        else:
            log.logger.info("[%s]获取文本成功，文本值为[%s]" % (str(loc),value))
            return value

    #定义下拉列表选择的关键字
    def select_value(self,loc,value):
        s=Select(self.locator_element(loc))
        s.select_by_value(value)

    def upload_file(self,loc,filename):
        relativepath=os.path.dirname(__file__).split("base1")[0]+'/data/'
        self.send_keys(loc,relativepath+filename)
        time.sleep(3)

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

    #定义获取当前页面url的关键字
    def get_url(self):
        return self.driver.current_url

    #显示等待
    #定义判断某个元素是否被加到了 dom 树里
    def presence_of_element_located(self,loc):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located(loc))

    #判断某个元素中是否不存在于dom树或不可见
    def invisibility_of_element_located(self,loc):
        WebDriverWait(self.driver,10).until(EC.invisibility_of_element_located(loc))

    #定义一直等待某元素可见，并返回定位元素中的文本,默认超时10秒的关键字
    def is_visible_text(self,loc):
        try:
            value=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc)).text
        except Exception:
            log.logger.exception('[%s]元素不可见' % str(loc),exc_info=True)
        else:
            log.logger.info('[%s]元素可见并返回文本[%s]' % (str(loc),value))
            return value

    # 定义一直等待某元素可见,默认超时10秒
    def is_visible(self,loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
        except TimeoutException:
            log.logger.exception('等待[%s]元素出现失败' % str(loc),exc_info=True)
            return False
        else:
            log.logger.info('等待[%s]元素出现成功' % str(loc))
            return True

    # 定义一直等待某元素不可见,默认超时10秒
    def is_not_visible(self,loc,timeout):
        try:
            WebDriverWait(self.driver,timeout).until_not(EC.visibility_of_element_located(loc))
        except TimeoutException:
            log.logger.exception('等待[%s]元素消失失败' % str(loc),exc_info=True)
            return False
        else:
            log.logger.info('等待[%s]元素消失成功' % str(loc))
            return True







