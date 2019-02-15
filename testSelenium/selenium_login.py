import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://wordpress-edu-3autumn.localprod.forc.work/wp-login.php")
# page_source = driver.page_source
# print(page_source)
time.sleep(2)
name_input = driver.find_element_by_id("user_login")
name_input.send_keys("spiderman")
pwd_input = driver.find_element_by_id("user_pass")
pwd_input.send_keys("crawler334566")
submit_button = driver.find_element_by_id("wp-submit")
submit_button.click()
# page_source = driver.page_source
# print(page_source)
link = driver.find_element_by_partial_link_text("同九义何汝秀").get_attribute("href")
driver.get(link)
print(driver.page_source)
textarea = driver.find_element_by_id("comment")
textarea.send_keys("2019.2.14 selenium 测试发表评论 hahah ")
submit = driver.find_element_by_class_name("submit")
submit.click()
driver.close()