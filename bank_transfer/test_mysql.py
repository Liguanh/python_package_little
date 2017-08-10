#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
test pymysql
'''

import pymysql
import mysql.connector
import sys

sys.path.append('./config')
from config import db_config

try:
    #conn = mysql.connector.connect( **db_config )
    conn = pymysql.connect(**db_config)
    print(conn)
except Exception as e:
    print('connect mysql failed, reason:%s'%format(e))



