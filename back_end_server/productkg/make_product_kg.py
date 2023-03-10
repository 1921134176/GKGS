#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: ChengXin
@contact:1921134176@qq.com
@version: 1.0.0
@license: Apache Licence
@file: make_product_kg.py
@time: 2023/3/6 16:01
"""
import sqlite3
from py2neo import GraphService, Graph


def makeProductKg(sqlitePath):
    """
    从遥感产品表制作遥感产品知识图谱
    将有实际意义的字段都做为知识图谱的一类节点，产品节点与属性节点间都是属性关系连接，只有相同类型节点之间才有特殊类型的关系。
    这样的设计不会增加检索量，但是能更好的反应产品节点之间存在的关系，适合推荐，与基于相似度的推荐异曲同工。
    :return:
    """
    # neo4j数据库连接
    user_name = 'neo4j'
    user_password = '201314'
    httpUrl = 'http://localhost:11005/'
    graphName = 'product'
    # graphService = GraphService(httpUrl, auth=(user_name, user_password))
    # graph = graphService[graphName]
    graph = Graph(httpUrl, auth=(user_name, user_password), name=graphName)

    # 创建与数据库的连接
    conn = sqlite3.connect(sqlitePath)
    # 创建一个游标 cursor
    cur = conn.cursor()
    # 查询语句
    sql_text_3 = "SELECT * FROM casearth"
    cur.execute(sql_text_3)
    # 获取查询结果
    res = cur.fetchall()
    # 关闭游标
    cur.close()
    # 关闭连接
    conn.close()

    produceSn_title = [[i[1], i[2]] for i in res]
    for product in produceSn_title:
        graph.run(f"create(:product{{productSN:'{product[0]}',title:'{product[1]}'}})")

    releaseDate = list(set([i[5] for i in res if i[5] != '']))
    for item in releaseDate:
        try:
            graph.run(f"create(:releaseDate{{value:'{item}'}})")
        except:
            graph.run(f"create(:releaseDate{{value:\"{item}\"}})")

    startDate = list(set([i[6] for i in res if i[6] != '']))
    for item in startDate:
        try:
            graph.run(f"create(:startDate{{value:'{item}'}})")
        except:
            graph.run(f"create(:startDate{{value:\"{item}\"}})")

    endDate = list(set([i[7] for i in res if i[7] != '']))
    for item in endDate:
        try:
            graph.run(f"create(:endDate{{value:'{item}'}})")
        except:
            graph.run(f"create(:endDate{{value:\"{item}\"}})")

    taxonomy = list(set([i[9] for i in res if i[9] != '']))
    for item in taxonomy:
        try:
            graph.run(f"create(:taxonomy{{value:'{item}'}})")
        except:
            graph.run(f"create(:taxonomy{{value:\"{item}\"}})")

    productType = list(set([i[12] for i in res if i[12] != '']))
    for item in productType:
        try:
            graph.run(f"create(:productType{{value:'{item}'}})")
        except:
            graph.run(f"create(:productType{{value:\"{item}\"}})")

    publishDepartmentTemp = list(set([i[13] for i in res if i[13] != '']))
    publishDepartment = dataSplit(publishDepartmentTemp)
    for item in publishDepartment:
        try:
            graph.run(f"create(:publishDepartment{{value:'{item}'}})")
        except:
            graph.run(f"create(:publishDepartment{{value:\"{item}\"}})")

    dataFormatTemp = list(set([i[14] for i in res if i[14] != '']))
    dataFormat = dataSplit(dataFormatTemp)
    for item in dataFormat:
        try:
            graph.run(f"create(:dataFormat{{value:'{item}'}})")
        except:
            graph.run(f"create(:dataFormat{{value:\"{item}\"}})")

    dataTypeTemp = list(set([i[15] for i in res if i[15] != '']))
    dataType = dataSplit(dataTypeTemp)
    for item in dataType:
        try:
            graph.run(f"create(:dataType{{value:'{item}'}})")
        except:
            graph.run(f"create(:dataType{{value:\"{item}\"}})")

    timeResolutionTemp = list(set([i[16] for i in res if i[16] != '']))
    timeResolution = dataSplit(timeResolutionTemp)
    for item in timeResolution:
        try:
            graph.run(f"create(:timeResolution{{value:'{item}'}})")
        except:
            graph.run(f"create(:timeResolution{{value:\"{item}\"}})")

    spatialResolutionTemp = list(set([i[17] for i in res if i[17] != '']))
    spatialResolution = dataSplit(spatialResolutionTemp)
    for item in spatialResolution:
        try:
            graph.run(f"create(:spatialResolution{{value:'{item}'}})")
        except:
            graph.run(f"create(:spatialResolution{{value:\"{item}\"}})")

    keywordTemp = list(set([i[18] for i in res if i[18] != '']))
    keyword = dataSplit(keywordTemp)
    for item in keyword:
        try:
            graph.run(f"create(:keyword{{value:'{item}'}})")
        except:
            graph.run(f"create(:keyword{{value:\"{item}\"}})")

    userTagTemp = list(set([i[19] for i in res if i[19] != '']))
    userTag = dataSplit(userTagTemp)
    for item in userTag:
        try:
            graph.run(f"create(:userTag{{value:'{item}'}})")
        except:
            graph.run(f"create(:userTag{{value:\"{item}\"}})")

    publisherTemp = list(set([i[21] for i in res if not i[21] is None]))
    publisher = dataSplit(publisherTemp)
    for item in publisher:
        try:
            graph.run(f"create(:publisher{{value:'{item}'}})")
        except:
            graph.run(f"create(:publisher{{value:\"{item}\"}})")

    rangeDescriptionTemp = list(set([i[25] for i in res if i[25] != '']))
    rangeDescription = dataSplit(rangeDescriptionTemp)
    for item in rangeDescription:
        try:
            graph.run(f"create(:rangeDescription{{value:\"{item}\"}})")
        except:
            graph.run(f"create(:rangeDescription{{value:\"{item}\"}})")

    shareMethod = list(set([i[27] for i in res if i[27] != '']))
    for item in shareMethod:
        try:
            graph.run(f"create(:shareMethod{{value:'{item}'}})")
        except:
            graph.run(f"create(:shareMethod{{value:\"{item}\"}})")

    # 创建关系
    index = [5, 6, 7, 9, 12, 13, 14, 15, 16, 17, 18, 19, 21, 25, 27]
    label = ['releaseDate', 'startDate', 'endDate', 'taxonomy', 'productType',
             'publishDepartment', 'dataFormat', 'dataType', 'timeResolution', 'spatialResolution',
             'keyword', 'userTag', 'publisher', 'rangeDescription', 'shareMethod']
    for item in res:
        for (i, j) in zip(index, label):
            if item[i] != '' and not item[i] is None:
                for value in strSplit(item[i]):
                    try:
                        graph.run(f"match(n1:product{{productSN:'{item[1]}'}}), (n2:{j}{{value:\"{value}\"}}) "
                                  f"create(n1)-[:attribute]->(n2)")
                    except:
                        graph.run(f"match(n1:product{{productSN:'{item[1]}'}}), (n2:{j}{{value:'{value}'}}) "
                                  f"create(n1)-[:attribute]->(n2)")


def dataSplit(dataList):
    res = []
    for data in dataList:
        res.extend(data.split(';'))
        res.extend(data.split('；'))
        res.extend(data.split('、'))
        res.extend(data.split('，'))
        res.extend(data.split(','))
    res = set(res)
    for data in dataList:
        if ';' in data or '；' in data or '、' in data or '，' in data or ',' in data:
            res.remove(data)
    if '' in res:
        res.remove('')
    return list(res)


def strSplit(string):
    res = []
    res.extend(string.split(';'))
    res.extend(string.split('；'))
    res.extend(string.split('、'))
    res.extend(string.split('，'))
    res.extend(string.split(','))
    res = set(res)
    if ';' in string or '；' in string or '、' in string or '，' in string or ',' in string:
        res.remove(string)
    if '' in res:
        res.remove('')
    return list(res)


if __name__ == "__main__":
    makeProductKg('../kgserver/kgsql.db')
