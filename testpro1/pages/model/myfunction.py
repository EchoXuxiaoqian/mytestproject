#!/usr/bin/env python3
# -*- coding=utf-8 -*-

from selenium import webdriver
import os,time

def save_screenshot(driver,file_name):
    base_dir = str(os.path.abspath(os.path.dirname(os.getcwd())))
    file_path = base_dir + "\\report\\image\\" + file_name
    print(file_path)
    driver.get_screenshot_as_file(file_path)
    
if __name__ == "__main__":  
    driver = webdriver.Chrome('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe') 
    driver.get("https://cn.bing.com/")
    driver.find_element_by_id('sb_form_q').send_keys("unittest")  
    driver.find_element_by_id('sb_form_go').click()    # 模拟点击    
    time.sleep(5)
    save_screenshot(driver,'test.png')
    driver.close()
              
    