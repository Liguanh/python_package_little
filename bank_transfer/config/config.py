#! /usr/bin/env python3
# -*- coding:utf-8 -*-

'''
config python files
'''
import pymysql

#数据库的基本配置
db_config = {
    'host': '127.0.0.1',
    'user': 'test_python',
    'password': '123qwe',
    'port': 3306,
    'db': 'python_test',
    'charset': 'utf8',
    'cursorclass': pymysql.cursors.DictCursor,
}

#other configs
