
# @Author: fxb1rd
# @Date:   2017-10-11 09:46:53
# @Last Modified by:   fxb1rd
# @Last Modified time: 2017-10-17 13:24:26
######################################################
import urllib.request#python2 urllib2

#向url地址发送请求，并返回服务器类文件
response = urllib.request.urlopen("http://www.baidu.com/")
#用python的方法操作文件
html = response.read()
#print(html)
#转码
print(html.decode('utf-8').encode('gbk','replace').decode('gbk'))
#print(html.decode())

######################################################
# import urllib.request#python2 urllib2



# #User-Agent
# ua_headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
# }

# #通过request方法构造一个请求对象
# request = urllib.request.Request("http://www.baidu.com/", headers = ua_headers)
# #向url地址发送请求，并返回服务器类文件
# response = urllib.request.urlopen(request)

# #用python的方法操作文件
# html = response.read()

# print(str(html),'utf-8')



