#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: ChengXin
@contact:1921134176@qq.com
@version: 1.0.0
@license: Apache Licence
@file: answer_search.py
@time: 2023/3/9 12:01
"""

from py2neo import Graph
import requests


class AnswerSearcher:
    def __init__(self, host, username, password):
        self.g = Graph(host, auth=(username, password))

    '''执行cypher查询，并返回相应结果'''

    def search_main(self, sqls):
        final_answers = []
        for sql_ in sqls:
            question_type = sql_['question_type']
            queries = sql_['sql']
            answers = []
            for query in queries:
                ress = self.g.run(query).data()
                answers += ress
            final_answer = self.answer_prettify(question_type, answers)
            if final_answer:
                final_answers.append(final_answer)
        return final_answers

    '''根据对应的qustion_type，调用相应的回复模板'''

    def answer_prettify(self, question_type, answers):
        final_answer = []
        if not answers:
            return ''
        if question_type == 'sub_distrist':
            desc = [i['n.name'] for i in answers]
            subject = answers[0]['m.name']
            final_answer = '{0}下级行政区划包括：{1}'.format(subject, '；'.join(list(set(desc))))

        elif question_type == 'distrist_isWhoSub':
            desc = [i['m.name'] for i in answers]
            subject = answers[0]['n.name']
            final_answer = '{0}属于：{1}'.format(subject, '；'.join(list(set(desc))))

        elif question_type == 'entity_dsc':
            subject = answers[0]['m.name']
            url1 = f"https://dmfw.mca.gov.cn/9095/stname/listPub?stName={subject}&searchType=精确"
            data1 = requests.request("POST", url1, verify=False)
            data1 = data1.json()
            locationId = data1['records'][0]['id']
            url2 = f"https://dmfw.mca.gov.cn/9095/stname/detailsPub?id={locationId}"
            data2 = requests.request("POST", url2, verify=False)
            data2 = data2.json()
            final_answer = data2['place_history']

        else:
            # location_weather类型希望直接用思知机器人
            final_answer = []

        return final_answer
