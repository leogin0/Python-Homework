# 多进程练习：
# 计算1～100000之间所有素数的个数， 要求如下:
# - 编写函数判断一个数字是否为素数，然后统计素数的个数；
# -对比1: 对比使用多进程和不使用多进程两种方法的统计速度。
# -对比2：对比开启4个多进程和开启10个多进程两种方法的速度。
from multiprocessing import Process
import time


def sushu(no):
    if no == 1:
        return 'false'
    for i in range(2, int(no**0.5+1)):
        if no % i == 0:
            break
    else:
        return 'true'

class Myprocess(Process):
    def __init__(self, a, b, count1):
        Process.__init__(self)
        self.a = a
        self.b = b
        self.count1 = count1

    def run(self):
        for i in range(self.a, self.b):
            if sushu(i) == 'true':
                self.count1 += 1

def no_use():
    start1 = time.time()
    count = 0
    for i in range(1, 100001):
        if sushu(i) == 'true':
            count += 1
    print('素数个数为%d'%count)
    end1 = time.time()
    print('不用多进程所用时间：%s'%(end1 - start1))

def use():
    # count = 0
    start = time.time()
    processes = []
    for x in range(1, 100001, 50000):
        p = Myprocess(x, x+50000, 0)
        p.start()
        # print(p.get_result())
        # count += p.get_result()
        processes.append(p)
    [process.join() for process in processes]
    # print('素数个数为%d'%count)
    end = time.time()
    print('多进程所用时间：%s' % (end - start))


def use4():
    start = time.time()
    processes = []
    for i in range(1,100001,25000):
        f = Myprocess(i, i+25000, 0)
        f.start()
        processes.append(f)
    [process.join() for process in processes]
    end = time.time()
    print('4个多进程所用时间：%s' % (end - start))


def use10():
    start = time.time()
    processes = []
    for i in range(1, 100001, 100000):
        f = Myprocess(i, i + 10000, 0)
        f.start()
        processes.append(f)
    [process.join() for process in processes]
    end = time.time()
    print('10个多进程所用时间：%s' % (end - start))


if __name__ == '__main__':
    use()
    no_use()
    use4()
    use10()





