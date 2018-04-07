# -*- coding: utf-8 -*-
# @Author: fxb1rd
# @Date:   2017-10-11 10:07:10
# @Last Modified by:   fxb1rd
# @Last Modified time: 2018-01-06 17:40:15

import urllib.request#python2 urllib2

#User-Agent
ua_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
}

#通过request方法构造一个请求对象
request = urllib.request.Request("http://lol.qq.com/web201310/info-heros.shtml", headers = ua_headers)
#向url地址发送请求，并返回服务器类文件
response = urllib.request.urlopen(request)
print(response)
#用python的方法操作文件
html = response.read()
print(html)

#返回响应码 200表示成功
print(response.getcode())
#返回实际url，防止重定向
print(response.geturl())
#返回http的请求报头
#print(response.info())