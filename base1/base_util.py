# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: test
@time: 2022/4/13 9:34
"""
import logging
import time
import unittest
from selenium import webdriver

from common.logger_util import Logger
from selenium.webdriver.chrome.options import Options


log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)

class BaseUtil:


    def setup_method(self) -> None:
        global driver
        chrome_options = Options()
        chrome_options.add_argument('--headless') # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
        chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
        chrome_options.add_argument('--disable-dev-shm-usage') # 大量渲染时候写入/tmp而非/dev/shm
        chrome_options.add_argument('--disable-gpu') # 谷歌文档提到需要加上这个属性来规避bug
        chrome_options.add_argument('-–single-process')  #以单进程模式运行 Chromium。（启动时浏览器会给出不安全警告）
        chrome_options.add_argument('window-size=1920x1080')  # 指定浏览器分辨率
        chrome_options.add_argument('--start-maximized')  # 最大化运行（全屏窗口）,不设置，取元素会报错
        chrome_options.add_argument('--user-data-dir=/home/jenkins/data')
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        self.driver = webdriver.Chrome(options=chrome_options, executable_path='/usr/bin/chromedriver')
        #self.driver = webdriver.Chrome(options=chrome_options)
        # self.driver = webdriver.Chrome()
        driver = self.driver
        #self.driver.implicitly_wait(10)
        self.driver.get('http://172.24.100.75:10006/#/login')
        self.driver.maximize_window()
        log.logger.info('************************starting run test cases************************')

    def teardown_method(self) -> None:
        self.driver.quit()
        log.logger.info('************************test case run completed************************')