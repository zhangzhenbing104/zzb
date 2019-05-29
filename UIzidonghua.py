# encoding:utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
driver.maximize_window()
driver.get("http://42.159.251.106:8881/hqls/login/login.html")
# 登录账号和密码
driver.find_element_by_id("logname").clear()
driver.find_element_by_id("logname").send_keys('15950562303')
driver.find_element_by_id("logpass").clear()
driver.find_element_by_id("logpass").send_keys('123456')
time.sleep(1)
driver.find_element_by_css_selector("#login_button").click()
time.sleep(2)
driver.find_element_by_css_selector("#hq_menu > li:nth-child(2) > a").click()
driver.find_element_by_xpath("//*[@id='hq_menu']/li[2]/dl/dd[1]/a").click()
time.sleep(3)
# driver.find_element_by_css_selector("#addStore").click()
# time.sleep(2)
# driver.find_element_by_css_selector("#storeTree > li > a > cite").click()
# time.sleep(4)
# # driver.find_element_by_xpath("//*[@id='layui-layer5']/div[3]/a[1]").click()
# driver.find_element_by_css_selector("#layui-layer2 > div.layui-layer-btn.layui-layer-btn- > a.layui-layer-btn0").click()
# time.sleep(5)
###############################
driver.find_element_by_css_selector("#storeClass").click()
time.sleep(2)
driver.find_element_by_css_selector("#storeClass > option:nth-child(3)").clear()