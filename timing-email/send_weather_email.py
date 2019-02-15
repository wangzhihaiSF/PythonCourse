import time

import requests
import schedule
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.header import Header

account = "1599315665@qq.com"
password = input("请输入密码") # 授权码
receiver = "wangzhihai_sf@163.com"

def get_weather_data():
    headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    url="http://www.weather.com.cn/weather/101010300.shtml"
    res = requests.get(url, headers=headers)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    tem1 = soup.find(class_='tem')
    weather1 = soup.find(class_='wea')
    tem = tem1.text
    weather = weather1.text
    return tem, weather


def send_email(tem, weather):
    global account, password, receiver
    mailhost = 'smtp.qq.com'
    qqmail = smtplib.SMTP()
    qqmail.connect(mailhost, 25)
    qqmail.login(account, password)
    content = tem + weather
    message = MIMEText(content, 'plain', 'utf-8')
    subject = '今日天气预报'
    message['Subject'] = Header(subject, 'utf-8')
    try:
        qqmail.sendmail(account, receiver, message.as_string())
        print('邮件发送成功')
    except:
        print('邮件发送失败')
    qqmail.quit()


def job():
    print('开始一次任务')
    tem, weather = get_weather_data()
    send_email(tem, weather)
    print('任务完成')


schedule.every().day.at("15:23").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)