#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: ChengXin
@contact:1921134176@qq.com
@version: 1.0.0
@license: Apache Licence
@file: app.py
@time: 2022/10/28 13:27
"""
# 版本flask==2.0.3 flask_sqlalchemy==2.5.0
from flask import request, jsonify, send_file
import re
import requests
import os
import pandas as pd
import json
import geopandas as gpd
from werkzeug.utils import redirect
from .models import db, app, Casearth
# 若运行当前的app.py则需要用from kgserver.models import app，因为当前运行会被认为是main module，无法找到相对路径
from kgserver import utilsql
from kgserver import kgcontrol
from qa_system_on_kg import *

os.environ['NO_PROXY'] = 'https://data.casearth.cn'  # 如果开了vpn需要此配置
app.secret_key = "asdasdasdasdasdsaa"
# 初始化图数据库
kgdb = kgcontrol.Kgdb("http://localhost:11005", 'neo4j', '201314')
chatBot = ChatBotGraph("http://localhost:11005", 'neo4j', '201314')
df = None


# 前端检查的响应码
# statusCode: {
# // 响应成功
# success: 200,
# // 未登录, 或登录失效
# notLogin: 401,
# // 权限不足
# authorize: 403,
# // 系统内部错误
# error: 500
# }
# ----------------------------------------------------欢迎页接口--------------------------------------------------------
# 登录接口
@app.route("/login", methods=["POST"])
def login():
    user = request.get_json()
    username = user.get("username")
    password = user.get("password")
    isUser = utilsql.hasUser(username, password)
    if isUser == 1:
        return jsonify(msg="登录成功", code=200)
    elif isUser == 2:
        return jsonify(msg="密码错误", code=401)
    else:
        return jsonify(msg="用户不存在", code=401)


# 注册接口
@app.route("/register", methods=["post"])
def register():
    user = request.get_json()
    username = user.get("username")
    password = user.get("password")
    isUser = utilsql.hasUser(username, password)
    if isUser == 1:
        return jsonify(msg="用户已存在", code=401)
    elif isUser == 2:
        return jsonify(msg="用户已存在", code=401)
    else:
        utilsql.addUser(username, password)
        return jsonify(msg="注册成功", code=200)


# 欢迎页1图片img
@app.route("/welcome/page1/<image>", methods=["get"])
def welcomePage1Img(image):
    image = './static/welcome_page_img/' + image
    return send_file(image, mimetype='image/gif')


# 欢迎页2图片img
@app.route("/welcome/page2", methods=["get"])
def welcomePage2Data():
    """
    返回欢迎页2的所有图像，添加数据直接在文件夹添加
    :return:
    """
    imgNameList = os.listdir('./kgserver/static/welcome_page2/')
    webUrlList = [i[1:-5].replace(".", "://", 1) for i in imgNameList]
    imgUrlList = ["http://10.101.121.31:5000/welcome/page2/" + i for i in imgNameList]  # 换网络地址需要重新修改
    res = list(zip(imgUrlList, webUrlList))
    return jsonify(data=res, code=200)


# 欢迎页2图片img
@app.route("/welcome/page2/<image>", methods=["get"])
def welcomePage2Img(image):
    image = './static/welcome_page2/' + image
    return send_file(image, mimetype='image/gif')


# ----------------------------------------------------知识管理页接口------------------------------------------------------
# 单节点获取接口
@app.route("/manage/kg/getOneNode", methods=["get"])
def getOneNode():
    label = request.args.get("label")
    key = request.args.get("key")
    value = request.args.get("value")
    data = kgdb.getOneNode(key, value, label)
    return jsonify(data=data, code=200)


# 单节点information获取接口
NAME_DICT = {'name': '名称', 'center': '中心点', 'area': '面积', 'unit': '计量单位', 'data': '数据',
             'author': '作者', 'company': '工作单位', 'link': '链接', 'resolution': '分辨率', 'year': '年份',
             '共享方式': '共享方式', '地域范围': '地域范围', '数据内容': '数据内容', '数据格式': '数据格式', '数据类型': '数据类型',
             'compare_dataset': '比较数据集', 'proxy': '指标', 'type': '类型', 'id': 'ID', 'address': '地址'}


@app.route("/manage/kg/getNodeInformation", methods=["get"])
def getNodeInformation():
    nodeid = request.args.get("nodeid")
    nodeInfo = kgdb.getNodeInformation(nodeid)
    data = {}
    column = []
    for key in nodeInfo:
        if key in NAME_DICT:
            data[key] = nodeInfo[key]
            column.append({'label': NAME_DICT[key], 'prop': key})
    return jsonify(data=data, column=column, code=200)


@app.route("/manage/kg/getRelationshipInformation", methods=["get"])
def getRelationshipInformation():
    relationshipId = request.args.get("relationshipId")
    relationshipType = request.args.get("relationshipType")
    relationshipInfo = kgdb.getRelationshipInformation(relationshipId)
    data = {}
    column = []
    for key in relationshipInfo:
        if key in NAME_DICT:
            data[key] = relationshipInfo[key]
            column.append({'label': NAME_DICT[key], 'prop': key})
    return jsonify(data=data, column=column, code=200)


# cypher执行接口
@app.route("/manage/kg/runCypher", methods=["get"])
def runCypher():
    cypher = request.args.get("cypher")
    node = kgdb.runCypher(cypher)
    return jsonify(data=node, code=200)


# 创建节点接口
@app.route("/manage/kg/createNode", methods=["get"])
def createNode():
    label = request.args.get("label")
    attribute = request.args.get("attribute")
    node = kgdb.addNode(label, attribute)
    return jsonify(data=node, code=200)


# 修改节点接口
@app.route("/manage/kg/setNode", methods=["get"])
def setNode():
    id = request.args.get("id")
    attribute = request.args.get("attribute")
    node = kgdb.setNode(id, attribute)
    return jsonify(data=node, code=200)


# 删除节点接口
@app.route("/manage/kg/delNode", methods=["get"])
def delNode():
    id = request.args.get("id")
    node = kgdb.delNode(id)
    return jsonify(data=node, code=200)


# 查询节点接口
@app.route("/manage/kg/matchNode", methods=["get"])
def matchNode():
    label = request.args.get("label")
    whereAttribute = request.args.get("whereAttribute")
    node, msg = kgdb.matchNode(label, whereAttribute)
    return jsonify(data=node, msg=msg, code=200)


# 创建边接口
@app.route("/manage/kg/createEdge", methods=["get"])
def createEdge():
    hid = request.args.get("hid")
    tid = request.args.get("tid")
    rtype = request.args.get("type")
    attribute = request.args.get("attribute")
    node = kgdb.addedge(hid, tid, rtype, attribute)
    return jsonify(data=node, code=200)


# 修改边接口
@app.route("/manage/kg/setEdge", methods=["get"])
def setEdge():
    id = request.args.get("id")
    attribute = request.args.get("attribute")
    node = kgdb.setEdge(id, attribute)
    return jsonify(data=node, code=200)


# 删除边接口
@app.route("/manage/kg/delEdge", methods=["get"])
def delEdge():
    id = request.args.get("id")
    node = kgdb.delEdge(id)
    return jsonify(data=node, code=200)


# 查询边接口
@app.route("/manage/kg/matchEdge", methods=["get"])
def matchEdge():
    rtype = request.args.get("type")
    whereAttribute = request.args.get("whereAttribute")
    data, links, msg = kgdb.matchEdge(rtype, whereAttribute)
    return jsonify(data=data, links=links, msg=msg, code=200)


# 联合查询边接口
@app.route("/manage/kg/matchEdgeNode", methods=["get"])
def matchEdgeNode():
    hlabel = request.args.get("hlabel")
    hwhereAttribute = request.args.get("hwhereAttribute")
    tlabel = request.args.get("tlabel")
    twhereAttribute = request.args.get("twhereAttribute")
    rtype = request.args.get("type")
    rwhereAttribute = request.args.get("rwhereAttribute")
    data, links, msg = kgdb.matchEdgeNode(hlabel, hwhereAttribute, tlabel, twhereAttribute, rtype, rwhereAttribute)
    return jsonify(data=data, links=links, msg=msg, code=200)


filePath = ''


# 上传xlsx接口
# 有bug，应该获取前端返回的文件数据，而不是文件名
@app.route("/manage/kg/xlsxFileLoad", methods=["get"])
def xlsxFileLoad():
    global df
    global filePath
    filePath = request.args.get("filePath")
    dataType = request.args.get("fileType")
    filePath = 'F:\\网络开发学习资料\\vue\\my-web\\multimodal_data\\' + filePath
    if dataType == '.xlsx':
        df = pd.read_excel(filePath)
    elif dataType == '.csv':
        df = pd.read_csv(filePath)
    data = df.to_dict('records')
    return jsonify(data=data, code=200)


# xlsx数据创建知识图谱接口
@app.route("/manage/kg/xlsxCreateKg", methods=["get"])
def xlsxCreateKg():
    data = df.to_dict('records')
    node = kgdb.load_xlsx(filePath.split('\\')[-1].split('_')[0], data)
    return jsonify(data=node, code=200)


pathkg = ''


# 上传shp接口
@app.route("/manage/kg/shpFileLoad", methods=["get"])
def shpFileLoad():
    global pathkg
    filePath = request.args.get("filePath")
    dataType = request.args.get("fileType")
    if dataType == '.json, .geojson':
        filePath = 'F:\\网络开发学习资料\\vue\\my-web\\multimodal_data\\' + filePath
        pathkg = filePath
        with open(filePath, 'r') as f:
            content = f.read()
            data = json.loads(content)
    elif dataType == '.shp':
        if not os.path.exists(
                'F:\\网络开发学习资料\\vue\\my-web\\multimodal_data\\德国行政区划\\' + filePath.split('.')[0] + '.geojson'):
            filePath1 = 'F:\\网络开发学习资料\\vue\\my-web\\multimodal_data\\德国行政区划\\' + filePath
            pathkg = filePath1
            out_data = gpd.read_file(filePath1)
            crs = out_data.crs
            out_data = gpd.GeoSeries(out_data.geometry, crs=crs)
            out_data.to_file(
                'F:\\网络开发学习资料\\vue\\my-web\\multimodal_data\\德国行政区划\\' + filePath.split('.')[0] + '.geojson',
                driver='GeoJSON', encoding="utf-8")
        with open('F:\\网络开发学习资料\\vue\\my-web\\multimodal_data\\德国行政区划\\' + filePath.split('.')[0] + '.geojson', 'r',
                  encoding='utf-8') as f:
            content = f.read()
            data = json.loads(content)
    return jsonify(data=data, code=200)


# shp数据创建知识图谱接口
@app.route("/manage/kg/shpCreateKg", methods=["get"])
def shpCreateKg():
    # 只适用于德国这个数据
    data = gpd.read_file(pathkg)
    data = data.to_dict('records')
    node = kgdb.load_shp(data)
    return jsonify(data=node, code=200)


# ----------------------------------------------------智能问答页接口------------------------------------------------------
# 智能问答-思知对话机器人接口
@app.route("/bot", methods=["get"])
def bot():
    appid = '521237838778735920fa1c8df3cb4a0b'
    userid = 'tiYCUZJP'
    spoken = request.args.get("spoken")
    # 先用自己的机器人
    entities, answer = chatBot.chat_main(spoken)
    if answer != '':
        botAnswer = {'data': {'info': {'text': answer}}}
    else:
        url = f"https://api.ownthink.com/bot?appid={appid}&userid={userid}&spoken={spoken}"
        botAnswer = requests.request("GET", url, verify=False).json()
    # 获取知识图谱的数据
    nodeData = []
    linksData = []
    if len(entities):
        for entitiesName in entities:
            label = entities[entitiesName][0]
            data, links = kgdb.nodeReNodeAlias(label, entitiesName)
            nodeData += data
            linksData += links
    # 获取知识卡片的数据
    kgCardData = {}
    kgCardcolumn = []
    try:
        if len(entities):
            locationName = list(entities.keys())[0]
            url1 = f"https://dmfw.mca.gov.cn/9095/stname/listPub?stName={locationName}&searchType=精确"
            data1 = requests.request("POST", url1, verify=False)
            data1 = data1.json()
            locationId = data1['records'][0]['id']
            url2 = f"https://dmfw.mca.gov.cn/9095/stname/detailsPub?id={locationId}"
            data2 = requests.request("POST", url2, verify=False)
            data2 = data2.json()
            for key in data2:
                if key in locationInfoDict and data2[key]:
                    kgCardData[key] = data2[key]
                    kgCardcolumn.append({'label': locationInfoDict[key], 'prop': key})
        return jsonify(bot=botAnswer, kgnode=nodeData, kglinks=linksData, kgCardData=kgCardData, kgCardcolumn=kgCardcolumn,
                       code=200)
    except:
        return jsonify(bot=botAnswer, kgnode=nodeData, kglinks=linksData, kgCardData=kgCardData, kgCardcolumn=kgCardcolumn, code=200)


# ----------------------------------------------------数据推荐页接口------------------------------------------------------
# 数据推荐页数据列表
@app.route("/datarecommendation/cardlist", methods=["get"])
def cardList():
    allField = Casearth.query.all()
    res = []
    templete = r"id=(.*?)&userType="
    for i in allField:
        sdoId = re.findall(templete, i.sdoId)
        # 数据详情页面
        fieldData = [i.title, i.iconPath, i.releaseDate, i.dataFormat, i.desc, sdoId[0], i.productSN]  # 直接网站地址
        # fieldData = [i.title, f"http://localhost:5000/datarecommendation/{i.iconPath.split('/')[-1]}", i.releaseDate, i.dataFormat, i.desc, sdoId]  # 本地网站地址
        res.append(fieldData)
    return jsonify(title=res, code=200)


# 数据推荐页数据列表图片img
@app.route("/datarecommendation/<image>", methods=["get"])
def cardListImg(image):
    image = './static/img/' + image
    return send_file(image, mimetype='image/gif')


# 数据推荐页标签云接口
@app.route("/datarecommendation/tagcloud", methods=["get"])
def tagCloud():
    with open('kgserver/static/CasearthTag.txt', 'r') as f:
        tags = f.read()
    tagList = tags.split(',')
    res = [{'text': i} for i in tagList]
    return jsonify(taglist=res, code=200)


# 数据推荐页数据详细描述对话框
@app.route("/datarecommendation/descDialog", methods=["get"])
def descDialog():
    sdoid = request.args.get("sdoid")
    dataUrl = f"https://data.casearth.cn/sdo/visitSdo?id={sdoid}&userType="
    record = Casearth.query.filter_by(sdoId=dataUrl).first()
    # 更新一下载量与访问量的数据
    re = requests.request("GET", dataUrl, verify=False)
    productJson = re.json()
    record.visitCount = productJson['vCount']
    record.downloadCount = productJson['dCount']
    res = {}
    res['desc'] = record.desc
    res['objectUrl'] = record.objectUrl
    res['taxonomy'] = record.taxonomy
    res['startTime'] = record.startTime
    res['endTime'] = record.endTime
    res['spatialResolution'] = record.spatialResolution
    res['timeResolution'] = record.timeResolution
    res['rangeDescription'] = record.rangeDescription
    res['shareMethod'] = record.shareMethod
    res['productSN'] = record.productSN
    res['publishDepartment'] = record.publishDepartment
    res['publisher'] = record.publisher
    res['releaseDate'] = record.releaseDate
    res['filesNumber'] = record.filesNumber
    res['mSize'] = record.mSize
    res['visitCount'] = productJson['vCount']
    res['downloadCount'] = productJson['dCount']
    res['dataFormat'] = record.dataFormat
    res['datatype'] = record.datatype
    res['keyword'] = record.keyword
    res['tagStr'] = record.tagStr
    db.session.commit()
    return jsonify(data=res, code=200)


# 数据推荐页知识图谱接口
@app.route("/datarecommendation/knowledgeGraph", methods=["get"])
def KnowledgeGraph():
    productSN = request.args.get("productSN")
    data, links = kgdb.getProductAttribute(productSN)
    return jsonify(data=data, links=links, code=200)


# 数据推荐页知识图谱推荐接口
@app.route("/datarecommendation/reKnowledgeGraph", methods=["get"])
def reKnowledgeGraph():
    productSN = request.args.get("productSN")
    data, links = kgdb.getProductRecommendation(productSN)
    # 卡片视图数据
    cardData = []
    templete = r"id=(.*?)&userType="
    for index in range(1, len(data)):
        sn = data[index]['sn']
        i = Casearth.query.filter_by(productSN=sn).first()
        sdoId = re.findall(templete, i.sdoId)
        fieldData = [i.title, i.iconPath, i.releaseDate, i.dataFormat, i.desc, sdoId[0], i.productSN]
        cardData.append(fieldData)
    return jsonify(data=data, links=links, cardData=cardData, code=200)


# 数据推荐页产品知识图谱点击接口
@app.route("/datarecommendation/productKgClick", methods=["get"])
def productKgClick():
    nodeId = request.args.get("id")
    data, links = kgdb.getProductKgClickData(nodeId)
    return jsonify(data=data, links=links, code=200)


# 数据推荐页推荐知识图谱点击返回产品
@app.route("/datarecommendation/recommendationItem", methods=["get"])
def recommendationItem():
    productSN = request.args.get("productSN")
    templete = r"id=(.*?)&userType="
    i = Casearth.query.filter_by(productSN=productSN).first()
    sdoId = re.findall(templete, i.sdoId)
    fieldData = [i.title, i.iconPath, i.releaseDate, i.dataFormat, i.desc, sdoId[0], i.productSN]
    return jsonify(data=fieldData, code=200)


# 数据推荐页搜索接口
@app.route("/datarecommendation/recommendationSearch", methods=["get"])
def recommendationSearch():
    searchText = request.args.get("searchText")
    res = []
    templete = r"id=(.*?)&userType="
    allField = Casearth.query.filter(Casearth.title.contains(f'{searchText}')).all()
    for i in allField:
        sdoId = re.findall(templete, i.sdoId)
        fieldData = [i.title, i.iconPath, i.releaseDate, i.dataFormat, i.desc, sdoId[0], i.productSN]
        res.append(fieldData)
    return jsonify(data=res, code=200)


# ----------------------------------------------------领域共享国土页接口--------------------------------------------------------
# 国土知识图谱初始化展示接口
@app.route("/guotu/kg/init", methods=["get"])
def guotuKgInit():
    label = request.args.get("label")
    alias = request.args.get("name")
    data, links = kgdb.nodeRelationshipNode(label, alias)
    return jsonify(data=data, links=links, code=200)


# 国土知识图谱点击geo更新接口
@app.route("/guotu/kg/update_from_geo", methods=["get"])
def guotuKgUpdateFromGeo():
    name = request.args.get("name")
    data, links = kgdb.nodeReNodeName(name)
    return jsonify(data=data, links=links, code=200)


# 国土知识图谱点击数据类型节点数据挖掘视图
@app.route("/guotu/kg/update_from_nodeid", methods=["get"])
def guotuKgUpdateFromId():
    node_id = request.args.get("id")
    data, links = kgdb.nodeReNodeId(node_id)
    return jsonify(data=data, links=links, code=200)


locationInfoDict = {'place_type': '地名类别', 'old_name': '历史地名', 'place_origin': '地名的来历',
                    'place_history': '地名的历史沿革', 'place_meaning': '地名的含义', 'government_history': '政区的历史沿革'}


# 领域共享-知识卡片数据获取接口
@app.route("/guotu/kg/kgCardUpdate", methods=["get"])
def kgCardUpdate():
    nodeId = request.args.get("id")
    locationName = kgdb.getLocationName(nodeId)
    data = {}
    column = []
    try:
        if locationName:
            url1 = f"https://dmfw.mca.gov.cn/9095/stname/listPub?stName={locationName}&searchType=精确"
            data1 = requests.request("POST", url1, verify=False)
            data1 = data1.json()
            locationId = data1['records'][0]['id']
            url2 = f"https://dmfw.mca.gov.cn/9095/stname/detailsPub?id={locationId}"
            data2 = requests.request("POST", url2, verify=False)
            data2 = data2.json()
            for key in data2:
                if key in locationInfoDict and data2[key]:
                    data[key] = data2[key]
                    column.append({'label': locationInfoDict[key], 'prop': key})
        return jsonify(data=data, column=column, code=200)
    except:
        return jsonify(data=data, column=column, code=200)


# @app.route("/", methods=["GET"])
# def hello_world():
#     return "hello 音宫"
#
#
# @app.route("/hey/<username>")
# def hey_yingong(username):
#     return "我是 %s" % (username + username)
#
#
# @app.route("/my/<float:number>")
# def my_number(number):
#     return "我的数字 %s" % (number + number)
#
#
# # 重定向
# @app.route("/bilibili")
# def bilibili():
#     return redirect("https://www.bilibili.com/")
#
#
# # json接口
# @app.route("/test/my/first", methods=["POST"])
# def first_post():
#     try:
#         my_json = request.get_json()
#         print(my_json)
#         get_name = my_json.get("name")
#         get_age = my_json.get("age")
#         if not all([get_name, get_age]):
#             return jsonify(msg="缺少参数")
#
#         get_age += 10
#
#         return jsonify(name=get_name, age=get_age)
#     except Exception as e:
#         print(e)
#         return jsonify(msg="出错了哦，请查看是否正确访问")
#
#
# # 登录
# @app.route("/try/login", methods=["POST"])
# def login():
#     """
#     账号 username asd123
#     密码 password asdasd
#     :return:
#     """
#     get_data = request.get_json()
#     username = get_data.get("username")
#     password = get_data.get("password")
#
#     if not all([username, password]):
#         return jsonify(msg="参数不完整")
#
#     if username == "asd123" and password == "asdasd":
#         # 如果验证通过 保存登录状态在session中
#         session["username"] = username
#         return jsonify(msg="登录成功")
#     else:
#         return jsonify(msg="账号或密码错误")
#
#
# # 检查登录状态
# @app.route("/session", methods=["GET"])
# def check_session():
#     username = session.get("username")
#     if username is not None:
#         # 操作逻辑 数据库什么的
#         # 数据库里面 把你的头像 等级 金币数量 查询出来
#         return jsonify(username=username)
#     else:
#         return jsonify(msg="出错了，没登录")
#
#
# # 登出
# @app.route("/try/logout", methods=["GET"])
# def logout():
#     session.clear()
#     return jsonify(msg="成功退出登录!")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
