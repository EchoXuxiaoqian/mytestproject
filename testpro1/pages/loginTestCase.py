#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""
测试代理商界面登录
"""
import sys
sys.path.append('./model')
sys.path.append('./page_obj')  

from time import sleep
import unittest
from page_obj.loginPage import Login
import os
from HtmlTestRunner import HTMLTestRunner
from model import myfunction,myunittest

class LoginTest(myunittest.MyTest):
    def test_login_all_empty(self):
        account = ''
        username = ''
        password = ''
        vercode = ''
        po = Login(self.browser)
        po.login_action(account, username, password, vercode)
        error = po.login_error_hint()
        print(error)
        self.assertEqual(po.login_error_hint(),'请输入代理商账号或登录号1！')
        
    def test_login_username_empty(self):
        account = 'A0000000000001'
        username = ''
        password = ''
        vercode = ''
        po = Login(self.browser)
        po.login_action(account, username, password, vercode)
        self.assertEqual(po.login_error_hint(),'请输入代理商操作员账号！')   
        
    def ntest_login_password_empty(self):
        account = 'A0000000000001'
        username = 'admin'
        password = ''
        vercode = ''
        po = Login(self.browser)
        po.login_action(account, username, password, vercode)
        self.assertEqual(po.login_error_hint(),'密码不能为空！')  
        
    def ntest_login_vercode_empty(self):
        account = 'A0000000000001'
        username = 'admin'
        password = 'hx888888'
        vercode = ''
        po = Login(self.browser)
        po.login_action(account, username, password, vercode)
        self.assertEqual(po.login_error_hint(),'请输入四位验证码！')    
        
    def ntest_login_vercode_wrong(self):
        account = 'A0000000000001'
        username = 'admin'
        password = 'hx888888'
        vercode = '1234'
        po = Login(self.browser)
        po.login_action(account, username, password, vercode)
        self.assertEqual(po.login_error_hint(),'验证码输入有误，请重新输入验证码！')     
        
if __name__ == '__main__':
    # unittest.main()
    # unittest.main(testRunner=HTMLTestRunner(output='example_dir')) # 使用默认的报告模板
    
    login_test = unittest.TestLoader().loadTestsFromTestCase(LoginTest) # 测试类里的方法不一定按测试函数的编写顺序执行，和函数名有关
    test_suite = unittest.TestSuite([login_test]) 
    base_dir = str(os.path.abspath(os.path.dirname(os.getcwd())))
    file_path = base_dir + "\\report\\"
    print(file_path)    
    testrunner = HTMLTestRunner(output=file_path,report_title='Test Report',report_name='Test')
    testrunner.run(test_suite)