'''
Author: conan0220 conanhuang8382@gmail.com
Date: 2022-12-07 21:48:58
LastEditors: conan0220 conanhuang8382@gmail.com
LastEditTime: 2022-12-07 22:14:25
FilePath: /2022CAD-E/home/conan/repos/automation_click/src/auto.py
Description: 

Copyright (c) 2022 by conan0220 conanhuang8382@gmail.com, All Rights Reserved. 
'''
# 載入需要的套件
from selenium import webdriver

# 開啟瀏覽器視窗(Chrome)
# 方法一：執行前需開啟chromedriver.exe且與執行檔在同一個工作目錄
driver = webdriver.Chrome()

driver.get("http://www.google.com") # 更改網址以前往不同網頁
# # 定位搜尋框
# element = driver.find_element_by_class_name("gLFyf.gsfi")
# # 傳入字串
# element.send_keys("Selenium Python")