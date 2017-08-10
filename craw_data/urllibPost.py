#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__="Lean"
'''
test urllib post 
'''

from urllib import parse
from urllib.request import urlopen
from urllib.request import Request

from bs4 import BeautifulSoup

url = 'http://www.thsrc.com.tw/tw/TimeTable/SearchResult'

req = Request(url)

postData = parse.urlencode(
    [
        ('StartStation','977abb69-413a-4ccf-a109-0272c24fd490'),
        ('EndStation','9c5ac6ca-ec89-48f8-aab0-41b738cb1814'),
        ('SearchDate','2017/08/02'),
        ('SearchTime','14:00'),
        ('SearchWay','DepartureInMandarin')
    ]
)

req.add_header('Origin', 'http://www.thsrc.com.tw')
req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')

response = urlopen(req, data=postData.encode("utf-8"))

html_content = response.read()


#html的解析获取开始和结束时间
def parse_html(html_content):
    s_time,e_time = set(),set()
    if html_content is None:
        return
    soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
    data1 = soup.find_all('td', class_='column3')
    for s in data1:
        s_time.add(s)

    data2 = soup.find_all('td', class_='column4')

    for e in data2:
        e_time.add(e)

    return s_time,e_time

sTime,eTime = parse_html(html_content)

print(sTime,eTime)



