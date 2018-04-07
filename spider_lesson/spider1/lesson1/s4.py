# -*- coding: utf-8 -*-
# @Author: fxb1rd
# @Date:   2017-10-11 10:24:36
# @Last Modified by:   fxb1rd
# @Last Modified time: 2017-10-14 16:38:54
import urllib.parse#python3
#转码
wd = {"wd":"百度百科"}
m = urllib.parse.urlencode(wd)
print(m)
M = urllib.parse.unquote(m)
print(M)