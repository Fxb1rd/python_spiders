#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2018-01-21 20:36:13
# @Author  : fxb1rd (w1589534127@outlook.com)
# @Link    : http://
# @Version : $Id$

import requests
import re
import sys

# sys.setdefaultencoding('utf-8')  # 输入内容为 utf-8编码

def opener(page):
    url = 'http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=000000%2C00&district=000000&funtype=0000&industrytype=00&issuedate=9&providesalary=99&keyword=%e6%83%85%e6%8a%a5%e5%ad%a6&keywordtype=2&curr_page={}&lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&list_type=0&fromType=14&dibiaoid=0&confirmdate=9'.format(page_num)
    response = requests.get(url)
    if response.status_code==200:
        html = response.text
    else:
        break
    return html

def get(html):
    # (.*?)是取出来, .*?是匹配到但是不取出来
    reg = re.compile(r'class="t1 ">.*?<a target="_blank" title="(.*?)".*?<span class="t2"><a target="_blank" title="(.*?)".*?<span class="t3">(.*?)</span>.*?<span class="t4">(.*?)</span>.*?<span class="t5">(.*?)</span>',re.S)
    items = re.findall(reg, html)
    #print(items)
    return items

for num in range(1, 10):
    content = opener(num)
    for i in get(content):
        print(i[0], i[1], i[2], i[3])
        with open('51job_情报学.txt', 'a') as f:
            f.write(i[0] + '\t' + i[1] + '\t' + i[2] + '\t' + i[3] + '\n\n')


