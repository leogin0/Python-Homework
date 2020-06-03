# 有100个同学的分数：数据请用随机函数生成；
#      A  利用多线程程序（比如，5个线程，每个线程负责输出20条记录），快速输出这100个同学的信息；
#      B 利用线程池来实现；
import random
import threading

# #多线程
student = [random.randint(0, 100) for x in range(100)]
print(student)
#
# count = 0
#
#
# class MyThread(threading.Thread):
#
#     def run(self):
#         global count
#         for i in range(20):
#             print('%s is working: %d' % (self.name, student[count]))
#             count += 1
#
#
# def print_score():
#     for i in range(5):
#         t = MyThread()
#         t.start()
#         t.join()
#
#
# if __name__ == '__main__':
#     print_score()

#线程池
import threadpool

def pool_num(num, p_methond, num_list):
    pool = threadpool.ThreadPool(num) #声明线程池个数
    reqs = threadpool.makeRequests(p_methond, num_list) #生成线程池启动参数
    [pool.putRequest(req) for req in reqs] #循环执行启动线程
    pool.wait() #等待子线程

def p_methond(num):
    print(str(num) + ' ')

pool_num(3, p_methond, student)