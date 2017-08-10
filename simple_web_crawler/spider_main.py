#!/usr/bin/env python
# -*- conding:utf-8 -*-
'''
main code program
'''
import url_manager,html_download,html_parser,html_outputer

__author__ = 'Liguanh'

import sys
class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_download.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url, nums):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.had_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw %d: %s' % (count, new_url))
                html_content = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_content)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count == nums:
                    break
                count = count + 1
            except Exception as e:
                print('craw failed reason %s'%(e))
        self.outputer.output_html()

if __name__ == '__main__':
    #检测参数是否为空
    if len(sys.argv[1:]) == 0:
        root_url = "http://baike.baidu.com/view/21087.htm"
        nums = 10
    else:
        root_url = sys.argv[1]
        nums = sys.argv[2]
    objSpider = SpiderMain()
    objSpider.craw(root_url,nums)