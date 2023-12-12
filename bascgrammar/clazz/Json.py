# !/usr/bin/python
# -*- coding: utf-8 -*-


import json

if __name__ == '__main__':
    file_pth = 'json.txt'
    file_obj = open(file_pth, 'r', )
    lines = file_obj.readline
    data = {}
    value = 0
    for line in lines:
        line_info = line.split(',')
        if line_info:
            info = {'name': line_info[0], 'url': line_info[1].replace('\n', "")}
            data[value] = info
            value += 1
    file_obj.close()
    s = open('json.json', 'w')
    json.dump(data, s, ensure_ascii=False)
