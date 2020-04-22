#定义一个10个元素的列表，通过列表自带的函数，实现元素在尾部插入和头部插入并记录程序运行的时间；
#用deque来实现，同样记录程序所耗费的时间；输出这2个时间的差值；
#提示：列表原生的函数实现头部插入数据：list.insert(0, v)；list.append（2）)
from collections import deque
import time

def time1():
    start = time.clock()
    l1 = [1,2,3,4,5,6,7,8,9,10]
    l1.insert(0,0)
    l1.insert(len(l1),11)
    end = time.clock()
    print('自带函数运行时间:',end - start)
    return (end - start)

def time2():
    start = time.clock()
    l1 = deque([1,2,3,4,5,6,7,8,9,10])
    l1.append(0)
    l1.appendleft(11)
    end = time.clock()
    print('使用deque运行时间:',end - start)
    return (end - start)

print('时间差值：',(time1()-time2()))
