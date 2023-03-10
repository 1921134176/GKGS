#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: ChengXin
@contact:1921134176@qq.com
@version: 1.0.0
@license: Apache Licence
@file: wuhan_school_crawler.py
@time: 2023/3/1 22:48
"""

import json
import requests
import pandas as pd


# 获取json返回字典
def getJson(url):
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,'
                         '*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh,zh-TW;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
               'Cache-Control': 'max-age=0',
               'Connection': 'keep-alive',
               'Cookie': 'HWWAFSESID=aafdffd4376e1fa35f; HWWAFSESTIME=1627540479256',
               'Host': 'api.tianditu.gov.cn',
               'Upgrade-Insecure-Requests': '1',
               'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/91.0.4472.124 Safari/537.36'}
    html = requests.get(url, headers=headers)
    modelJson = html.text
    # 模型字典
    modelDict = json.loads(modelJson)
    return modelDict


if __name__ == "__main__":
    cityName = '长沙市'
    key = 'd223161b1a596fde33b7360f9411534a'
    # 武汉市行政区请求
    url_wuhan = f'http://api.tianditu.gov.cn/administrative?postStr={{"searchWord":"{cityName}","searchType":"1","needSubInfo":"true","needAll":"true","needPolygon":"true","needPre":"true"}}&tk=' + key
    wuHan = getJson(url_wuhan)
    wuHan_administrative = wuHan['data'][0]['child']
    # 武汉市区划及其代码
    adminDict = {}
    for admin in wuHan_administrative:
        adminDict[admin['name']] = admin['cityCode']
    # 武汉市行政区学校请求
    adminSchoolList = []
    adminSchoolDict = {}
    for (k, v) in adminDict.items():
        url_kindergarten = 'http://api.tianditu.gov.cn/v2/search?postStr={"queryType":13,"start":0,"count":300,' \
                           '"specify":' + v + ',"dataTypes":"幼儿园"}&type=query&tk=' + key
        url_primary = 'http://api.tianditu.gov.cn/v2/search?postStr={"queryType":13,"start":0,"count":300,' \
                      '"specify":' + v + ',"dataTypes":"小学"}&type=query&tk=' + key
        url_middle = 'http://api.tianditu.gov.cn/v2/search?postStr={"queryType":13,"start":0,"count":300,' \
                     '"specify":' + v + ',"dataTypes":"中学"}&type=query&tk=' + key
        url_secondary = 'http://api.tianditu.gov.cn/v2/search?postStr={"queryType":13,"start":0,"count":300,' \
                        '"specify":' + v + ',"dataTypes":"中专"}&type=query&tk=' + key
        url_university = 'http://api.tianditu.gov.cn/v2/search?postStr={"queryType":13,"start":0,"count":300,' \
                         '"specify":' + v + ',"dataTypes":"大专院校"}&type=query&tk=' + key
        url_driver = 'http://api.tianditu.gov.cn/v2/search?postStr={"queryType":13,"start":0,"count":300,' \
                     '"specify":' + v + ',"dataTypes":"驾校"}&type=query&tk=' + key
        url_party = 'http://api.tianditu.gov.cn/v2/search?postStr={"queryType":13,"start":0,"count":300,' \
                    '"specify":' + v + ',"dataTypes":"党校"}&type=query&tk=' + key
        urlList = [url_kindergarten, url_primary, url_middle, url_secondary, url_university, url_driver, url_party]
        urlName = ['幼儿园', '小学', '中学', '中专', '大专院校', '驾校', '党校']
        schoolList = []
        schoolDict = {}
        for i in range(0, len(urlList)):
            schoolName = []
            schoolInfo = getJson(urlList[i])
            if int(schoolInfo['count']) > 0:
                for kk in range(int(schoolInfo['count'])//100+1):
                    schoolInfo2 = getJson(f'http://api.tianditu.gov.cn/v2/search?postStr={{"queryType":13,"start":{kk * 100},"count":100,"specify":{v},"dataTypes":"{urlName[i]}"}}&type=query&tk={key}')
                    for j in schoolInfo2['pois']:
                        schoolName.append({'name': j['name'], 'address': j['address'], 'task_id': 'school'})
                # if int(schoolInfo['count']) < 300:
                #     for j in schoolInfo['pois']:
                #         schoolName.append({'name': j['name'], 'address': j['address'], 'task_id': 'school'})
                # else:
                #     for j in schoolInfo['pois']:
                #         schoolName.append({'name': j['name'], 'address': j['address'], 'task_id': 'school'})
                #     schoolInfo = getJson('http://api.tianditu.gov.cn/v2/search?postStr={"queryType":13,"start":300,"count":100,"specify":156420115,"dataTypes":"幼儿园"}&type=query&tk=d223161b1a596fde33b7360f9411534a')
                #     for j in schoolInfo['pois']:
                #         schoolName.append({'name': j['name'], 'address': j['address'], 'task_id': 'school'})
                #     print(k, urlList[i], '有遗漏')
            schoolDict[urlName[i]] = schoolName
        adminSchoolDict[k] = schoolDict
    head_node_label = []
    head_node_attritute = []
    r_type = []
    r_attritube = []
    tail_node_label = []
    tail_node_attribute = []
    for district in adminSchoolDict:
        for schoolType in adminSchoolDict[district]:
            for school in adminSchoolDict[district][schoolType]:
                head_node_label.append('district')
                head_node_attritute.append(f"name:'{district}'")
                r_type.append('school')
                r_attritube.append(f"name:'{schoolType}'")
                tail_node_label.append(schoolType)
                tail_node_attribute.append(f"name:'{school['name']}',address:'{school['address']}', task_id:'{school['task_id']}'")
    dfData = {
        'head_node_label':head_node_label,
        'head_node_attritute': head_node_attritute,
        'r_type': r_type,
        'r_attritube': r_attritube,
        'tail_node_label': tail_node_label,
        'tail_node_attribute': tail_node_attribute
    }
    df = pd.DataFrame(dfData)  # 创建DataFrame
    df.to_excel(f'{cityName}_school.xlsx', index=False)  # 存表，去除原始索引列（0,1,2...）
    df.to_csv(f'{cityName}_school.csv', index=False)