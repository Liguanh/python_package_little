#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = "Lean"
'''
test urlib model
'''

from urllib import request

url = 'http://en.wikipedia.org/robots.txt'

req= request.Request(url)

req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')

response = request.urlopen(req)

print (response.read().decode('utf-8'))
