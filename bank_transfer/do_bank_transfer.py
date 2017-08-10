#! /usr/bin/env python3
# -*- coding:utf-8 -*-

__author__='Liguanh'

'''
执行模拟银行转账的操作
'''

import pymysql
from log import Logger
from bank_transfer import BankTransfer
import sys

#获取配置信息
sys.path.append('./config')
from config import db_config

logger  = Logger().getLog()

try:
    conn = pymysql.connect(**db_config)
except Except as e:
    logger.error('数据库连接失败,%s'%format(e))
    print('mysql connect faild ! {}'.format(e))


#定义终端的执行结果
if __name__ == '__main__':
    fromUser = sys.argv[1]
    targetUser = sys.argv[2]
    money = sys.argv[3]

transfer = BankTransfer(conn)

try:
    transfer.doTransfer(fromUser, targetUser, money)
    logger.info( '帐户%s转账%s元钱至帐户%s成功'%(transfer.getUserById(fromUser)['name'], money, transfer.getUserById(targetUser)['name']))
except Exception as e:
    logger.error('帐户转账失败%s'%e)
    print('transfer money failed %s'%format(e))
finally:
    conn.close()
