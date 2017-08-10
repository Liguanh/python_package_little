#!/usr/bin/env python3
#! -*- coding:utf-8 -*-
__author__ = 'Liguanh'

# import program package
from bs4 import BeautifulSoup
from urllib import parse
from urllib.request import Request,urlopen
import pymysql
import re

#引入配置文件
import sys
sys.path.append('./config')
from config import db_config


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
        # 链接数据库mysql
        try:
            conn = pymysql.connect(**db_config)
            with conn.cursor() as cursor:
                # create a mysql sql
                insert_sql = "insert into `wiki_urls` (`url_name`,`url_href`) values (%s,%s)"
                # 执行excute sql
                cursor.execute(insert_sql, (url.get_text(), 'https://en.wikipedia.org' + url['href']))

                # submit cursor
                conn.commit()

        except Exception as e:
            print('connect mysql error %s' % e)
        finally:
            conn.close()
