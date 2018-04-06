#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2018-01-07 15:57:39
# @Author  : fxb1rd (w1589534127@outlook.com)
# @Link    : http://
# @Version : $Id$

import urllib.request
import urllib.parse
from lxml import etree

headers = {
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language":"zh-CN,zh;q=0.9",
            "Cache-Control":"max-age=0",
            "Connection":"keep-alive",
            #"Content-Length":"326",
            "Content-Type":"application/x-www-form-urlencoded",
            "Cookie":"JSESSIONID=1975ADDD87A9D7212775542E4B004C18",
            "Host":"npd.nsfc.gov.cn",
            "Origin":"http://npd.nsfc.gov.cn",
            "Referer":"http://npd.nsfc.gov.cn/fundingProjectSearchAction.action",
            "Upgrade-Insecure-Requests":"1",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"
            }
url = "http://npd.nsfc.gov.cn/fundingProjectSearchAction!search.action"

def req():
    ##请求
    data = urllib.parse.urlencode(values).encode(encoding='utf-8')
    requests=urllib.request.Request(url, data = data, headers = headers)
    response=urllib.request.urlopen(requests)
    html=response.read().decode('utf-8')
    #print(html)
    ##xpath处理
    selector = etree.HTML(html)
    title = selector.xpath("//ul[@id='project_result']/li/dl/dt")
    #print(title)
    number = selector.xpath("//ul[@id='project_result']/li/dl/dd[1]")
    sort = selector.xpath("//ul[@id='project_result']/li/dl/dd[2]")
    unit = selector.xpath("//ul[@id='project_result']/li/dl/dd[3]")
    leader = selector.xpath("//ul[@id='project_result']/li/dl/dd[4]")
    fund = selector.xpath("//ul[@id='project_result']/li/dl/dd[5]")
    year = selector.xpath("//ul[@id='project_result']/li/dl/dd[6]")
    key = selector.xpath("//ul[@id='project_result']/li/dl/dd[7]")
    ##构建二维数组循环输出数据
    content = [title,number,sort,unit,leader,fund,year,key]
    length = len(title)
    with open("data.txt","a") as f:
        for i in range(0,length):
            for x in content:
                info = x[i].xpath('string(.)')
                #info = info.strip().replace('\n','')
                info = "".join(info.split())
                #print(info)
                f.write(info + '\n')
        f.write('\n')
        # f.write('第%d页写入成功！'%page)
        # f.write('\n')
    #print('第%d页写入成功！'%page)


for page in range(1,26):
    values = {
        "pageSize":"10",
        "currentPage":page,
        # "fundingProject.projectNo":"",
        # "fundingProject.name":"",
        # "fundingProject.person":"",
        # "fundingProject.org":"",
        # "fundingProject.applyCode":"",
        # "fundingProject.grantCode":"",
        # "fundingProject.subGrantCode":"",
        # "fundingProject.helpGrantCode":"",
        "fundingProject.keyword":"人工智能",
        # "fundingProject.statYear":"",
        "checkCode":"u2t9"
        }
    req()






