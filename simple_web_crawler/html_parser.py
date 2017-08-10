#!/usr/bin/env python
# -*- conding:utf-8 -*-
'''
通过传入的url获取URL的内容以及那个url内容中链接按照正则表达式匹配
'''
import re
from urllib.parse import urlparse,urljoin

__author__ = 'Liguanh'

from bs4 import BeautifulSoup

class HtmlParser(object):

    def parse(self, page_url, html_content):
        if page_url is None or html_content is None:
            return
        soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls,new_data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"/item/\w+"))
        for link in links:
            new_url = link['href']
            new_full_url = urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):

        res_data = {}

        res_data['url'] = page_url
        #<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1')
        res_data['title'] = title_node.get_text()

        #<div class="lemma-summary" label-module="lemmaSummary">
        smmary_node = soup.find('div',class_="lemma-summary")
        res_data['summary'] = smmary_node.get_text()

        return res_data
