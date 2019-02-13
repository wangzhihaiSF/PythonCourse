import requests
import openpyxl

url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'

wb = openpyxl.Workbook()
sheet2 = wb.active
sheet2.title = "song"
listName = ["歌曲名", "所属专辑", "歌曲时长", "歌曲链接"]
sheet2.append(listName)

for x in range(5):
    # 将参数封装为字典
    params = {
        'ct': '24',
        'qqmusic_ver': '1298',
        'new_json': '1',
        'remoteplace': 'sizer.yqq.song_next',
        'searchid': '64405487069162918',
        't': '0',
        'aggr': '1',
        'cr': '1',
        'catZhida': '1',
        'lossless': '0',
        'flag_qc': '0',
        'p': str(x + 1),
        'n': '20',
        'w': '周杰伦',
        'g_tk': '5381',
        'loginUin': '0',
        'hostUin': '0',
        'format': 'json',
        'inCharset': 'utf8',
        'outCharset': 'utf-8',
        'notice': '0',
        'platform': 'yqq.json',
        'needNewCode': '0'
    }
    # 调用get方法，下载这个列表
    res_music = requests.get(url, params=params)
    # 使用json()方法，将response对象，转为列表/字典
    json_music = res_music.json()
    # 一层一层地取字典，获取歌单列表
    list_music = json_music['data']['song']['list']


    # list_music是一个列表，music是它里面的元素
    for music in list_music:
        # 以name为键，查找歌曲名，把歌曲名赋值给name
        name = music['name']
        # 查找专辑名，把专辑名赋给album
        album = music['album']['name']
        # 查找播放时长，把时长赋值给time
        time = music['interval']
        # 查找播放链接，把链接赋值给link
        link = 'https://y.qq.com/n/yqq/song/' + str(music['file']['media_mid']) + '.html\n\n'
        # 把name、album、time和link写成列表，用append函数多行写入Excel
        sheet2.append([name, album, time, link])

        print('歌曲名：' + name + '\n' + '所属专辑:' + album + '\n' + '播放时长:' + str(time) + '\n' + '播放链接:' + link)

wb.save('Jay.xlsx')
