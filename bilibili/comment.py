#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2017-12-26 16:37:15
# bilibili评论及回复获取
import requests
import json

def getHTML(av,page):
    ############评论抓取#################
    html = url + av + '&pn='
    count = 1
    f=open('bilibili.txt','w',encoding='utf-8')
    while count<page+1:
        #拼接评论地址
        main_url = html + str(count)
        #print(main_url)
        Request = requests.get(main_url)
        if Request.status_code==200:
            content = json.loads(Request.text)
        else:
            break
        #获取每页回复数
        length = len(content['data']['replies'])#每页回复数
        print(length)
        if length!=0:
            #打印评论
            for i in range(length):
                #取得评论内容
                Message = content['data']['replies'][i]['content']['message']
                #去除换行符
                Message = Message.replace('\n', '')
                f.write('▽▽' + Message + '\n')

    #############评论的回复抓取##########

                #获取回复数并生成页数
                leng = content['data']['replies'][i]['count']
                #print(leng)
                page_num = int(leng/10 + 1)
                #print(page_num)
                if leng!=0:
                    #获取有回复楼层的root_id(楼主)
                    poster_id = content['data']['replies'][i]['rpid']
                    print(poster_id)
                    reply = "https://api.bilibili.com/x/v2/reply/reply?type=1&oid={}&ps=10&root={}&pn=".format(av,poster_id)
                    for j in range(page_num):
                        #拼接回复地址
                        Rp_url = reply + str(j)
                        #print(Rp_url)
                        request = requests.get(Rp_url)
                        if request.status_code==200:
                            cont = json.loads(request.text)
                        else:
                            break
                        Length = len(cont['data']['replies'])#每页回复数
                        for k in range(Length):
                            message = cont['data']['replies'][k]['content']['message']
                            message = message.replace('\n', '')
                            f.write('    →→' + message + '\n')
                else:
                    continue#使用continue保证循环不中断
        else:
            break
        f.write('*'*40 + '第%d页'%count + '*'*40 + '\n')
        print("第%d页写入成功！"%count)
        count += 1
    f.close()
    print(count-1,'页评论写入成功！')

url = "https://api.bilibili.com/x/v2/reply?type=1&oid="
av = input("输入av号:")
page = int(input("输入爬取的总页数:"))
getHTML(av,page)