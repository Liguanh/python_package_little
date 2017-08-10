#! /usr/bin/env python3
# -*- coding:utf-8 -*-

__author__='Liguanh'

'''
银行转账的类操作
'''

from log import Logger

logger = Logger().getLog()

class BankTransfer(object):
    def __init__(self, conn):
        self.conn = conn

    #执行转账的操作
    def doTransfer(self, fromUser, targetUser, money):

        try:
            #检测转账用户是否存在
            self.checkUseIsExists(fromUser)
            #检测接收帐户是否存在
            self.checkUseIsExists(targetUser)
            #检测转账金额是否足够
            self.checkEnoughMoney(fromUser, money)
            #执行转账用户金额减少
            self.reduceMoney(fromUser, money)
            #执行接收帐户金额增加
            self.addMoney(targetUser, money)
            #添加转账历史纪录
            self.addFundhistory(fromUser, targetUser, money)
            self.conn.commit()
        except Exception as e:
            logger.error('转账失败%s'%format(e))
            self.conn.rollback()
            raise e


    #检测转账的帐户是否存在
    def checkUseIsExists(self, userId):
        cursor = self.conn.cursor()

        try:
            sql = 'select id from users where id = %s'%userId
            cursor.execute(sql)
            logger.info(sql)
            res = cursor.fetchall()
            if len(res) == 0:
                raise Exception('帐户%s不存在'%userId)
        finally:
            cursor.close()

    #检测转账的帐户是否有足够的余额
    def checkEnoughMoney(self, userId, money):
        cursor = self.conn.cursor()

        try:
            sql = 'select id from users where id = %s and balance >= %s'%(userId, money)

            cursor.execute(sql)
            logger.info(sql)
            res = cursor.fetchall()

            if len(res)==0:
                raise Exception('转账帐户%s余额不足'%userId)
        finally:
            cursor.close()
    #帐户扣款转账
    def reduceMoney(self, userId, money):
        cursor = self.conn.cursor()

        try:
            sql = 'update users set balance = balance - %s where id = %s'%(money, userId)
            cursor.execute(sql)
            logger.info(sql)

            if cursor.rowcount == 0:
                raise Exception('帐户%s扣款失败'%userId)
        finally:
            cursor.close()

    #帐户收款
    def addMoney(self, userId, money):
        cursor = self.conn.cursor()

        try:
            sql  = 'update users set balance = balance + %s where id = %s'%(money, userId)

            cursor.execute(sql)
            logger.info(sql)

            if cursor.rowcount == 0:
                raise Exception('帐户%s收款失败'%userId)

        finally:
            cursor.close()

    #添加转账历史纪录
    def addFundhistory(self, fromUser, targetUser, money):
        cursor = self.conn.cursor()

        try:
            sql = 'insert into fund_history (`from_user_id`, `target_user_id`, `transfer_money`) values( %s, %s, %s )'%(fromUser, targetUser, money)

            cursor.execute(sql)
            logger.info(sql)

            if cursor.rowcount == 0:
                raise Exception('转账纪录更新失败')
        finally:
            cursor.close()


    #获取帐户信息
    def getUserById(self, userId):
        cursor = self.conn.cursor()

        try:
            sql = 'select email, name from users where id = %s'%userId

            cursor.execute(sql)
            logger.info(sql)
            result = cursor.fetchone()

        except Exception as e:
            raise e

        finally:
            cursor.close()

        return result
