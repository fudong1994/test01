from selenium import webdriver
import time

costomername = '橘子'
driver = webdriver.Chrome()  # 选择谷歌浏览器
url = 'http://uat-icbs-ifs.fehorizon.com/'
driver.get(url)  # 打开页面
driver.maximize_window()
time.sleep(3)