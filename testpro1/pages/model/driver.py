#!/usr/bin/env python3
# -*- coding -*-

from selenium import webdriver

def browser():
    driver = webdriver.Chrome('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe') 
    return driver

if __name__ == '__main__':
    browser()