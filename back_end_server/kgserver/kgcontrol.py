#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: ChengXin
@contact:1921134176@qq.com
@version: 1.0.0
@license: Apache Licence
@file: kgcontrol.py
@time: 2022/11/26 20:57
"""
from py2neo import Graph

CATEGORY_INDEX = {'country': 0, 'province': 1, 'city': 2, 'district': 3, 'street': 4, 'region': 5, 'statistics': 6,
                  'proxy': 7, '幼儿园': 8, '小学': 9, '中学': 10, '中专': 11, '大专院校': 12, '驾校': 13, '党校': 14, 'State': 15,
                  'FreeState': 16}
PRODUCT_CATEGORY_INDEX = {'product': 0, 'releaseDate': 1, 'startDate': 1, 'endDate': 1, 'taxonomy': 1,
                          'productType': 1, 'publishDepartment': 1, 'dataFormat': 1, 'dataType': 1,
                          'timeResolution': 1, 'spatialResolution': 1, 'keyword': 1, 'userTag': 1,
                          'publisher': 1, 'rangeDescription': 1, 'shareMethod': 1}
PRODUCT_CHINESE_NAME = {'releaseDate': '发布时间', 'startDate': '开始时间', 'endDate': '结束时间', 'taxonomy': '学科分类',
                        'productType': '产品类型', 'publishDepartment': '出版单位', 'dataFormat': '数据格式',
                        'dataType': '数据类型', 'timeResolution': '时间分辨率', 'spatialResolution': '空间分辨率',
                        'keyword': '关键词', 'userTag': '用户标签', 'publisher': '作者', 'rangeDescription': '数据范围',
                        'shareMethod': '共享方式'}


# 国土领域知识图谱操作类
class Kgdb:
    def __init__(self, host, username, password):
        self.g = Graph(host, auth=(username, password))
        self.g_product = Graph(host, auth=(username, password), name='product')

    def getOneNode(self, key, value, label=None):
        """
        获取一个节点
        :param key:
        :param value:
        :return:
        """
        if label is None:
            kgdata = self.g.run(
                f"match (n1) where n1.{key}='{value}' return n1.name as name, id(n1) as id, labels(n1)[0] as label").data()
        else:
            kgdata = self.g.run(
                f"match (n1:{label}) where n1.{key}='{value}' return n1.name as name, id(n1) as id, labels(n1)[0] as label").data()
        return {'id': str(kgdata[0]['id']), 'name': kgdata[0]['name'], 'category': CATEGORY_INDEX[kgdata[0]['label']]}

    def getNodeInformation(self, nodeid):
        """
        获取节点信息
        :param nodeid:
        :return:
        """
        nodeData = self.g.run(f"match (n) where id(n)={nodeid} return n").data()[0]
        nodeData = dict(nodeData['n'])
        nodeData['id'] = nodeid
        if 'center' in nodeData:
            x = nodeData['center']['coordinates'][0]
            y = nodeData['center']['coordinates'][1]
            crs = nodeData['center']['crs']['name']
            nodeData['center'] = f"X:{x},Y:{y},CRS:{crs}"
        return nodeData

    def getRelationshipInformation(self, relationId):
        """
        获取关系信息
        :param relationId:
        :return:
        """
        res = {}
        res['id'] = relationId
        relationData = self.g.run(f"match ()-[r]->() where id(r)={relationId} return r, type(r) as type_r").data()[0]
        res.update(dict(relationData)['r'])
        res['type'] = relationData['type_r']
        return res

    def nodeRelationshipNode(self, label, alias):
        """
        根据label与name/alias获取数据
        :param label:
        :param alias:
        :return:
        """
        data = []
        links = []
        kgdata = self.g.run(
            f"match p=(n1:{label})-[r]->(n2) where n1.alias='{alias}' or n1.name='{alias}' return n1.name as h_name, id(n1) as h_id, type(r) as r, id(r) as r_id, labels(n2)[0] as label, n2.name as name, id(n2) as t_id").data()
        for index, value in enumerate(kgdata):
            data.append({'id': str(value['t_id']), 'name': value['name'], 'category': CATEGORY_INDEX[value['label']]})
            links.append({'source': str(value['h_id']), 'target': str(value['t_id']), 'value': value['r'],
                          'id': str(value['r_id'])})
        data.append({'id': str(value['h_id']), 'name': value['h_name'], 'category': CATEGORY_INDEX[label]})
        return [data, links]

    def nodeReNodeName(self, name):
        """
        根据name模糊查询数据，为了解决数据重复导致前端画图错误，加一个id字段(用neo4j中给节点的id)
        :param name:
        :return:
        """
        data = []
        links = []
        kgdata = self.g.run(
            f"match (n1)-[r]->(n2) where n1.name contains '{name}' return n1.name as name1, labels(n1)[0] as label1 ,"
            f"type(r) as r, id(r) as r_id, r.name as r_name, labels(n2)[0] as label, n2.name as name, n2.data as data, id(n1) as id_head, "
            f"id(n2) as id_tail").data()
        data.append({'id': str(kgdata[0]['id_head']), 'name': kgdata[0]['name1'],
                     'category': CATEGORY_INDEX[kgdata[0]['label1']]})  # id得用字符串，echarts需要
        for value in kgdata:
            if value['name']:
                data.append(
                    {'id': str(value['id_tail']), 'name': value['name'], 'category': CATEGORY_INDEX[value['label']]})
                links.append({'source': str(value['id_head']), 'target': str(value['id_tail']), 'value': value['r'],
                              'id': str(value['r_id'])})
            else:
                data.append({'id': str(value['id_tail']), 'name': str(round(value['data'], 2)),
                             'category': CATEGORY_INDEX[value['label']]})
                links.append(
                    {'source': str(value['id_head']), 'target': str(value['id_tail']), 'value': value['r_name'],
                     'id': str(value['r_id'])})
        return [data, links]

    def nodeReNodeId(self, id):
        """
        根据id查询下一级节点与关系
        :param id:
        :return:
        """
        data = []
        links = []
        kgdata = self.g.run(
            f"match (n1)-[r]->(n2) where id(n1)={id} return n1.name as name1, n1.data as data1, labels(n1)[0] as label1 ,"
            f"type(r) as r, id(r) as r_id, r.name as r_name, r.compare_dataset as compare_dataset, labels(n2)[0] as label, n2.name as name, n2.data as data, id(n1) as id_head, "
            f"id(n2) as id_tail").data()
        if kgdata[0]['name1']:
            data.append({'id': str(kgdata[0]['id_head']), 'name': kgdata[0]['name1'],
                         'category': CATEGORY_INDEX[kgdata[0]['label1']]})
        else:
            data.append({'id': str(kgdata[0]['id_head']), 'name': str(round(kgdata[0]['data1'], 2)),
                         'category': CATEGORY_INDEX[kgdata[0]['label1']]})
        for value in kgdata:
            if value['name'] and not value['data'] is None:
                data.append(
                    {'id': str(value['id_tail']), 'name': str(round(value['data'], 2)), 'des': value['name'],
                     'category': CATEGORY_INDEX[value['label']]})
                if value['r_name']:
                    links.append(
                        {'source': str(value['id_head']), 'target': str(value['id_tail']), 'value': value['r_name'],
                         'id': str(value['r_id'])})
                else:
                    links.append({'source': str(value['id_head']), 'target': str(value['id_tail']),
                                  'value': value['compare_dataset'], 'id': str(value['r_id'])})
            elif value['name']:
                data.append(
                    {'id': str(value['id_tail']), 'name': value['name'], 'category': CATEGORY_INDEX[value['label']]})
                if value['r_name']:
                    links.append(
                        {'source': str(value['id_head']), 'target': str(value['id_tail']), 'value': value['r_name'],
                         'id': str(value['r_id'])})
                else:
                    links.append({'source': str(value['id_head']), 'target': str(value['id_tail']), 'value': value['r'],
                                  'id': str(value['r_id'])})
            else:
                data.append({'id': str(value['id_tail']), 'name': str(round(value['data'], 2)),
                             'category': CATEGORY_INDEX[value['label']]})
                if value['r_name']:
                    links.append(
                        {'source': str(value['id_head']), 'target': str(value['id_tail']), 'value': value['r_name'],
                         'id': str(value['r_id'])})
                else:
                    links.append(
                        {'source': str(value['id_head']), 'target': str(value['id_tail']), 'value': value['r'],
                         'id': str(value['r_id'])})
        return [data, links]

    def nodeReNodeAlias(self, label, alias):
        """
        根据id查询下一级节点与关系
        :param id:
        :return:
        """
        data = []
        links = []
        kgdata = self.g.run(
            f"match p=(n1:{label})-[r]->(n2) where n1.alias='{alias}' or n1.name='{alias}' return n1.name as name1, n1.data as data1, labels(n1)[0] as label1 ,"
            f"type(r) as r, id(r) as r_id, r.name as r_name, r.compare_dataset as compare_dataset, labels(n2)[0] as label, n2.name as name, n2.data as data, id(n1) as id_head, "
            f"id(n2) as id_tail").data()
        if kgdata[0]['name1']:
            data.append({'id': str(kgdata[0]['id_head']), 'name': kgdata[0]['name1'],
                         'category': CATEGORY_INDEX[kgdata[0]['label1']]})
        else:
            data.append({'id': str(kgdata[0]['id_head']), 'name': str(round(kgdata[0]['data1'], 2)),
                         'category': CATEGORY_INDEX[kgdata[0]['label1']]})
        for value in kgdata:
            if value['name'] and not value['data'] is None:
                data.append(
                    {'id': str(value['id_tail']), 'name': str(round(value['data'], 2)), 'des': value['name'],
                     'category': CATEGORY_INDEX[value['label']]})
                if value['r_name']:
                    links.append(
                        {'source': str(value['id_head']), 'target': str(value['id_tail']), 'value': value['r_name'],
                         'id': str(value['r_id'])})
                else:
                    links.append({'source': str(value['id_head']), 'target': str(value['id_tail']),
                                  'value': value['compare_dataset'], 'id': str(value['r_id'])})
            elif value['name']:
                data.append(
                    {'id': str(value['id_tail']), 'name': value['name'], 'category': CATEGORY_INDEX[value['label']]})
                if value['r_name']:
                    links.append(
                        {'source': str(value['id_head']), 'target': str(value['id_tail']), 'value': value['r_name'],
                         'id': str(value['r_id'])})
                else:
                    links.append({'source': str(value['id_head']), 'target': str(value['id_tail']), 'value': value['r'],
                                  'id': str(value['r_id'])})
            else:
                data.append({'id': str(value['id_tail']), 'name': str(round(value['data'], 2)),
                             'category': CATEGORY_INDEX[value['label']]})
                if value['r_name']:
                    links.append(
                        {'source': str(value['id_head']), 'target': str(value['id_tail']), 'value': value['r_name'],
                         'id': str(value['r_id'])})
                else:
                    links.append(
                        {'source': str(value['id_head']), 'target': str(value['id_tail']), 'value': value['r'],
                         'id': str(value['r_id'])})
        return [data, links]

    def runCypher(self, cypher):
        """
        cypher语句执行
        :param cypher:
        :return:
        """
        try:
            self.g.run(cypher)
            return {'msg': 200}
        except:
            return {'msg': 401}

    def addNode(self, label, attribute):
        """
        创建节点，并返回节点信息
        :param label:
        :param attribute:
        :return:
        """
        try:
            kgdata = self.g.run(
                f"create(n1:{label}{{{attribute}}}) return n1.name as name, id(n1) as id, labels(n1)[0] as label").data()
            return {'id': str(kgdata[0]['id']), 'name': kgdata[0]['name'],
                    'category': CATEGORY_INDEX[kgdata[0]['label']], 'msg': 200}
        except:
            return {'msg': 401}

    def setNode(self, id, attribute):
        """
        修改节点属性
        :param id:
        :return:
        """
        try:
            kgdata = self.g.run(
                f"match(n1) where id(n1)={id} set n1+={{{attribute}}} return n1.name as name, id(n1) as id, labels(n1)[0] as label").data()
            return {'id': str(kgdata[0]['id']), 'name': kgdata[0]['name'],
                    'category': CATEGORY_INDEX[kgdata[0]['label']], 'msg': 200}
        except:
            return {'msg': 401}

    def delNode(self, id):
        """
        删除节点
        :param id:
        :return:
        """
        try:
            kgdata = self.g.run(f"match(n1) where id(n1)={id} return n1").data()
            if len(kgdata) > 0:
                self.g.run(f"match(n1) where id(n1)={id} delete n1").data()
                return {'msg': 200}
            else:
                return {'msg': 401}
        except:
            return {'msg': 401}

    def matchNode(self, label, attribute):
        """
        查询节点
        :param label:
        :param attribute:
        :return:
        """
        data = []
        if attribute is None:
            attribute = ''
        try:
            kgdata = self.g.run(
                f"match(n1:{label}{{{attribute}}}) return n1.name as name, n1.data as data, id(n1) as id, labels(n1)[0] as label").data()
            for value in kgdata:
                if value['name'] and not value['data'] is None:
                    data.append(
                        {'id': str(value['id']), 'name': str(round(value['data'], 2)), 'des': value['name'],
                         'category': CATEGORY_INDEX[value['label']]})
                elif value['name']:
                    data.append(
                        {'id': str(value['id']), 'name': value['name'],
                         'category': CATEGORY_INDEX[value['label']]})
                else:
                    data.append({'id': str(value['id']), 'name': str(round(value['data'], 2)),
                                 'category': CATEGORY_INDEX[value['label']]})
            msg = f"成功查询{len(kgdata)}个节点"
            return [data, msg]
        except:
            msg = f"查询失败"
            return [data, msg]

    def addedge(self, hid, tid, rtype, attribute):
        """
        添加关系
        :param hid:
        :param tid:
        :param rtype:
        :param attribute:
        :return:
        """
        try:
            self.g.run(
                f"match(n1),(n2) where id(n1)={hid} and id(n2)={tid} create (n1)-[r:{rtype}{{{attribute}}}]->(n2)").data()
            return {'msg': 200}
        except:
            return {'msg': 401}

    def setEdge(self, id, attribute):
        """
        修改边属性
        :param id:
        :param attribute:
        :return:
        """
        try:
            kgdata = self.g.run(
                f"match(n1)-[r]->(n2) where id(r)={id} set r+={{{attribute}}} return id(n1) as hid").data()
            return {'id': str(kgdata[0]['hid']), 'msg': 200}
        except:
            return {'msg': 401}

    def delEdge(self, id):
        """
        删除边
        :param id:
        :return:
        """
        try:
            kgdata = self.g.run(f"match(n1)-[r]->(n2) where id(r)={id} return r").data()
            if len(kgdata) > 0:
                self.g.run(f"match(n1)-[r]->(n2) where id(r)={id} delete r").data()
                return {'msg': 200}
            else:
                return {'msg': 401}
        except:
            return {'msg': 401}

    def matchEdge(self, rtype, attribute):
        """
        查询边
        :param rtype:
        :param attribute:
        :return:
        """
        data = []
        links = []
        dataSet = set()
        linksSet = set()
        if attribute is None:
            attribute = ''
        try:
            kgdata = self.g.run(
                f"match(n1)-[r:{rtype}{{{attribute}}}]->(n2) return n1.name as name1, n1.data as data1, labels(n1)[0] as label1 ,"
                f"type(r) as r, id(r) as r_id, r.name as r_name, r.compare_dataset as compare_dataset, labels(n2)[0] as label, n2.name as name, n2.data as data, id(n1) as id_head, "
                f"id(n2) as id_tail").data()
            for value in kgdata:
                if value['name1'] and not value['data1'] is None:
                    if not str(value['id_head']) in dataSet:
                        data.append(
                            {'id': str(value['id_head']), 'name': str(round(value['data1'], 2)), 'des': value['name1'],
                             'category': CATEGORY_INDEX[value['label1']]})
                        dataSet.add(str(value['id_head']))
                elif value['name1']:
                    if not str(value['id_head']) in dataSet:
                        data.append(
                            {'id': str(value['id_head']), 'name': value['name1'],
                             'category': CATEGORY_INDEX[value['label1']]})
                        dataSet.add(str(value['id_head']))
                else:
                    if not str(value['id_head']) in dataSet:
                        data.append({'id': str(value['id_head']), 'name': str(round(value['data1'], 2)),
                                     'category': CATEGORY_INDEX[value['label1']]})
                        dataSet.add(str(value['id_head']))

                if value['name'] and not value['data'] is None:
                    if not str(value['id_tail']) in dataSet:
                        data.append(
                            {'id': str(value['id_tail']), 'name': str(round(value['data'], 2)), 'des': value['name'],
                             'category': CATEGORY_INDEX[value['label']]})
                        dataSet.add(str(value['id_tail']))
                    if value['r_name']:
                        if not str(value['r_id']) in linksSet:
                            links.append(
                                {'source': str(value['id_head']), 'target': str(value['id_tail']),
                                 'value': value['r_name'],
                                 'id': str(value['r_id'])})
                            linksSet.add(str(value['r_id']))
                    else:
                        if not str(value['r_id']) in linksSet:
                            links.append({'source': str(value['id_head']), 'target': str(value['id_tail']),
                                          'value': value['compare_dataset'], 'id': str(value['r_id'])})
                            linksSet.add(str(value['r_id']))
                elif value['name']:
                    if not str(value['id_tail']) in dataSet:
                        data.append(
                            {'id': str(value['id_tail']), 'name': value['name'],
                             'category': CATEGORY_INDEX[value['label']]})
                        dataSet.add(str(value['id_tail']))
                    if value['r_name']:
                        if not str(value['r_id']) in linksSet:
                            links.append(
                                {'source': str(value['id_head']), 'target': str(value['id_tail']),
                                 'value': value['r_name'],
                                 'id': str(value['r_id'])})
                            linksSet.add(str(value['r_id']))
                    else:
                        if not str(value['r_id']) in linksSet:
                            links.append(
                                {'source': str(value['id_head']), 'target': str(value['id_tail']), 'value': value['r'],
                                 'id': str(value['r_id'])})
                            linksSet.add(str(value['r_id']))
                else:
                    if not str(value['id_tail']) in dataSet:
                        data.append({'id': str(value['id_tail']), 'name': str(round(value['data'], 2)),
                                     'category': CATEGORY_INDEX[value['label']]})
                        dataSet.add(str(value['id_tail']))
                    if value['r_name']:
                        if not str(value['r_id']) in linksSet:
                            links.append(
                                {'source': str(value['id_head']), 'target': str(value['id_tail']),
                                 'value': value['r_name'],
                                 'id': str(value['r_id'])})
                            linksSet.add(str(value['r_id']))
                    else:
                        if not str(value['r_id']) in linksSet:
                            links.append(
                                {'source': str(value['id_head']), 'target': str(value['id_tail']), 'value': value['r'],
                                 'id': str(value['r_id'])})
                            linksSet.add(str(value['r_id']))
            msg = f"成功查询{len(kgdata)}条关系"
            return [data, links, msg]
        except:
            msg = f"查询失败"
            return [data, links, msg]

    def matchEdgeNode(self, hlabel, hwhereAttribute, tlabel, twhereAttribute, rtype, rwhereAttribute):
        """
        联合查询
        :param hlabel:
        :param hwhereAttribute:
        :param tlabel:
        :param twhereAttribute:
        :param rtype:
        :param rwhereAttribute:
        :return:
        """
        data = []
        links = []
        dataSet = set()
        linksSet = set()
        if hlabel:
            hlabel = ':' + hlabel
        if tlabel:
            tlabel = ':' + tlabel
        if rtype:
            rtype = ':' + rtype
        try:
            kgdata = self.g.run(f"match(n1{hlabel}{{{hwhereAttribute}}})-[r{rtype}{{{rwhereAttribute}}}]->(n2{tlabel}"
                                f"{{{twhereAttribute}}}) return n1.name as name1, n1.data as data1, labels(n1)[0] as label1 ,"
                                f"type(r) as r, id(r) as r_id, r.name as r_name, r.compare_dataset as compare_dataset, "
                                f"labels(n2)[0] as label, n2.name as name, n2.data as data, id(n1) as id_head, id(n2) as id_tail").data()
            for value in kgdata:
                if value['name1'] and not value['data1'] is None:
                    if not str(value['id_head']) in dataSet:
                        data.append(
                            {'id': str(value['id_head']), 'name': str(round(value['data1'], 2)), 'des': value['name1'],
                             'category': CATEGORY_INDEX[value['label1']]})
                        dataSet.add(str(value['id_head']))
                elif value['name1']:
                    if not str(value['id_head']) in dataSet:
                        data.append(
                            {'id': str(value['id_head']), 'name': value['name1'],
                             'category': CATEGORY_INDEX[value['label1']]})
                        dataSet.add(str(value['id_head']))
                else:
                    if not str(value['id_head']) in dataSet:
                        data.append({'id': str(value['id_head']), 'name': str(round(value['data1'], 2)),
                                     'category': CATEGORY_INDEX[value['label1']]})
                        dataSet.add(str(value['id_head']))

                if value['name'] and not value['data'] is None:
                    if not str(value['id_tail']) in dataSet:
                        data.append(
                            {'id': str(value['id_tail']), 'name': str(round(value['data'], 2)), 'des': value['name'],
                             'category': CATEGORY_INDEX[value['label']]})
                        dataSet.add(str(value['id_tail']))
                    if value['r_name']:
                        if not str(value['r_id']) in linksSet:
                            links.append(
                                {'source': str(value['id_head']), 'target': str(value['id_tail']),
                                 'value': value['r_name'],
                                 'id': str(value['r_id'])})
                            linksSet.add(str(value['r_id']))
                    else:
                        if not str(value['r_id']) in linksSet:
                            links.append({'source': str(value['id_head']), 'target': str(value['id_tail']),
                                          'value': value['compare_dataset'], 'id': str(value['r_id'])})
                            linksSet.add(str(value['r_id']))
                elif value['name']:
                    if not str(value['id_tail']) in dataSet:
                        data.append(
                            {'id': str(value['id_tail']), 'name': value['name'],
                             'category': CATEGORY_INDEX[value['label']]})
                        dataSet.add(str(value['id_tail']))
                    if value['r_name']:
                        if not str(value['r_id']) in linksSet:
                            links.append(
                                {'source': str(value['id_head']), 'target': str(value['id_tail']),
                                 'value': value['r_name'],
                                 'id': str(value['r_id'])})
                            linksSet.add(str(value['r_id']))
                    else:
                        if not str(value['r_id']) in linksSet:
                            links.append(
                                {'source': str(value['id_head']), 'target': str(value['id_tail']), 'value': value['r'],
                                 'id': str(value['r_id'])})
                            linksSet.add(str(value['r_id']))
                else:
                    if not str(value['id_tail']) in dataSet:
                        data.append({'id': str(value['id_tail']), 'name': str(round(value['data'], 2)),
                                     'category': CATEGORY_INDEX[value['label']]})
                        dataSet.add(str(value['id_tail']))
                    if value['r_name']:
                        if not str(value['r_id']) in linksSet:
                            links.append(
                                {'source': str(value['id_head']), 'target': str(value['id_tail']),
                                 'value': value['r_name'],
                                 'id': str(value['r_id'])})
                            linksSet.add(str(value['r_id']))
                    else:
                        if not str(value['r_id']) in linksSet:
                            links.append(
                                {'source': str(value['id_head']), 'target': str(value['id_tail']), 'value': value['r'],
                                 'id': str(value['r_id'])})
                            linksSet.add(str(value['r_id']))
            msg = f"成功查询{len(kgdata)}条数据"
            return [data, links, msg]
        except:
            msg = f"查询失败"
            return [data, links, msg]

    def load_xlsx(self, city, data):
        res = []
        for item in data:
            kgdata = self.g.run(
                f"match(:city{{name:'{city}'}})-[]->(n1:{item['head_node_label']}{{{item['head_node_attritute']}}})"
                f" create(n1)-[:{item['r_type']}{{{item['r_attritube']}}}]->(:{item['tail_node_label']}{{{item['tail_node_attribute']}}})"
                f" return n1.name as name, id(n1) as id, labels(n1)[0] as label").data()
            res.append(
                {'id': str(kgdata[0]['id']), 'name': kgdata[0]['name'], 'category': CATEGORY_INDEX[kgdata[0]['label']]})
        return res

    def load_shp(self, data):
        res = []
        kgdata = self.g.run(
            f"create(n1:country{{name:'Germany'}}) return n1.name as name, id(n1) as id, labels(n1)[0] as label").data()
        res.append(
            {'id': str(kgdata[0]['id']), 'name': kgdata[0]['name'], 'category': CATEGORY_INDEX[kgdata[0]['label']]})
        for item in data:
            self.g.run(f"match(n1:country{{name:'Germany'}})"
                       f" create(n1)-[:{item['ENGTYPE_1']}]->(:{item['ENGTYPE_1']}{{name:'{item['NAME_1']}'}})")
        return res

    def getLocationName(self, nodeId):
        """
        判断node是否为地名，并返回
        :param nodeId:
        :return:
        """
        try:
            kgdata = self.g.run(
                f"match (n1) where id(n1)={nodeId} return n1.name as name, labels(n1)[0] as label").data()[0]
            if kgdata['label'] in {'country', 'province', 'city', 'district', 'street', 'region'}:
                return kgdata['name']
            else:
                return 0
        except:
            return 0

    def getProductAttribute(self, productSN):
        """
        根据产品的productSN号，获取产品属性知识图谱
        :param productSN:
        :return:
        """
        data = []
        links = []
        kgdata = self.g_product.run(f"match(n1:product{{productSN:'{productSN}'}})-[r:attribute]->(n2)"
                                    f"return id(n1) as id_head, n1.title as title, labels(n1)[0] as label1,"
                                    f"id(n2) as id_tail, labels(n2)[0] as label2, n2.value as value,"
                                    f"id(r) as r_id").data()
        for item in kgdata:
            data.append(
                {'id': str(item['id_head']), 'name': item['title'], 'category': PRODUCT_CATEGORY_INDEX[item['label1']]})
            data.append(
                {'id': str(item['id_tail']), 'name': item['value'], 'category': PRODUCT_CATEGORY_INDEX[item['label2']]})
            links.append({'source': str(item['id_head']), 'target': str(item['id_tail']),
                          'value': PRODUCT_CHINESE_NAME[item['label2']], 'id': str(item['r_id'])})
        return [data, links]

    def getProductRecommendation(self, productSN):
        """
        数据推荐接口
        :param productSN:
        :return:
        """
        data = []
        links = []
        kgdata = self.g_product.run(
            f"match(n1:product{{productSN:'{productSN}'}})-[:attribute]->(att)<-[:attribute]-(n2:product)"
            f" return id(n1) as id_head, n1.title as title1, labels(n1)[0] as label1, n1.productSN as sn1, "
            f"id(n2) as id_tail, n2.title as title2, labels(n2)[0] as label2, n2.productSN as sn2, "
            f"count(n2) as c_n2 ORDER BY c_n2 desc limit 20").data()
        data.append(
            {'id': str(kgdata[0]['id_head']), 'name': kgdata[0]['title1'],
             'category': PRODUCT_CATEGORY_INDEX[kgdata[0]['label1']], 'sn': kgdata[0]['sn1']})
        for item in kgdata:
            # data.append(
            #     {'id': str(item['id_tail']), 'name': item['title2'],
            #      'category': PRODUCT_CATEGORY_INDEX[item['label2']]})
            data.append(
                {'id': str(item['id_tail']), 'name': item['title2'],
                 'category': 1, 'sn': item['sn2']})
            links.append({'source': str(item['id_head']), 'target': str(item['id_tail']), 'value': str(item['c_n2'])})
        return [data, links]

    def getProductKgClickData(self, nodeId):
        """
        推荐页产品知识图谱点击数据获取
        :param nodeId:
        :return:
        """
        data = []
        links = []
        kgdata = self.g_product.run(f"match(n1)-[r:attribute]->(n2) where id(n1)={nodeId}"
                                    f"return id(n1) as id_head, n1.title as title, labels(n1)[0] as label1,"
                                    f"id(n2) as id_tail, labels(n2)[0] as label2, n2.value as value,"
                                    f"id(r) as r_id").data()
        if len(kgdata) == 0:
            kgdata = self.g_product.run(f"match(n1)-[r:attribute]->(n2) where id(n2)={nodeId}"
                                        f"return id(n1) as id_head, n1.title as title, labels(n1)[0] as label1,"
                                        f"id(n2) as id_tail, labels(n2)[0] as label2, n2.value as value,"
                                        f"id(r) as r_id").data()
        for item in kgdata:
            data.append(
                {'id': str(item['id_head']), 'name': item['title'], 'category': PRODUCT_CATEGORY_INDEX[item['label1']]})
            data.append(
                {'id': str(item['id_tail']), 'name': item['value'], 'category': PRODUCT_CATEGORY_INDEX[item['label2']]})
            links.append({'source': str(item['id_head']), 'target': str(item['id_tail']),
                          'value': PRODUCT_CHINESE_NAME[item['label2']], 'id': str(item['r_id'])})
        return [data, links]


if __name__ == "__main__":
    kgdb = Kgdb(username="neo4j", password="201314", port="11005")
    data1 = kgdb.nodeRelationshipNode('country', '中华人民共和国-country')
    print('end')
