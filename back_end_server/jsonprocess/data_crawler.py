#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: ChengXin
@contact:1921134176@qq.com
@version: 1.0.0
@license: Apache Licence
@file: data_crawler.py
@time: 2022/12/8 22:23
爬虫程序
"""
import requests
import os
import json
from kgserver.models import db, Casearth

os.environ['NO_PROXY'] = 'https://data.casearth.cn'  # 如果开了vpn需要此配置


def crawlerCasearth():
    """
    爬取地球大数据科学工程平台数据https://data.casearth.cn/
    :return:
    """
    url = "https://data.casearth.cn/sdo/getData?prodId=&searchKey=&tags=&dataFormat=&sortName=score&tagstr=&publishDepartment=&categoryId=&pageNo=1&pageSize=1600"
    payload = {}
    headers = {
        'Cookie': 'JSESSIONID=D9D59DE52D8462BA1B80412785C2DCCB'
    }
    response = requests.request("GET", url, headers=headers, data=payload, verify=False)
    # response.text返回的是Unicode型的数据。
    # response.content返回的是bytes型的数据。用于图片
    # response.json返回json数据
    jsonData = response.json()
    # 标签列表，用于标签云
    tagNameList = [i['tagName'] for i in jsonData['tagList']]
    with open('../kgserver/static/CasearthTag.txt', 'w') as fp:
        fp.write(','.join(tagNameList))
    # 大类标签
    tagNameClassList = []
    # 数据列表
    for i in jsonData['list']:
        dataUrl = f"https://data.casearth.cn/sdo/visitSdo?id={i['sdoid']}&userType="
        re = requests.request("GET", dataUrl, verify=False)
        productJson = re.json()
        # 将大类标签加入标签列表
        if productJson['tagstr']:
            tagNameClassList += productJson['tagstr']
        # 保存图片
        imgUrl = f"https://data.casearth.cn{i['iconPath']}"
        reImg = requests.request("GET", imgUrl, verify=False)
        imgName = i['iconPath'].split('/')[-1]
        imgPath = '../kgserver/static/img/' + imgName
        with open(imgPath, 'wb') as fp:
            fp.write(reImg.content)
        # 存入数据库
        item = Casearth(
            productSN=productJson['productSN'],
            title=productJson['title'],
            iconPath=f"https://data.casearth.cn{i['iconPath']}",
            sdoId=f"https://data.casearth.cn/sdo/visitSdo?id={i['sdoid']}&userType=",
            releaseDate=productJson['publisher_publishTime'],
            startTime=productJson['startTime'],
            endTime=productJson['endTime'],
            filesNumber=productJson['fNumber'],
            taxonomy=i['taxonomy'],
            publishPhone=productJson['pTel'],
            visitCount=productJson['vCount'],
            productType=i['productType'],
            publishDepartment=productJson['pOrganization'],
            dataFormat=productJson['fileType'],
            datatype=productJson['dataType'],
            timeResolution=productJson['rTime'],
            spatialResolution=productJson['rSpatial'],
            keyword=i['keyword'],
            tagStr=i['tagstr'],
            publishEmail=productJson['pEmail'],
            publisher=productJson['pName'],
            downloadCount=productJson['dCount'],
            desc=productJson['desc'],
            objectUrl=productJson['objectUrl'],
            rangeDescription=productJson['rangeDescription'],
            mSize=productJson['mSize'],
            shareMethod=productJson['shareMethod']
        )
        db.session.add(item)
        db.session.commit()
    # 保存标签列表
    tagNameClassList = list(set(tagNameClassList))
    with open('../kgserver/static/CasearthTagClass.txt', 'w') as fp:
        fp.write(','.join(tagNameClassList))


if __name__ == "__main__":
    crawlerCasearth()
