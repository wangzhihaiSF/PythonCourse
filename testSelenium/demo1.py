import time
from selenium import webdriver
"""
selenium它可以真实地打开一个浏览器，
等待所有数据都加载到Elements中之后，再把这个网页当做静态网页爬取就好了。
"""

driver = webdriver.Chrome()
# 当一个网页被打开，网页中的数据就加载到了浏览器中，也就是说，数据被我们获取到了。
driver.get("https://localprod.pandateacher.com/python-manuscript/hello-spiderman/")
time.sleep(5)
label = driver.find_elements_by_tag_name("label") # 解析网页并提取第一个<label>标签
print(label)
for i in label:
    print(i.text)# 打印label的文本
driver.close()