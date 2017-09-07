#!/usr/bin/env python3
#! -*- coding:utf-8 -*-
import numpy

__author__ = 'Liguanh'


def main():
    list = [[1,3,5],[2,4,6]]
    print(type(list))

    num_list = numpy.array(list, dtype=numpy.float)
    #bool，int,int8,int16,int32,int64,int128,uint8,.......
    print(type(num_list))
    print(num_list.shape)
    print(num_list.ndim)
    print(num_list.dtype)
    print(num_list.itemsize)
    print(num_list.size)

    # @some arrays
    print(numpy.zeros([2,4]))
    print(numpy.ones([1,4]))

    print("Rand:")
    print(numpy.random.rand(2,4))

    print("RandInt:")
    print(numpy.random.randint(1,100))

    print("Choice:")
    print(numpy.random.choice([10,20,30]))

    print("Distrbute:")
    print(numpy.random.beta(1,10,10))

if __name__ == '__main__':
    main()
