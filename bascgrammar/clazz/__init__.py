# !/usr/bin/python
# -*- coding: utf-8 -*-

import sys

def test001():
    args = sys.argv
    if len(args)==1:
        print("hello")
    else:
        print('Too many arguments!')

if __name__ == '__main__':
    test001()