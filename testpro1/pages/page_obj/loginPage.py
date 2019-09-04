#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""
代理商登录界面
封装1.代理商账号、操作员账号、登录密码、验证码文本框；2.登录按钮；3.提示信息
"""
from base import Page
from selenium.webdriver.common.by import By
from selenium import webdriver


class Login(Page):
    url = "/html/design/index.jsp"
    # 代理商账号/登录号的定位
    account_input_loc = (By.ID,'ACCOUNT')
    # 操作员账号的定位
    username_input_loc = (By.ID,'USER_ID') 
    # 登录密码的定位
    password_input_loc = (By.ID,'USER_PWD')
    # 验证码的定位
    vercode_input_loc = (By.ID,'VERCODE')
    # 登录按钮的定位
    login_button_loc= (By.CLASS_NAME,'logo_but')
    # 错误提示的定位
    login_wrong_loc = (By.ID,'login_wrong')
    # 英文语言选择的定位 ?
    # en_language_loc = (By.XPATH,"//span[@id='language']/ul/li[1]")
    # 忘记密码链接的定位
    forget_password_loc = (By.LINK_TEXT,'/agent/html/design/findPwd1.jsp')
    
    def account(self,account):
        self.find_element(*self.account_input_loc).clear()
        self.find_element(*self.account_input_loc).send_keys(account)
        
    def username(self,username):
        self.find_element(*self.username_input_loc).clear()
        self.find_element(*self.username_input_loc).send_keys(username)    
        
    def password(self,password):
        self.find_element(*self.password_input_loc).clear()
        self.find_element(*self.password_input_loc).send_keys(password)       
        
    def vercode(self,vercode):
        self.find_element(*self.vercode_input_loc).clear()
        self.find_element(*self.vercode_input_loc).send_keys(vercode)       
        
    def login_button(self):
        self.find_element(*self.login_button_loc).click()
        
    def login_error_hint(self):
        return self.find_element(*self.login_wrong_loc).text
        
    #def change_language_en(self):
        #self.find_element(*self.en_language_loc).click()
        
    def login_action(self,account,username,password,vercode):
        self.open()
        self.account(account)
        self.username(username)
        self.password(password)
        self.vercode(vercode)
        self.login_button()
    def goto_forget_password(self):
        self.find_element(*self.forget_password_loc).click()