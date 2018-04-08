#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 智联招聘爬虫 数据科学
# http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%e5%8c%97%e4%ba%ac%2b%e6%b7%b1%e5%9c%b3%2b%e5%b9%bf%e5%b7%9e%2b%e4%b8%8a%e6%b5%b7%2b%e5%8d%97%e4%ba%ac&kw=%e6%95%b0%e6%8d%ae%e7%a7%91%e5%ad%a6&p={}.format(num)
import requests
import re
import time
from pyquery import PyQuery as pq

###爬虫，requests模块
def opener(url):
	#设置爬虫时间间隔
	time.sleep(5)
	#user-agent模拟浏览器
	headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"}
	#发送请求
	response = requests.get(url,headers=headers)
	if response.status_code==200:
		response.encoding = 'utf-8'
		html = response.text
	return html#返回网页数据

###筛选链接，正则匹配
def get_links(html):
	#匹配链接
	reg = re.compile(r'<td class="zwmc".*?href="(.*?)"',re.S)
	link = re.findall(reg, html)
	return link#返回链接数据

###筛选信息，pyquery
def get_infos(html):
	p = pq(html)#创建pyquery对象
	info1 = p('div').filter('.top-fixed-box').text()
	info2 = p('ul').filter('.terminal-ul').text()
	info3 = p('div').filter('.tab-inner-cont').eq(0).text()
	infos = [info1,info2,info3]
	return infos#返回信息数据

for num in range(1,11):
	##主页面链接
	url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%e5%8c%97%e4%ba%ac%2b%e6%b7%b1%e5%9c%b3%2b%e5%b9%bf%e5%b7%9e%2b%e4%b8%8a%e6%b5%b7%2b%e5%8d%97%e4%ba%ac&kw=%e6%95%b0%e6%8d%ae%e7%a7%91%e5%ad%a6&p={}'.format(num)
	print(url)
	content = opener(url)
	links = get_links(content)
	print(len(links))
	for item in links:
		##二级页面链接
		print(item)
		Url = item
		cont = opener(Url)
		infos = get_infos(cont)
		##输出到文件
		with open('test.txt','a',encoding='utf-8') as f:
			for info in infos:
				f.write(info + '\n')
			f.write('\n\n')






