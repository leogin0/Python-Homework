# 多进程通讯：
#   编写一个简单的聊天程序；其中一个进程发送文字聊天消息（从键盘输入文字消息）；  另外一个进程接收并打印消息；

from multiprocessing import Process, Queue
import os, time, random


# 写数据进程执行的代码:
def write(q, str):
    # print('Process to write: %s' % os.getpid())
    # print('Put %s to queue...' % str)
    q.put(str)
    time.sleep(random.random())


# 读数据进程执行的代码:
def read(q, name):
    # print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('%s说的话：%s' % (name, value))


if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()

    pr = Process(target=read, args=(q,'B'))
    # 启动子进程pr，读取:
    pr.start()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()
    # 启动子进程pw，写入:
    str = input('A:')
    pw = Process(target=write, args=(q,str))
    pw.start()
    # 等待pw结束:
    pw.join()
    print(q.qsize())

    pr2 = Process(target=read, args=(q,'A'))
    # 启动子进程pr，读取:
    pr2.start()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr2.terminate()
    # 启动子进程pw，写入:
    str2 = input('B：')
    pw2 = Process(target=write, args=(q, str))
    pw2.start()
    # 等待pw结束:
    pw2.join()
    