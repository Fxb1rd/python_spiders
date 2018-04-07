# -*- coding: utf-8 -*-
# @Author: fxb1rd
# @Date:   2017-08-24 18:32:59
# @Last Modified by:   fxb1rd
# @Last Modified time: 2017-08-24 23:24:40

class UrlManeger(object):
    """docstring for UrlManeger"""
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self,url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self,urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
