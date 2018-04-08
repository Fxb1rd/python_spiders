#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2018-01-21 20:36:13
# @Author  : fxb1rd (w1589534127@outlook.com)
# @Link    : http://
# 51job爬虫

import requests
import re
import time
from pyquery import PyQuery as pq

###爬虫，requests
def opener(url):
	time.sleep(5)
	response = requests.get(url)
	if response.status_code==200:
		response.encoding = 'gbk'
		html = response.text
	return html

###筛选链接，正则匹配
def get_links(html):
	reg = re.compile(r'<p class="t1 ">.*?href="(.*?)"',re.S)
	link = re.findall(reg, html)
	return link

###筛选信息，pyquery
def get_infos(html):
	p = pq(html)
	info1 = p('div').filter('.cn').text()
	info2 = p('div').filter('.t1').text()
	info3 = p('div').filter('.job_msg').text()
	infos = [info1,info2,info3]
    # .items()获取多个节点
	return infos

for num in range(1,4):
	##主链接
	url = 'http://search.51job.com/jobsearch/search_result.php?fromJs=1&jobarea=010000%2C020000%2C030200%2C040000%2C070200&district=000000&funtype=0000&industrytype=00&issuedate=9&providesalary=99&keyword=%e6%83%85%e6%8a%a5%e5%ad%a6&keywordtype=2&curr_page={}&lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&list_type=0&fromType=14&dibiaoid=0&confirmdate=9'.format(num)
	print(url)
	content = opener(url)
	links = get_links(content)
	print(len(links))
	for item in links:
		##二级链接
		print(item)
		Url = item
		cont = opener(Url)
		infos = get_infos(cont)
		##输出到文件
		with open('test.txt','a') as f:
			for info in infos:
				f.write(info + '\n')
			f.write('\n\n')






