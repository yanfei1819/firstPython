# !/usr/bin/python
# -*- coding: utf-8 -*-

class Student:

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def hello(self):
        pass


if __name__ == '__main__':
    s = Student('222', 3)
    print(s.get_name())
    s.hello()
