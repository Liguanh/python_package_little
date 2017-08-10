# ! /usr/bin/env python3.6
# -*- coding:utf-8 -*-

'''
define log level handler
'''
__author__='Lean'

import logging
import time

#用字典保存日志级别
format_dict = {
        1 : logging.Formatter('[%(asctime)s]  %(name)s.%(levelname)s:line_%(lineno)d  %(message)s'),
        2 : logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
        3 : logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
        4 : logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
        5 : logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        }

timeStr = time.strftime('%Y%m%d', time.localtime())
logDirFile = 'log/bank-transfer-%s.log'%timeStr

class Logger(object):
    def __init__(self, logFile=logDirFile, loglevel=1, logger='testing'):

        #创建一个logger
        self.logger  =  logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        self.logFile = logFile
        self.loglevel = loglevel

#文件日志纪录
    def getLog(self):
        #判断是否含有handlers
        if not self.logger.handlers:
            #创建一个操作句柄，写入日志文件
            fh = logging.FileHandler(self.logFile)
            fh.setLevel(logging.DEBUG)

            formater = format_dict[int(self.loglevel)]
            fh.setFormatter(formater)

            self.logger.addHandler(fh)
        return self.logger

#终端日志打印信息
    def commandLog(self):
        if not self.logger.handlers:
            #创建一个handler输出到控制台
            ch = logging.StreamHandler()
            ch.setLevel(logging.DEBUG)

            formater = format_dict[int(self.loglevel)]
            ch.setFormatter(formater)
            self.logger.addHandler(ch)
        return self.logger


