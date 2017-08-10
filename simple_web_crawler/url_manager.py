#!/usr/bin/env python
# -*- conding:utf-8 -*-
'''
main code program
'''

__author__ = 'Liguanh'

class UrlManager(object):
    new_urls, old_urls = set(),set()
    def __int__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self,urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def had_new_url(self):
        return len(self.new_urls) != 0
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url


