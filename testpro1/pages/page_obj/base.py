#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException

class Page(object):
    base_url = "http://192.168.6.54:8866/agent/";
    
    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
            return True
        except NoAlertPresentException as e:
            return False
    
    def __init__(self, driver,base_url=base_url):
        self.driver = driver
        self.base_url = base_url
        self.timeout = 30
    
    def _open(self,url):
        url_ = self.base_url + url
        self.driver.get(url_)
        if(self.is_alert_present()):
            webdriver.common.alert.Alert(self.driver).accept() # 接收弹框提示        
        assert self.driver.current_url == url_ , 'failed open page %s' % url_
    def open(self):
        self._open(self.url)
        
    # *loc参数个数不是固定 *loc = (By.ID,"kw")
    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    def iframe(self,iframeid):
        return self.driver.switch_to.frame(iframeid)

    def iframe_out(self):
        return self.driver.switch_to.default_content()

    def script(self,src):
        return self.driver.execute_script(src)    