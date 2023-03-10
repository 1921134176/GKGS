#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: ChengXin
@contact:1921134176@qq.com
@version: 1.0.0
@license: Apache Licence
@file: question_classifier.py
@time: 2023/3/9 11:58
"""

import os
import ahocorasick
import json


class QuestionClassifier:
    def __init__(self):
        print('正在加载问答模型 ......')
        cur_dir = '\\'.join(os.path.abspath(__file__).split('\\')[:-1])
        # 　特征词路径
        self.country_path = os.path.join(cur_dir, 'dict\\country.txt')
        self.province_path = os.path.join(cur_dir, 'dict\\province.txt')
        self.city_path = os.path.join(cur_dir, 'dict\\city.txt')
        self.district_path = os.path.join(cur_dir, 'dict\\district.txt')
        self.street_path = os.path.join(cur_dir, 'dict\\street.txt')
        self.ambiguityDict_path = os.path.join(cur_dir, 'dict\\ambiguityDict.txt')
        # 加载特征词
        self.country_wds = [i.strip() for i in open(self.country_path, encoding='utf-8') if i.strip()]
        self.province_wds = [i.strip() for i in open(self.province_path, encoding='utf-8') if i.strip()]
        self.city_wds = [i.strip() for i in open(self.city_path, encoding='utf-8') if i.strip()]
        self.district_wds = [i.strip() for i in open(self.district_path, encoding='utf-8') if i.strip()]
        self.street_wds = [i.strip() for i in open(self.street_path, encoding='utf-8') if i.strip()]
        self.region_words = set(
            self.country_wds + self.province_wds + self.city_wds + self.district_wds + self.street_wds)
        self.ambiguityDict_words = json.loads([i.strip() for i in open(self.ambiguityDict_path, encoding='utf-8') if i.strip()][0])
        # 构造领域actree
        self.region_tree = self.build_actree(list(self.region_words))
        # 构建词典
        self.wdtype_dict = self.build_wdtype_dict()
        # 问句疑问词
        self.baohan_qwds = ['包含', '下级']
        self.shuyu_qwds = ['属于', '上级']
        self.weather_qwds = ['天气', '气候']

        print('model init finished ......')

    def classify(self, question):
        '''
        分类主函数
        :param question:
        :return:
        '''
        data = {}
        medical_dict = self.check_medical(question)
        if not medical_dict:
            return {}
        data['args'] = medical_dict
        # 收集问句当中所涉及到的实体类型
        types = []
        for type_ in medical_dict.values():
            types += type_

        question_types = []

        # 下级行政区划有哪些
        if self.check_words(self.baohan_qwds, question):
            question_type = 'sub_distrist'
            question_types.append(question_type)

        # 上级行政区是谁
        if self.check_words(self.shuyu_qwds, question):
            question_type = 'distrist_isWhoSub'
            question_types.append(question_type)

        # 地方天气
        if self.check_words(self.weather_qwds, question):
            question_type = 'location_weather'
            question_types.append(question_type)

        # 若没有查到相关的外部查询信息，那么则返回描述信息
        if len(question_types) == 0:
            question_types = ['entity_dsc']

        # 将多个分类结果进行合并处理，组装成一个字典
        data['question_types'] = question_types

        return data

    def build_wdtype_dict(self):
        '''
        构造词对应的类型
        :return:
        '''
        wd_dict = dict()
        for wd in self.region_words:
            wd_dict[wd] = []
            if wd in self.country_wds:
                wd_dict[wd].append('country')
            if wd in self.province_wds:
                wd_dict[wd].append('province')
            if wd in self.city_wds:
                wd_dict[wd].append('city')
            if wd in self.district_wds:
                wd_dict[wd].append('district')
            if wd in self.street_wds:
                wd_dict[wd].append('street')
        return wd_dict

    def build_actree(self, wordlist):
        '''
        构造actree，加速过滤
        :param wordlist:
        :return:
        '''
        actree = ahocorasick.Automaton()
        for index, word in enumerate(wordlist):
            actree.add_word(word, (index, word))
        actree.make_automaton()
        return actree

    def check_medical(self, question):
        '''
        问句过滤
        :param question:
        :return:
        '''
        region_wds = []
        for i in self.region_tree.iter(question):
            wd = i[1][1]
            if wd in self.ambiguityDict_words:
                wd = self.ambiguityDict_words[wd]
            region_wds.append(wd)
        stop_wds = []
        # 解决嵌套命名实体识别
        for wd1 in region_wds:
            for wd2 in region_wds:
                if wd1 in wd2 and wd1 != wd2:
                    stop_wds.append(wd1)
        final_wds = [i for i in region_wds if i not in stop_wds]
        final_dict = {i: self.wdtype_dict.get(i) for i in final_wds}

        return final_dict

    def check_words(self, wds, sent):
        '''
        基于特征词进行分类
        :param wds:
        :param sent:
        :return:
        '''
        for wd in wds:
            if wd in sent:
                return True
        return False
