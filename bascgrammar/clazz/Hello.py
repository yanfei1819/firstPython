# !/usr/bin/python
# -*- coding: utf-8 -*-

class Hello(object):
    def hello(self , name='hello,world'):
        print('%s' % name)


def test(name):
    if name == '1':
        print(1)
    if name == '2':
        print(2)


if __name__ == '__main__':
    h = Hello()
    h.hello()
    test('2')





