

# 中文分词新词发现
python3利用互信息和左右信息熵的中文分词新词发现

简介
========
* 使用[jieba分词](https://github.com/fxsjy/jieba)为基本分词组件
* 针对用户给出的文本，利用信息熵进行新词发现
* 使用[字典树](https://github.com/zhanzecheng/The-Art-Of-Programming-By-July/blob/master/ebook/zh/06.09.md)存储单词和统计词频
* 由于但文本不能正确反映单个词的词频，这里使用[jieba](https://github.com/fxsjy/jieba)自带的词频表作为外部数据源
* 取 TOP N 个作为新词


使用配置
========
    git clone https://github.com/zhanzecheng/Chinese_segment_augment.git
    pip3 install jieba
    
    
使用方式
========
    from model import TrieNode

# 得到 TOP5 得分的新词
    # result里面存储的是所有新词和其得分，add_word里面是top5
    result, add_word = root.wordFind(5)

> 运行： python demo_run.py  体验程序的快感

具体细节请参考demo_run.py

效果说明
========
初始语句：

    蔡英文在昨天应民进党当局的邀请，准备和陈时中一道前往世界卫生大会，和谈有关九二共识问题
添加前：
    
    蔡/ 英文/ 在/ 昨天/ 应/ 民进党/ 当局/ 邀请/ 准备/ 和/ 陈时/ 中/ 一道/ 前往/ 世界卫生/ 大会/ 和谈/ 有关/ 九二/ 共识/ 问题/ 
添加后：

    蔡英文/ 在/ 昨天/ 应/ 民进党当局/ 邀请/ 准备/ 和/ 陈时中/ 一道/ 前往/ 世界卫生大会/ 和谈/ 有关/ 九二共识/ 问题/
    
新词结果和得分：

    世界卫生大会 ---->   0.4380419441616299
    蔡英文      ---->   0.28882968751888893
    民进党当局   ---->   0.2247420989996931
    陈时中      ---->   0.15996145099751344
    九二共识    ---->   0.14723726297223602
    
测试样本：

    台湾“中时电子报”26日报道称，蔡英文今日一早会见“世卫行动团”，她称，台湾虽然无法参加WHA(世界卫生大会)，但“还是要有贡献”。于是，她表示要捐100万美元给WHO对抗埃博拉病毒
    对于台湾为何不能，蔡英文又一次惯性“甩锅”，宣称“中国对台湾的外交打压已无所不用其极”。
    ......
在 demo.txt中

方法解释
========
* 先使用jieba分词对demo.txt做粗略分词
* 使用 3 gram 的方式来构建节点，并使用词典树对存储分词，如

        [4G, 网络， 上网卡] --> [4G, 网络， 上网卡, 4G网络, 网络上网卡, 4G网络上网卡]
* 利用trie树计算互信息 PMI
* 利用trie树计算左右熵
* 得出得分 score = PMI + min(左熵， 右熵)
* 以得分高低进行排序，取出前5个，若前面的待选词在属于后面待选词一部分，则删除后面待选词，如

        [花呗， 蚂蚁花呗] --> [花呗]

具体原理说明请看这个[链接](https://www.jianshu.com/p/e9313fd692ef)

感谢
========
10/21/2018 感谢[caomaocao](https://github.com/caomaocao) 对代码遵守pep8规范、增加pipenv依赖管理和工程化的贡献

09/29/2018 感谢[jiangzhonglian](https://github.com/jiangzhonglian) 对代码进行的精简和注释补充
