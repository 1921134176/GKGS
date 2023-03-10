#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: ChengXin
@contact:1921134176@qq.com
@version: 1.0.0
@license: Apache Licence
@file: chatbot.py
@time: 2023/3/9 11:55
"""

from qa_system_on_kg.question_classifier import *
from qa_system_on_kg.question_parser import *
from qa_system_on_kg.answer_search import *

'''问答类'''


class ChatBotGraph:
    def __init__(self, host, username, password):
        self.classifier = QuestionClassifier()
        self.parser = QuestionPaser()
        self.searcher = AnswerSearcher(host, username, password)

    def chat_main(self, sent):
        answer = ''
        res_classify = self.classifier.classify(sent)
        if not res_classify:
            return [{}, answer]
        res_sql = self.parser.parser_main(res_classify)
        final_answers = self.searcher.search_main(res_sql)
        if not final_answers:
            return [res_classify['args'], answer]
        else:
            return [res_classify['args'], '\n'.join(final_answers)]


if __name__ == '__main__':
    handler = ChatBotGraph("http://localhost:11005", 'neo4j', '201314')
    while 1:
        question = input('用户:')
        answer = handler.chat_main(question)
        print('小勇:', answer)
