from selenium import webdriver
#导入WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
import time

drive = webdriver.Chrome()
drive.get("http://www.baidu.com/")

#WebDriverWait方法
element = WebDriverWait(drive,10).until(lambda drive:drive.find_element_by_id("kw"))
element.send_keys("uniquefu")

#添加智能等待
drive.implicitly_wait(10)
drive.find_element_by_id("su").click()

#添加固定等待时间
time.sleep(10)
drive.quit()

