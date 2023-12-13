# !/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime


def getNowTime():
    now = datetime.now()
    print(now)
    print(type(now))


def spec():
    time = datetime(2015, 2, 12, 12, 1)
    print(time)
    timestamp = time.fromtimestamp()
    print(timestamp)

if __name__ == '__main__':
    getNowTime()
    spec()
