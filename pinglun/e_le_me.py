import requests
session = requests.session()

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
url_1 = 'https://h5.ele.me/restapi/eus/login/mobile_send_code'
tel = input('请输入手机号码：')
data_1 = {'captcha_hash':'',
        'captcha_value':'',
        'mobile':tel,
        'scf':''}

token_dic = session.post(url_1, headers=headers, data=data_1).json()
token = token_dic.get("validate_token")
print(token)

url_2 = 'https://h5.ele.me/restapi/eus/login/login_by_mobile'
validate_code = input('请输入手机验证码：')
data_2 = {
    'mobile':tel,
    'scf':'ms',
    'validate_code':validate_code,
    'validate_token':token
}

session.post(url_2,headers=headers,data=data_2)


address_url = 'https://www.ele.me/restapi/v2/pois?'
place = input('请输入你的收货地址：')
params = {'extras[]':'count','geohash':'ws105rz9smwm','keyword':place,'limit':'20','type':'nearby'}
# 这里使用了深圳的geohash

address_res = requests.get(address_url,params=params)
address_json = address_res.json()

print('以下，是与'+place+'相关的位置信息：\n')
n=0
for address in address_json:
    print(str(n)+'. '+address['name']+'：'+address['short_address']+'\n')
    n = n+1
address_num = int(input('请输入您选择位置的序号：'))
final_address = address_json[address_num]
