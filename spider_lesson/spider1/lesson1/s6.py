# -*- coding: utf-8 -*-
# @Author: fxb1rd
# @Date:   2017-10-11 15:30:11
# @Last Modified by:   fxb1rd
# @Last Modified time: 2017-10-11 18:14:15

#get和post请求的区别
#get请求附带查询参数
#post请求不附带参数
#
#get请求，查询参数在QueryString里保存
#post请求，查询参数在Form表单里保存
import urllib.request
import urllib.parse


# ##########POST###########################
# #通过抓包的方式获得url，而不是浏览器
# url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"

# headers = {
#         "Accept" : "application/json, text/javascript, */*; q=0.01",
#         "X-Requested-With" : "XMLHttpRequest",
#         "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
#         "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
#     }


# key = input("请输入需要翻译的文字:")

# # 发送到web服务器的表单数据
# formdata = {
# "type" : "AUTO",
# "i" : key,
# "doctype" : "json",
# "xmlVersion" : "1.8",
# "keyfrom" : "fanyi.web",
# "ue" : "UTF-8",
# "action" : "FY_BY_CLICKBUTTON",
# "typoResult" : "true"
# }

# # 经过urlencode转码##encode转码
# data = urllib.parse.urlencode(formdata).encode(encoding='utf-8')

# # 如果Request()方法里的data参数有值，那么这个请求就是POST
# # 如果没有，就是Get
# request = urllib.request.Request(url, data = data, headers = headers)
# response = urllib.request.urlopen(request)
# print(response.read().decode('UTF-8'))#decode解码


###########################AJAX#########################
url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action"

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

formdata = {
        "start":"0",
        "limit":"2"
    }

data = urllib.parse.urlencode(formdata).encode(encoding='utf-8')

request = urllib.request.Request(url, data = data, headers = headers)

print(urllib.request.urlopen(request).read().decode('utf-8'))


