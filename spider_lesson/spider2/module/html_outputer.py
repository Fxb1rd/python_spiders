# -*- coding: utf-8 -*-
# @Author: fxb1rd
# @Date:   2017-08-24 18:35:25
# @Last Modified by:   fxb1rd
# @Last Modified time: 2017-08-24 23:54:50

class HtmlOutputer(object):
    """docstring for HtmlOutputer"""
    def __init__(self):
        self.datas = []

    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html','w',encoding='utf-8')

        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')

        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td><a href="%s">%s</a></td>'%(data['url'],data['title']))
            #fout.write('<td>%s</td>'%data['title'])
            fout.write('<td>%s</td>'%data['summary'])
            fout.write('</tr>')

        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')