#练习1
#利用闭包返回一个计数器函数，每次调用它返回递增整数：
# -*- coding: utf-8 -*-

# # 测试:
# s=0
# def createCounter():
#     def counter():
#         global s #引用全局变量
#         s = s+1
#         return s
#     return counter
# counterA = createCounter()
# print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
# counterB = createCounter()
# if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
#     print('测试通过!')
# else:
#     print('测试失败!')

#练习:  定义一个函数, 做2个数的加法;  然后我们定义一个装饰器, 对原函数记录运行日志;

def log(func):
    def wrapper(*args, **kw):
        print('加法被执行了')
        return func(*args, **kw)
    return wrapper

@log
def add():
     print(1+2)

add()