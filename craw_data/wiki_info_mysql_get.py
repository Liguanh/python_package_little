#!/usr/bin/env python3
#! -*- coding:utf-8 -*-
__author__ = 'Liguanh'

import pymysql

import sys
sys.path.append('./config')

from config import db_config

#python链接数据库mysql
conn = pymysql.connect(**db_config)

try:
    with conn.cursor() as cursor:
        sql = "select url_name,url_href from wiki_urls "
        count = cursor.execute(sql)

        result = cursor.fetchall()

        print(count)
        print(result)
except Exception as e:
    pass
finally:
    conn.close()