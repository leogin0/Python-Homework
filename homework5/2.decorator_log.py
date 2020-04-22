#编写一个装饰器，能记录其他函数调用的日志，将日志写入到文件中；

def outer(func):
    def inner(a,b):
        print('调用函数%s()'% func.__name__)
        func(a,b)
    return inner

@outer
def add(a,b):
    print(a + b)

add(1,2)