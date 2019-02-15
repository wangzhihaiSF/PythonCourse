import requests
from bs4 import BeautifulSoup
#引入requests库和BeautifulSoup库
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
#封装headers
url='http://www.weather.com.cn/weather/101010300.shtml'
#把URL链接赋值到变量url上。
res=requests.get(url,headers=headers)
res.encoding="utf-8"
print(res.text)
#打印出res对象的网页源代码
soup = BeautifulSoup(res.text, "html.parser")
weather_tag_list = soup.find(id="7d").find("ul", class_="clearfix").find_all("li")
# print(weather_tag_list)
date_list = []
weather_list = []
tem_list = []
wind_list = []
for item in weather_tag_list:
    date = item.find("h1").text
    date_list.append(date)
    weather = item.find(class_="wea").text
    weather_list.append(weather)
    tem = ""
    tem_f = item.find(class_="tem").find("span").text
    tem_b = item.find(class_="tem").find("i").text
    tem = tem_f + "/" + tem_b
    tem_list.append(tem)
    wind = item.find(class_="win").find("i").text
    wind_list.append(wind)
print(date_list)
print(weather_list)
print(tem_list)
print(wind_list)

import smtplib
mailHost = "smtp.qq.com" # 服务器地址
qqMail = smtplib.SMTP() # 实例化 SMTP 对象
qqMail.connect(mailHost, 25) # 连接服务器

account = "1599315665"
pwd = input("请输入密码") # 授权码
qqMail.login(account, pwd) # 登录

receiver = "wangzhihai_sf@163.com"

from email.mime.text import MIMEText
from email.header import Header

content = input("邮件正文")
# 实例化一个 MIMEText 邮件对象类，三个参数
# 分别是邮件正文，文本格式和编码.
message = MIMEText(content, "plain", "utf-8")
print(type(message))
subject = "天气情况" # 邮件主题
# 实例化了一个Header邮件头对象，该对象需要写入两个参数，分别是邮件主题和编码
message["Subject"] = Header(subject, "utf-8")
try:
    qqMail.sendmail(account, receiver, message.as_string())
    print("邮件发送成功")
except:
    print("邮件发送失败！")
qqMail.quit()