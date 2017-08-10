#!/usr/bin/env python
# -*- conding:utf-8 -*-
'''
main code program
'''

__author__ = 'Liguanh'


class HtmlOutputer(object):

    datas = []
    def __int__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fileOut = open('out.html', 'w')

        fileOut.write("<html>")
        fileOut.write("<style>td{border:1px #d4d4d4 solid;font-family:YaHei;font-size:11px;}</style>")
        fileOut.write("<body>")
        fileOut.write("<table>")
        fileOut.write("<tr><td>url</td><td>title</td><td>summary</td></tr>")

        #assci
        for data in self.datas:
            fileOut.write("<tr>")
            fileOut.write("<td>%s</td>"%data['url'])
            fileOut.write("<td>%s</td>"%data['title'].encode('utf-8'))
            fileOut.write("<td>%s</td>"%data['summary'].encode('utf-8'))
            fileOut.write("</tr>")

        fileOut.write("</table>")
        fileOut.write("</body>")
        fileOut.write("</html>")

        fileOut.close()