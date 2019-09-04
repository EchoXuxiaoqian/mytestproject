#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import unittest,time
from HtmlTestRunner import HTMLTestRunner
import sys,os
sys.path.append('./testpro1/pages/model')  # 需要把引用到的模块的路径加到sys的path里
sys.path.append('./testpro1/pages/page_obj')

if __name__ == '__main__':
    
    allcase = unittest.defaultTestLoader.discover('./testpro1/pages', pattern='*TestCase.py') # 在指定路径下搜索指定名称格式的文件，加载到testsuite里
    base_dir = str(os.getcwd())
    file_path = base_dir + "\\testpro1\\report\\" 
    testrunner = HTMLTestRunner(output=file_path,report_title='测试报告',report_name='Test Report',template='report_template.html') # 自定义测试报告模板
    # 问题：1.输出的报告中文乱码 ————> 报告的编码格式非utf-8，需要将编码转换为utf-8，直接生成utf-8编码格式的方法未找到
    testrunner.run(allcase)    