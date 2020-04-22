#使用random模块，生成随机数，来初始化一个列表，元组；
#使用 random 模块的 randint() 函数来生成随机数，查询一下相关函数的用法；
    #random.uniform(a, b)，用于生成一个指定范围内的随机符点数
    #random.randint(a, b)，用于生成一个指定范围内的整数
    #random.choice(sequence)从序列中获取一个随机元素

import random

plist = [random.randint(1,10) for x in range(10)]
# plist = [random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10)]
ptuple = (random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10))
print(plist,ptuple)