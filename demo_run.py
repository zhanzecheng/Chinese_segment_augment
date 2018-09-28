# -*- coding: utf-8 -*-
"""
# @Time    : 2018/05/26 下午5:13
# @Update  : 2018/09/28 上午10:30
# @Author  : zhanzecheng/片刻
# @File    : demo.py.py
# @Software: PyCharm
"""
import os
import jieba
# 自定义
from model import TrieNode
from utils import getStopwords, loadWords, generate_ngram, saveModel, loadModel


def loadDate(fileName, stopwords):
    # 加载数据集
    data = []
    with open(fileName, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            line = [x for x in jieba.cut(line, cut_all=False) if x not in stopwords]
            data.append(line)

    # 按照行进行切分句子，得到一个数组
    # [[行，切词], [], []]
    # print(data)
    return data


def loadDate2Root(data):
    print('------> 插入节点')
    for i in data:
        # tmp 表示每一行自由组合后的结果（n gram）
        # tmp: [['它'], ['是'], ['小'], ['狗'], ['它', '是'], ['是', '小'], ['小', '狗'], ['它', '是', '小'], ['是', '小', '狗']]
        tmp = generate_ngram(i, 3)
        # print(tmp)
        for d in tmp:
            root.add(d)
    print('------> 插入成功')


if __name__ == "__main__":
    # 加载停用词
    stopwords = getStopwords()

    rootName = ("data/root.pkl")
    if os.path.exists(rootName):
        root = loadModel(rootName)
    else:
        dictName = 'data/dict.txt'
        word_freq = loadWords(dictName)
        root = TrieNode('*', word_freq)
        saveModel(root, rootName)

    # 加载新的文章
    fileName = 'data/demo.txt'
    data = loadDate(fileName, stopwords)
    # 将新的文章插入到Root中
    loadDate2Root(data)

    # 定义取TOP5个
    N = 5
    result, add_word = root.wordFind(N)
    # 如果想要调试和选择其他的阈值，可以print result来调整
    # print("\n----\n", result)
    print("\n----\n", '增加了 %d 个新词, 词语和得分分别为: \n' % len(add_word))
    print('#############################')
    for word, score in add_word.items():
        print(word + ' ---->  ', score)
    print('#############################')

    # 前后效果对比
    test = '蔡英文在昨天应民进党当局的邀请，准备和陈时中一道前往世界卫生大会，和谈有关九二共识问题'
    print('添加前：')
    print("".join([(x + '/ ') for x in jieba.cut(test, cut_all=False) if x not in stopwords]))

    for word, score in add_word.items():
        jieba.add_word(word)
    print("添加后：")
    print("".join([(x + '/ ') for x in jieba.cut(test, cut_all=False) if x not in stopwords]))
