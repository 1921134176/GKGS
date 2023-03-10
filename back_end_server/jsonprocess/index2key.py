#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: ChengXin
@contact:1921134176@qq.com
@version: 1.0.0
@license: Apache Licence
@file: index2key.py
@time: 2022/11/18 22:33
"""
import json
if __name__ == "__main__":
    """
    把index.json做成字典形式方便查找
    """
    with open('./index.json', 'r', encoding='utf-8') as f:
        index = json.load(f)
    out = {}
    for i in index:
        out[i['id']] = {'name': i['name'], 'geo': i['geo']}
    with open('./id_index.json', 'w', encoding='utf-8') as f:
        json.dump(out, f)
    print('end')