# -*- coding: utf-8 -*-
# @Author: fxb1rd
# @Date:   2017-10-11 10:50:57
# @Last Modified by:   fxb1rd
# @Last Modified time: 2017-10-14 17:45:49
import urllib.request
import urllib.parse

ua_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
}

def load(url,filename):
    """
       根据url发送请求，获取服务器响应文件
       url：待爬取地址
    """
    print("正在下载"+filename)

    # 构造一个请求
    request = urllib.request.Request(url,headers = ua_headers)
    response =  urllib.request.urlopen(request)
    return response.read()

def output(html,filename):
    """
       输出到本地
       html：响应的文件
    """
    print("正在保存"+filename)

    with open(filename,"wb+") as f:# wb+,使用w 会出现中文乱码
        f.write(html)

    print("-"*50)

def Spider(url,beginPage,endPage):
    """
       爬虫调度器
    """
    for page in range(beginPage,endPage+1):
        pn = (page-1)*50
        filename = "第" + str(page) + "页.html"
        fulurl = url + "&pn=" + str(pn)
        print(fulurl)

        html = load(fulurl,filename)

        output(html,filename)


def main():
    url = "http://tieba.baidu.com/f?"

    kw = input("请输入贴吧名:")
    begin = int(input("请输入起始页:"))
    end = int(input("请输入结束页:"))

    keyword = urllib.parse.urlencode({"ky":kw})
    fulurl = url + keyword

    Spider(fulurl,begin,end)


if __name__ == '__main__':
    main()