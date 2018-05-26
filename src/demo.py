# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/26 下午5:13
# @Author  : zhanzecheng
# @File    : demo.py.py
# @Software: PyCharm
"""

from model import TrieNode
from utils import stopword, word_freq, generate_ngram
import jieba


# 定义取TOP5个
N = 5

# 加载数据集
data = []
with open('../data/demo.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        line = [x for x in jieba.cut(line, cut_all=False) if x not in stopword]
        data.append(line)




print('------> 初始化字典树')
root = TrieNode('*', word_freq)

print('------> 插入节点')
for i in data:
    tmp = generate_ngram(i, 3)
    for d in tmp:
        root.add(d)

result, add_word = root.wordFind(5)

print('增加了%d个新词, 词语和得分分别为' % len(add_word))
print('#############################')
for word, score in add_word.items():
    print(word + ' ---->  ', score)
print('#############################')

# 如果想要调试和选择其他的阈值，可以print result来调整
# print(result)

test = '蔡英文在昨天应民进党当局的邀请，准备和陈时中一道前往世界卫生大会，和谈有关九二共识问题'
print('添加前：')
print("".join([(x + '/ ') for x in jieba.cut(test, cut_all=False) if x not in stopword]))

for word, score in add_word.items():
    jieba.add_word(word)
print("添加后：")
print("".join([(x + '/ ') for x in jieba.cut(test, cut_all=False) if x not in stopword]))






