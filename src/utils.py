# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/26 下午5:20
# @Author  : zhanzecheng
# @File    : utils.py
# @Software: PyCharm
"""

def generate_ngram(data, n):
    """
    参数ngram特征
    :param data:
    :param n:
    :return:
    """
    result = []
    for i in range(1, n+1):
        if len(data) -i + 1< 1:
            break
        for j in range(len(data) - i + 1):
            result.append(data[j:j+i])

    return result

# 加载停用词
stopword = set()
with open('../data/stopword.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        stopword.add(line.strip())

# 加载外部词频记录
word_freq = {}
print('-----> 加载外部词频')
with open('../data/dict.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.split(' ')
        # 规定最少词频
        if int(line[1]) > 2:
            word_freq[line[0]] = line[1]
