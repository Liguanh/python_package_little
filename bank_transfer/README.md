1、python 日志类封装，解决了重复写日志的问题
use: from log import Logger
logger = Logger.getLog()

2、引入pymysql的链接mysql数据库
import pymysql  pymysql.connect(**db_config)

3、模拟银行转账，并调用数据库的事务处理,以及一些相关数据的验证

4、sql数据初始化 init.sql 引入sql 初始化数据表，导入到自己的数据库
