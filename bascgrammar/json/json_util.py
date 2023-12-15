# !/usr/bin/python
# -*- coding: utf-8 -*-

import json

data_json = {
    'name': 'syf',
    'age': 32,
    'sex': 'w'
}


def json_to_string(json_data):
    print(json_data)

    # json 转字符串，indent指定空格键
    json_string = json.dumps(json_data, indent=2)
    print(json_string)

    # JSON字符串转JSON对象
    json_string_data = '{"name":"lyf"}'
    new_json = json.loads(json_string)
    print(new_json)


if __name__ == '__main__':
    json_to_string(data_json)
