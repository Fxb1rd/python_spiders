# -*- coding: utf-8 -*-
# @Author: fxb1rd
# @Date:   2017-08-24 18:34:40
# @Last Modified by:   fxb1rd
# @Last Modified time: 2017-08-24 23:24:32

from urllib import request

class HtmlDownloader(object):
    """docstring for HtmlDownloader"""
    def download(self,url):
        if url is None:
            return None

        response = request.urlopen(url)

        if response.getcode() != 200:
            return None

        return response.read()