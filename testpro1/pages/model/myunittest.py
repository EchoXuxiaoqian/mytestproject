#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from selenium import webdriver
import unittest,time,os
from driver import browser
from myfunction import save_screenshot

class MyTest(unittest.TestCase):
    global case_count
    case_count = 0
    
    @classmethod
    def setUpClass(self):  # setUpClass,必须使用@classmethod 装饰器,所有test运行前运行一次
        self.browser = browser()
        self.browser.maximize_window     
        #self.browser.implicitly_wait(10)
    
    @classmethod
    def tearDownClass(self):
        self.browser.close()
    
    def setUp(self):    # 每个test函数运行前运行
        global case_count
        case_count += 1
        
    def tearDown(self):
        now_time = time.strftime("%Y%m%d%H%M%S")
        file_name = now_time + self.__class__.__name__ +".png"
        #save_screenshot(self.browser, file_name)
        

if __name__ == "__main__":
    class Test(MyTest):
        def test_case(self):
            self.browser.get("https://cn.bing.com/")
            self.browser.find_element_by_id('sb_form_q').send_keys("unittest")  
            self.browser.find_element_by_id('sb_form_go').click()    # 模拟点击
            time.sleep(2) # 等待1秒            
    unittest.main()