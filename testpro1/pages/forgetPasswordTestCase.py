#!/usr/bin/env python3
# -*- coding=utf-8 -*-

"""
测试代理商忘记密码界面
"""

import sys
sys.path.append('./model')
sys.path.append('./page_obj')
from time import sleep
import unittest
from page_obj.forgetPasswordPage import ForgetPassword
import os
from HtmlTestRunner import HTMLTestRunner
from model import myfunction,myunittest


class ForgetPasswordTest(myunittest.MyTest):
    def test_forgetpwd_001_verify_all_empty(self):
        account = ''
        certificateno = ''
        username = ''
        po = ForgetPassword(self.browser)
        po.verify_action(account, certificateno, username)
        self.assertEqual(po.alert_error_hint(),'代理商账号/登录号不能为空！')
        
    def test_forgetpwd_002_verify_certificateno_empty(self):
        account = 'A0000000000001'
        certificateno = ''
        username = ''
        po = ForgetPassword(self.browser)
        po.verify_action(account, certificateno, username)
        self.assertEqual(po.alert_error_hint(),'证件号码不能为空！')            
    
    def test_forgetpwd_003_verify_username_empty(self):
        account = 'A0000000000001'
        certificateno = '12'
        username = ''
        po = ForgetPassword(self.browser)
        po.verify_action(account, certificateno, username)
        self.assertEqual(po.alert_error_hint(),'操作员帐号不能为空')      
        
    def test_forgetpwd_004_verify_account_wrong(self):
        account = 'A0000000000000'
        certificateno = '1'
        username = '1'
        po = ForgetPassword(self.browser)
        po.verify_action(account, certificateno, username)
        self.assertEqual(po.alert_error_hint(),'Agent No is incorrect, please input again!')   
        
    def test_forgetpwd_005_verify_certificateno_wrong(self):
        account = 'A0000000000001'
        certificateno = '0'
        username = '1'
        po = ForgetPassword(self.browser)
        po.verify_action(account, certificateno, username)
        self.assertEqual(po.alert_error_hint(),'Certificate No is incorrect, please input again!')   
        
    def test_forgetpwd_006_verify_username_wrong(self):
        account = 'A0000000000001'
        certificateno = '123333'
        username = '1'
        po = ForgetPassword(self.browser)
        po.verify_action(account, certificateno, username)
        self.assertEqual(po.alert_error_hint(),'The operator does not exist, please input again!') 
        
    def test_forgetpwd_007_verify_all_succeed(self):
        account = 'A0000000000001'
        certificateno = '123333'
        username = 'admin'
        po = ForgetPassword(self.browser)
        po.verify_action(account, certificateno, username)
        self.assertEqual(po.driver.current_url,po.base_url + 'html/design/findPwd2.jsp')   
        
    def test_forgetpwd_008_submit_type_empty(self):
        account = 'A0000000000001'
        certificateno = '123333'
        username = 'admin'
        po = ForgetPassword(self.browser)
        po.verify_action(account, certificateno, username)
        search_type = ''
        email = ''
        po.submit_action(search_type, email)
        self.assertEqual(po.alert_error_hint(),'请选择找回登录密码方式')   
        
    def test_forgetpwd_009_submit_email_empty(self):
        account = 'A0000000000001'
        certificateno = '123333'
        username = 'admin'
        po = ForgetPassword(self.browser)
        po.verify_action(account, certificateno, username)
        search_type = '1'
        email = ''
        po.submit_action(search_type, email)
        self.assertEqual(po.alert_error_hint(),'邮箱格式不正确，请确认后再输！') 
        
    def test_forgetpwd_010_submit_email_error(self):
        account = 'A0000000000001'
        certificateno = '123333'
        username = 'admin'
        po = ForgetPassword(self.browser)
        po.verify_action(account, certificateno, username)
        search_type = '1'
        email = '12@@@'
        po.submit_action(search_type, email)
        self.assertEqual(po.alert_error_hint(),'邮箱格式不正确，请确认后再输！') 
            
    def test_forgetpwd_011_submit_email_wrong(self):
        account = 'A0000000000001'
        certificateno = '123333'
        username = 'admin'
        po = ForgetPassword(self.browser)
        po.verify_action(account, certificateno, username)
        search_type = '1'
        email = '12@qq.com'
        po.submit_action(search_type, email)
        self.assertEqual(po.alert_error_hint(),'邮箱输入不正确！') 
        
    def test_forgetpwd_012_submit_all_succeed(self):
        account = 'A0000000000001'
        certificateno = '123333'
        username = 'admin'
        po = ForgetPassword(self.browser)
        po.verify_action(account, certificateno, username)
        search_type = '1'
        email = '12@qq.com'
        po.submit_action(search_type, email)
        self.assertEqual(po.alert_error_hint(),'Send successfully') 
        
if __name__ == '__main__':    
    forget_password_test = unittest.TestLoader().loadTestsFromTestCase(ForgetPasswordTest)
    test_suite = unittest.TestSuite([forget_password_test])
    base_dir = str(os.path.abspath(os.path.dirname(os.getcwd())))
    file_path = base_dir + "\\report\\"
    print(file_path)    
    testrunner = HTMLTestRunner(output=file_path,report_title='Test Report',report_name='Test')
    testrunner.run(test_suite)