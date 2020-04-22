#编写一个装饰器，能计算其他函数的运行时间；

import time

def outer(func):
    def inner():
        start = time.time()
        func()
        end = time.time()
        print('运行时间为%s'%(end - start))
    return inner

@outer
def add():
    print(1 + 5)

add()
