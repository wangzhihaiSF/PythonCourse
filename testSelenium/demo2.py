"""selenium 与 BeautifulSoup 协作解析数据"""
import time

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://localprod.pandateacher.com/python-manuscript/hello-spiderman/")
time.sleep(5) # 等待两秒，等浏览器加缓冲载数据

pageSource = driver.page_source # 获取完整渲染的网页源代码
print(type(pageSource)) # 打印pageSource的类型
print(pageSource) # 打印pageSource
driver.close() # 关闭浏览器