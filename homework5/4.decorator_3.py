# 编写装饰器来实现，对目标函数进行装饰，分3种情况：目标函数无参数无返回值，目标函数有参数，目标函数有返回值；
#      三个目标函数分别为：
#      A 打印输出20000之内的素数；
#      B 计算整数2-10000之间的素数的个数；
#      C 计算整数2-M之间的素数的个数；


def deco(func):
    def inner(*args, **kwargs):
        print('decorator %s'%func.__name__)
        func(*args, **kwargs)
        res=func(*args,**kwargs)    
        print(res)
    return inner

#无参数无返回值
@deco
def func1():
    for i in range(1,20000):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            print(i)

#有返回值
@deco
def func2():
    count = 0
    for i in range(2,10000):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            count += 1
    return(count)

#有参数
@deco
def func3(m):
    count = 0
    for i in range(2,m):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            count += 1
    return count

func1()
func2()
func3(1000)
            
    
