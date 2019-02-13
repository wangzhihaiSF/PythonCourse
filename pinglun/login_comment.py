import requests

url = "https://wordpress-edu-3autumn.localprod.forc.work/wp-login.php"
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}
data = {
    "log": "spiderman",
    "pwd": "crawler334566",
    "wp-submit": "登录",
    "redirect_to": "https://wordpress-edu-3autumn.localprod.forc.work",
    "testcookie": "1"
}
session = requests.session()
session.post(url, headers=headers, data=data) # post 登录
# cookies = login.cookies # 获取cookies

url_1 = 'https://wordpress-edu-3autumn.localprod.forc.work/wp-comments-post.php'
#我们想要评论的文章网址。
data_1 = {
'comment': input('请输入你想要发表的评论：'),
'submit': '发表评论',
'comment_post_ID': '23',
'comment_parent': '0'
}
#把有关评论的参数封装成字典。
comment = session.post(url_1,headers=headers,data=data_1)
#用requests.post发起发表评论的请求，放入参数：文章网址、headers、评论参数、cookies参数，赋值给comment。
#调用cookies的方法就是在post请求中传入cookies=cookies的参数。
print(comment.status_code)
#打印出comment的状态码，若状态码等于200，则证明我们评论成功。
print(comment)
