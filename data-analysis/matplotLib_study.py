#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
matplotLib introduction 图标库
'''
__author__ = 'Liguanh'

import numpy
import matplotlib.pyplot as plt


def main():
    x = numpy.linspace(-numpy.pi, numpy.pi, 256, endpoint = True)
    sin, cos = numpy.sin(x), numpy.cos(x)
    print('基本画法第一个图')
    plt.figure(1)
    plt.plot(x, cos,  color= 'blue',  label="sin")
    plt.plot(x, sin, color='green', linewidth=1.5, linestyle="-", label='sin',alpha=0.5)
    plt.title('Sin and Cos line')
    plt.show()

if __name__ == '__main__':
    main()
