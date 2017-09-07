#! /usr/bin/env python3
# -*- coding:utf-8 -*-

__author__= "Liguanh"

import numpy
from numpy.linalg import *

def main():
    lst = numpy.array(numpy.arange(1,5).reshape([2, -1]))
#    lst = numpy.array([[1,2,3],[5,6,7]])


    print('Inv:')
    print(inv(lst))

    print('T:')
    print(lst.transpose())

    print('Det:')
    print(det(lst))

    print('deg:')
    print(eig(lst))

    lst = numpy.array(numpy.arange(1,5).reshape([2, -1]))
    result = numpy.array([[9],[11]])
    print('Solve')
    solves = solve(lst,result)
    print('二元一次方程的解:x=%s, y=%s'%(solves[0][0], solves[1][0]))


    x1 = numpy.poly1d([2,1,3])
    print(x1.r)
if __name__ == "__main__":
    main()
