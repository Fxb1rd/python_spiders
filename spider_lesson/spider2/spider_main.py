# -*- coding: utf-8 -*-
# @Author: fxb1rd
# @Date:   2017-08-24 14:14:00
# @Last Modified by:   fxb1rd
# @Last Modified time: 2017-08-25 00:09:26

from module import html_downloader, html_parser, html_outputer, url_manager

class SpiderMain(object):
    """docstring for SpiderMain"""
    def __init__(self):
        self.urls = url_manager.UrlManeger()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self,root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw %d:%s'%(count,new_url))
                html_cont = self.downloader.download(new_url)
                new_urls,new_data = self.parser.parse(new_url,html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == 1000:
                    break
                count += 1
            except:
                print("craw failed")


        self.outputer.output_html()

if __name__ == '__main__':
    root_url = "http://baike.baidu.com/item/Python"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)