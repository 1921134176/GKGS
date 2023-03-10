#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: ChengXin
@contact:1921134176@qq.com
@version: 1.0.0
@license: Apache Licence
@file: question_parser.py
@time: 2023/3/9 11:59
"""


class QuestionPaser:

    def build_entitydict(self, args):
        '''
        构建实体节点
        :param args:
        :return:
        '''
        entity_dict = {}
        for arg, types in args.items():
            for type in types:
                if type not in entity_dict:
                    entity_dict[type] = [arg]
                else:
                    entity_dict[type].append(arg)

        return entity_dict

    def parser_main(self, res_classify):
        '''
        解析主函数
        :param res_classify:
        :return:
        '''
        args = res_classify['args']
        entity_dict = self.build_entitydict(args)
        question_types = res_classify['question_types']
        sqls = []
        for question_type in question_types:
            sql_ = {}
            sql_['question_type'] = question_type
            sql = []
            if question_type == 'sub_distrist':
                sql = self.sql_transfer(question_type, entity_dict.get(list(entity_dict.keys())[0]))

            elif question_type == 'distrist_isWhoSub':
                sql = self.sql_transfer(question_type, entity_dict.get(list(entity_dict.keys())[0]))

            elif question_type == 'entity_dsc':
                sql = self.sql_transfer(question_type, entity_dict.get(list(entity_dict.keys())[0]))

            if sql:
                sql_['sql'] = sql

                sqls.append(sql_)

        return sqls

    def sql_transfer(self, question_type, entities):
        '''
        针对不同的问题，分开进行处理
        :param question_type:
        :param entities:
        :return:
        '''
        if not entities:
            return []

        # 查询语句
        sql = []
        # 下级行政区划有哪些
        if question_type == 'sub_distrist':
            sql = ["MATCH (m)-[r]->(n) where m.name = '{0}' and type(r) in ['province','city','district','street'] return m.name, n.name".format(i) for i in entities]

        # 上级行政区划
        elif question_type == 'distrist_isWhoSub':
            sql = ["MATCH (m)-[r]->(n) where n.name = '{0}' and type(r) in ['province','city','district','street'] return m.name, n.name".format(i) for i in entities]

        # 实体描述
        elif question_type == 'entity_dsc':
            sql = ["MATCH (m) where m.name = '{0}' return m.name".format(i) for i in entities]

        else:
            sql = []

        return sql
