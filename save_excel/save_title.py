import openpyxl, requests

url = "https://www.zhihu.com/api/v4/members/zhang-jia-wei/articles?"
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
parameters = {
    "include": "data[*].comment_count,suggest_edit,is_normal,thumbnail_extra_info,thumbnail,can_comment,comment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followees,voting,review_info,is_labeled,label_info;data[*].author.badge[?(type=best_answerer)].topics",
    "offset": "10",
    "limit": "10",
    "sort_by": "voteups"
}
response = requests.get(url, headers=headers, params=parameters)
print(response.status_code)

articles=response.json()
listSource = articles.get("data")
titles = []
for item in listSource:
    title = item.get("title")
    print(title)
    titles.append(title)



#用json()方法去解析response对象，并赋值到变量articles上面。
# print(articles)
# 打印这个json文件
# 确认请求成功

# wb = openpyxl.Workbook()
# sheet = wb.active
# sheet.title = "title"
