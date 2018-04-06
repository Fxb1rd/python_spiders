#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2017-12-26 15:43:19
# @Author  : Marte (iqianduan@126.com)
# @Link    : http://www.iqianduan.cn
# @Version : $Id$

import requests
import re
import time

"""bilibili弹幕"""

#视频地址 https://www.bilibili.com/video/av17480312
#弹幕地址 https://comment.bilibili.com/dmroll,1513785600,28547920
url = 'https://comment.bilibili.com/rolldate,28547920'

#获得弹幕id 28547920
video_id = url.split(',')[-1]
print(video_id)

#获得json
html = requests.get(url)

time_list = [i['timestamp']for i in html.json()]

# 获取弹幕网址格式 'https://comment.bilibili.com/dmroll,时间戳,弹幕号'
#

for i in time_list:
    content = ''
    j = 'https://comment.bilibili.com/dmroll,{0},{1}'.format(i, video_id)
    print(j)
    text = requests.get(j).text
    # 匹配弹幕内容
    res = re.findall('<d p=".*?">(.*?)</d>', text)
    # 将时间戳转化为日期形式,需要把字符串转为整数
    timeArray = time.localtime(int(i))
    data_time = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    print(data_time)

    content += data_time + '\n'

    for k in res:
        content += k + '\n'

    file_path = 'txt/{}.txt'.format(time.strftime("%Y_%m_%d", timeArray))
    print(file_path)
    with open(file_path, mode='w+', encoding='utf8') as f:
        f.write(content)