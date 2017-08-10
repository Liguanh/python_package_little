#!/usr/bin/env python
# -*- conding:utf-8 -*-
'''
main code program
'''

__author__ = 'Liguanh'

from urllib import request

class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None;

        reponse = request.urlopen(url)

        if reponse.getcode() != 200:
            return None;

        return reponse.read()
