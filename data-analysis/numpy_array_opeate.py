#!/usr/bin/env python3
# -*- coding;utf-8 -*-

__author__ = "Liguanh"
import numpy

def main():
    # numpy Array Opeates
    print('数组的操作')
    print("\nArray Opeate:")
    lists = numpy.arange(1,11).reshape([2,-1])
    print(lists)
    print('exp')
    print(numpy.exp(lists))
    print('exp2')
    print(numpy.exp2(lists))
    print('sqrt')
    print(numpy.sqrt(lists))
    print('sin')
    print(numpy.sin(lists))
    print('log')
    print(numpy.log(lists))
    print('sum list')
    list = numpy.array([
        [[1,2,3,4],[5,6,7,8]],
        [[9,10,11,12],[13,14,15,16]],
        [[17,18,19,20],[21,22,23,24]]
        ])
    print(list.sum(axis=1))
    # mutil array
    lst1 = numpy.array([1,2,3,4])
    lst2 = numpy.array([5,6,7,8])
    print(lst1+lst2)
    print(lst1-lst2)
    print(lst1.reshape([2,2]))
    print(lst2.reshape([2,2]))
    print(numpy.dot(lst1.reshape([2,2]),lst2.reshape([2,2])))

    print('数组链接与分割操作')
    print(numpy.concatenate((lst1,lst2)))
    print(numpy.vstack((lst1,lst2)))
    print(numpy.hstack((lst1,lst2)))

    print(numpy.split(lst1,2))
    print(numpy.copy(lst2))

if __name__ == '__main__':
    main()
