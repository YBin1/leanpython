#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Michael Liao'

import sys
import os

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

def recur_fibo(n):
    """递归函数
    输出斐波那契数列"""
    if n <= 1:
        return n
    else:
        return (recur_fibo(n-1)+recur_fibo(n-2))
if __name__=='__main__':
    nterms = int(input("您要输出几项?"))

    # 检查输入的数字是否正确
    if nterms <= 0:
        print("请输入正数")
    else:
        print("斐波那契数列：")
        for i in range(nterms):
            print(recur_fibo(i))

    os.system("pause")
