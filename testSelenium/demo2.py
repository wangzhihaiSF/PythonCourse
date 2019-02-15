"""selenium 与 BeautifulSoup 协作解析数据"""
import time

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome()
driver.get("https://localprod.pandateacher.com/python-manuscript/hello-spiderman/")
time.sleep(3) # 等待两秒，等浏览器加缓冲载数据

pageSource = driver.page_source # 获取完整渲染的网页源代码
print(type(pageSource)) # 打印pageSource的类型
print(pageSource) # 打印pageSource
teacher_input = driver.find_element_by_id("teacher")
teacher_input.send_keys("吴枫")
assistant_input = driver.find_element_by_class_name("assistant")
assistant_input.send_keys("酱酱")
button = driver.find_element_by_class_name("sub")
time.sleep(2)
button.click()
time.sleep(3)
driver.close() # 关闭浏览器