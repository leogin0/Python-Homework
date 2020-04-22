#对一篇中文文献, ;利用jieba库,进行词频统计分析找出文章的关键词(取词频最高的前10个词语,作为文章的关键字);

import jieba
try:
    txt = open("homework3/文章.txt", "r", encoding='utf-8').read()
except IOError:
    print('Error:没有找到文件或文件读取失败')

words = jieba.lcut(txt)
d = {} 

for i in words:
    if  len(i) == 1:    # 单个词语不计算在内
        continue
    else:
        d[i] = d.get(i,0) + 1

sort_d = sorted(d.items(),key = lambda x: x[1],reverse=True)

for i in range(10):
    print(sort_d[i])