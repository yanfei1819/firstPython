# !/usr/bin/python
# -*- coding: utf-8 -*-


# object 表示继承类
class User(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print("hello,world!")


if __name__ == '__main__':
    u = User('syf', 30)
    u.name = 'lyf'
    print(u.name)
    u.say()
