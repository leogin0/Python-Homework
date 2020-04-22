#编写一个函数, 传入一个数字列表, 输出列表中的奇数;数字列表请用随机数函数生成;
import random

def odd(list1):
    print('列表中奇数有：'[i for i in list1 if i % 2 != 0])

l = [random.randint(1,10) for x in range(10)]
odd(l)