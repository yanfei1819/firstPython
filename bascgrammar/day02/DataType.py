# !/usr/bin/python
# -*- coding: utf-8 -*-

counter = 100
miles = 1000.02
name = "shiyanfei"

print(counter)
print(miles)
print(name)

# 多变量赋值
a = b = c = 1
print(a)
print(c)

a, bv = 2, "name"
print(a)
print(bv)

# Number  String List(列表)  Tuple(元组)  Dictionary(字典) -- 五种数据类型
# Number : int long float complex-复数
var1 = 1

# 删除变量值
del var1
var1 = 2
print(var1)

s = "abcdefghijklmnopqrstuvwxyz"
print(s[5])
print(s[2:5])
print(s[5:])
print(s * 4)

# List  可以支持字符，数据的混合
lists = ["ss", "sdrf", "w"]
print(lists)

# Tuple-类似list，但是不能二次赋值
tuples = ("name", 23, "b", 45)
print(tuples[2:4])

# 注意：列表可以重新赋值，元组是不能重新赋值，相当于只读列表

# python字典
dicts = {'name': "石焰飞", 3: 5}
print(dicts['name'])
print(dicts.keys())
print(dicts.values())

# 浮点数：一般采用科学计数法技术，小数点可以浮动，故名
