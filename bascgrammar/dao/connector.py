# !/usr/bin/python
# -*- coding: utf-8 -*-
import mysql.connector


def test():
    conn = mysql.connector.connect(
        host='192.168.1.110',
        # port=3306,
        user='root',
        password='Wt20222..',
        database='taiji-vpp-syf'
    )
    print(conn)
    cursor = conn.cursor()
    print('执行开始')
    cursor.execute('create table user2 (id varchar(20) primary key, name varchar(20))')
    print('执行结束')
    print(cursor.rowcount)  ## 影响行数

    conn.commit()
    cursor.close()


if __name__ == '__main__':
    test()
