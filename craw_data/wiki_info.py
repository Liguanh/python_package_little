#!/usr/bin/env python3
#! -*- coding:utf-8 -*-
__author__ = 'Liguanh'

# import program package
from bs4 import BeautifulSoup
from urllib import parse
from urllib.request import Request,urlopen

import re

# get the wiki main page
url = 'https://en.wikipedia.org/wiki/Main_Page'
resp = urlopen(url)
html_content = resp.read().decode('utf-8')

# beautifulSoup useful
soup = BeautifulSoup(html_content, 'html.parser')

urlLists = soup('a', href=re.compile(r"^/wiki/"))

#output all name and url info
for url in urlLists:
    if not re.search(r"\.jpg|JPG|gif|png", url['href']):
        #string 只能获取一个，get_text() 获取标签下所有的文字
         print(url.text, '<--->', url['href'])



