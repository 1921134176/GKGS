#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: ChengXin
@contact:1921134176@qq.com
@version: 1.0.0
@license: Apache Licence
@file: utilsql.py
@time: 2022/11/15 15:25
"""
from kgserver.models import db, User


# 添加用户
def addUser(username, password):
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()


# 查询用户是否存在
def hasUser(username, password):
    user = User.query.filter_by(username=username).first()
    if user:
        if user.password == password:
            return 1
        else:
            return 2
    else:
        return 0


if __name__ == "__main__":
    # addUser('gkgs', '12345678')
    isUser = hasUser('gkgs', '12345678')
    print('end')