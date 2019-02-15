import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
time.sleep(3)
elem.clear()
elem.send_keys("pycon")
time.sleep(3)
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
time.sleep(4)
driver.close()