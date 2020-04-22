#京东二面笔试题
#1） 生成一个大文件ip.txt,要求1200行，每行随机为172.25.254.1---172.25.254.254之间的一个ip地址;
# 2） 读取ip.txt文件统计这个文件中ip出现频率排前10的ip

import random

with open('ip.txt','w') as f1:
    for i in range(1200):
        f1.write('172.25.254.' + str(random.randint(0,255)) + '\n')

d = {}
with open('ip.txt','r') as f2:
    for i in f2.read().splitlines():
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

l1 = list(d.items())
sorted_l1 = sorted(l1, key=lambda x: x[1], reverse=True)
print(sorted_l1[0:10])


