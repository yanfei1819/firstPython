# !/usr/bin/python
# -*- coding: utf-8 -*-
import random


def genPass():
    count = random.randint(1,3)
    return random.choice('ABCD',count)

def __init__():
    print(genPass())
