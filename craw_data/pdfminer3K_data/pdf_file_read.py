#! /usr/bin/env python3
# -*- coding:utf-8 -*-
from urllib.request import urlopen

from pdfminer.converter import PDFPageAggregator

from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams

__author__='Liguanh'

'''
test python pdfminer3k read pdf files
'''

# 获取文档的对象(object)
fp = open("test1.pdf", "rb")

#fp = urlopen('')

# 创建一个与文档关联的分析器
parser = PDFParser(fp)

# 创建一个PDF的文档对象
doc = PDFDocument()

#链接解释器and文档对象
parser.set_document(doc)
doc.set_parser(parser)

#初始化文，没有密码设置为空
doc.initialize("")

#创建PDF资源管理器
resouce = PDFResourceManager()

#参数分析器
laparam = LAParams()

#PDF聚合器
device = PDFPageAggregator(resouce, laparams=laparam)

#创建pdf页面解释器
interpreter = PDFPageInterpreter(resouce, device)

#使用文档对象得到页面的集合
for page in doc.get_pages():

    # 使用页面解释器来读取
    interpreter.process_page(page)

    # 使用聚合器来获取内容
    layout = device.get_result()

    for outPut in layout:
        if  hasattr(outPut, 'get_text'):
            print(outPut.get_text())
