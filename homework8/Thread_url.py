# 给定一组数据网址数据，请判断这些网址是否可以访问； 用多线程的方式来实现；
#    请查资料，Python的 requests库，如何判断一个网址可以访问；
import threading
import requests


def getHtmlText(url):
    try:        # 网络连接有风险，异常处理很重要
        r = requests.get(url, timeout=30)    # 查一下这个方法的使用
        r.raise_for_status()       # 如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return url + '可以访问'
    except:
         return url + "产生异常"


class MyThread(threading.Thread):
    def __init__(self, func, args=()):
        threading.Thread.__init__(self)
        self.args = args
        self.func = func
        # self.result = self.func(*self.args)

    def run(self):
        mutex.acquire()
        self.result = self.func(*self.args)
        mutex.release()

    def get_result(self):
        try:
            return self.result
        except Exception as e:
            return None


mutex = threading.Lock()
threads = []

with open('url_data.txt', 'r') as f1:
    lines1 = f1.read().splitlines()
    lines = []
    for line in lines1:
        if ';' in line:
            l1 = line.split(';')
            for i in l1:
                lines.append(i)
        else:
            lines.append(line)

# print(lines)


for i in lines:
    thread1 = MyThread(getHtmlText, args=(i,))
    thread1.start()
    # thread2 = MyThread(getHtmlText, args=(lines[i+1],)).start()
    # thread3 = MyThread(getHtmlText, args=(lines[i+2],)).start()
    #
    threads.append(thread1)
    # threads.append(thread2)
    # threads.append(thread3)

for t in threads:
    t.join()
    print(t.get_result())
#     results.append(t.get_result())
# print(results)
print("Exiting Main Thread")



