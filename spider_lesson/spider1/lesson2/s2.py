# -*- coding: utf-8 -*-
# @Author: fxb1rd
# @Date:   2017-10-12 10:23:31
# @Last Modified by:   fxb1rd
# @Last Modified time: 2017-10-12 11:28:39

import urllib.request

# 代理开关，表示是否启用代理
proxyswitch = True

# 构建一个Handler处理器对象，参数是一个字典类型，包括代理类型和代理服务器IP+PROT
httpproxy_handler = urllib.request.ProxyHandler({"http":"59.40.68.136:8010"})

# 构建了一个没有代理的处理器对象
nullproxy_handler = urllib.request.ProxyHandler({})

if proxyswitch:
    opener = urllib.request.build_opener(httpproxy_handler)
else:
    opener = urllib.request.build_opener(nullproxy_handler)

# 构建了一个全局的opener，之后所有的请求都可以用urlopen()方式去发送，也附带Handler的功能
urllib.request.install_opener(opener)

request = urllib.request.Request("http://www.baidu.com/")
response = urllib.request.urlopen(request)

#print response.read().decode("gbk")
print(response.read())
