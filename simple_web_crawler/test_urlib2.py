#! /usr/bin/env python3.6
# -*- coding:utf-8 -*-

'''
test urllib get web page content
'''
__author__ = "Lean"

import urllib,cookielib

url = 'http://www.baidu.com'

print('第一种方法')

reponse1 = urllib.urlopen(url)

print(reponse1.getcode())
print(len(reponse1.read()))

print('第二种方法')

request = urllib.Request(url)
request.add_header('user-agent','Mozilla/5.0')
reponse2 = urllib.urlopen(request)
print(reponse2.getcode())
print(len(reponse2.read()))

print('three idea')

cj = cookielib.CookieJar()

opener = urllib.build_opener(urllib.HTTPCookieProcessor(cj))

urllib.install_opener(opener)
reponse3 = urllib.urlopen(url)

print(reponse3.getcode())
print(reponse3.read())

