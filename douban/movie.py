#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2018-04-02 19:55:15
# @Author  : fxb1rd (w1589534127@outlook.com)

from pyquery import PyQuery as pq
import urllib.request
import re
import time
import urllib.parse
import codecs
import ssl

ssl._create_default_https_content = ssl._create_unverified_context#忽略ssl证书验证

headers = {
    "User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
}

def opener(url:str, headers:dict=headers, data:dict = None) -> str:
    time.sleep(0.2)
    request = urllib.request.Request(url = url,headers = headers,data = data)
    response = urllib.request.urlopen(request)
    html = response.read().decode('utf-8').encode('gbk','replace').decode('gbk')#转码，具体情况具体对待
    return html

def get_id(name:str) -> str:
    name = urllib.parse.quote(name)
    ID = re.findall('movie.douban.com%2Fsubject%2F(.*?)%2F&amp;query',opener("https://www.douban.com/search?q={}".format(name)))
    return ID[0]

def get_content(ID:str) -> str:
    html = opener('https://movie.douban.com/subject/{}'.format(ID))
    p = pq(html)
    content = p('div').filter('#info').text()

    content2 = p('span').filter('.·all.hidden').text()
    content3 = p('div').filter('#link-report').text()
    if content2:
        return content + '\n简介:' + content2
    else:
        return content + '\n简介:' + content3

def main():
    Content = {}
    print('多个名称用‘ ’(空格)隔开,输入‘quit’输出并退出')
    while True:
        print('输入电影名称')
        names = input()
        names = names.split(' ')
        for name in names:
            if name=='quit':
                with codecs.open('test.txt','w','utf-8') as f:
                    for k,v in Content.items():
                        f.write(k + '\n')
                        f.write(v + '\n')
                        f.write('-'*50 + '\n\n')
                return print('输出完成!')
            else:
                Content[name] = get_content(get_id(name))
                print(name + '信息的已提取。')

if __name__ == '__main__':
    main()




