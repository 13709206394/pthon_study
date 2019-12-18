from selenium import webdriver
import time

driver =webdriver.Chrome()
driver.maximize_window()
time.sleep(3)
driver.get("http:\\www.baidu.com")
driver.find_element_by_id("kw").send_keys("国庆")
driver.find_element_by_id("su").click()

