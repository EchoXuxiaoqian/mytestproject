#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""
代理商忘记密码界面
封装1.代理商账号、操作员账号、证件号码文本框；2.下一步按钮；3.提示信息；4.邮箱手机单选框；5.邮箱手机文本框；6.提交按钮
"""

from base import Page
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

class ForgetPassword(Page):
    url = "/html/design/findPwd1.jsp"
    # 代理商账号/登录号的定位
    account_input_loc = (By.ID,'merno')
    # 操作员账号的定位
    username_input_loc = (By.ID,'oper') 
    # 证件号码的定位
    certificateno_input_loc = (By.ID,'cerno')    
    # 下一步按钮的定位
    next_button_loc= (By.CLASS_NAME,'anf_fan')    
    # 邮箱手机单选框的定位
    email_radio_loc = (By.ID,'search_type1')
    phone_radio_loc = (By.ID,'search_type2')
    # 邮箱的定位
    email_input_loc = (By.ID,'mail1')
    # 提交按钮的定位
    submit_button_loc = (By.ID,'subd1')
    
    def account(self,account):
        self.find_element(*self.account_input_loc).clear()
        self.find_element(*self.account_input_loc).send_keys(account)       
        
    def certificateno(self,certificateno):
        self.find_element(*self.certificateno_input_loc).clear()
        self.find_element(*self.certificateno_input_loc).send_keys(certificateno) 
        
    def username(self,username):
        self.find_element(*self.username_input_loc).clear()
        self.find_element(*self.username_input_loc).send_keys(username)     
        
    def alert_error_hint(self):
        hint = Alert(self.driver).text
        Alert(self.driver).accept() # 不关闭的话执行error，关闭的话截图无法查看到提示信息
        return hint
    
    def next_button(self):
        self.find_element(*self.next_button_loc).click()    
        
    def verify_action(self,account,certificateno,username):
        self.open()
        self.account(account)
        self.certificateno(certificateno)
        self.username(username)
        self.next_button()     
    
    def email_radio(self):
        self.find_element(*self.email_radio_loc).click()   
        
    def email(self,username):
        self.find_element(*self.email_input_loc).clear()
        self.find_element(*self.email_input_loc).send_keys(email)     
            
    def submit_button(self):
        self.find_element(*self.submit_button_loc).click()    
    
    def submit_action(self,search_type,email):
        if search_type == '1':
            self.email_radio()
            self.email(email)
        self.submit_button()