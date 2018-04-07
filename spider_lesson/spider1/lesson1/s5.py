# -*- coding: utf-8 -*-
# @Author: fxb1rd
# @Date:   2017-10-11 10:37:50
# @Last Modified by:   fxb1rd
# @Last Modified time: 2017-10-11 10:49:57
import urllib.request
import urllib.parse

ua_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
}

url = "http://www.baidu.com/s"

keyword = input("请输入要查询的词条:")
wd = {"wd":keyword}#字典类型
wd = urllib.parse.urlencode(wd)

#拼接完整url
fulurl = url + "?" + wd

request = urllib.request.Request(fulurl,headers = ua_headers)

response = urllib.request.urlopen(request)

print(response.read())