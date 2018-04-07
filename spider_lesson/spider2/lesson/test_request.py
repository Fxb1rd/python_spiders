# -*- coding: utf-8 -*-
# @Author: fxb1rd
# @Date:   2017-08-23 23:54:31
# @Last Modified by:   fxb1rd
# @Last Modified time: 2017-08-24 00:15:57

#import urllib2,cookielib#######python2

#python3
from urllib import request
import http.cookiejar

url = "http://www.baidu.com"

print('方法1')

 #直接请求
response1 = request.urlopen(url)

#获取状态码，200表示获取成功
print(response1.getcode())

#读取内容
print(len(response1.read()))

print('方法2')

 #创建Request对象
req = request.Request(url)

#添加http的header
req.add_header('user-Agent','Mozilla/5.0')#伪装

#发送请求获取结果
response2 = request.urlopen(req)
print(response2.getcode())
print(len(response2.read()))

print('方法3')

#创建cookie容器
cj = http.cookiejar.CookieJar()

#创建一个opener
opener = request.build_opener(request.HTTPCookieProcessor(cj))

#给request/urllib2安装opener
request.install_opener(opener)

#使用带有cookie的request/urllib2访问网页
response3 = request.urlopen(url)
print(response3.getcode())
print(cj)
print(response3.read())#打印网页内容