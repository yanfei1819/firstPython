# !/usr/bin/python
# -*- coding: utf-8 -*-

def test():
    try:
        n = 1 / 0
    except ValueError:
        return ''
    finally:
        return ''
