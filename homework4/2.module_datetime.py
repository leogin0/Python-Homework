#定义一个函数，判断一个输入的日期，是当年的第几周，周几？  
#将程序改写一下，能针对我们学校的校历时间进行计算（校历第1周，2月17-2月23；校历第27周，8月17-8月23；）；
import time
import datetime

# def date():
#     str1 = input('请输入一个日期：')
#     date1 = datetime.datetime.strptime(str1,'%Y-%m-%d')
#     week1 = datetime.datetime.strftime(date1,'%W')
#     week2 = datetime.datetime.strftime(date1,'%w')
#     print('%s是第%s周，周%s'%(str1,week1,week2))

# date()

def schooldate():
    str1 = input('请输入一个日期：')
    date1 = datetime.datetime.strptime(str1,'%Y-%m-%d')
    date2 = datetime.datetime.strptime('2020-2-17','%Y-%m-%d')
    date3 = datetime.datetime.strptime("2020-8-23",'%Y-%m-%d')

    if date1 >= date2 and date1 <=date3:    
        week = int(datetime.datetime.strftime(date2,'%W'))
        week1 = int(datetime.datetime.strftime(date1,'%W')) - week + 1
        week2 = datetime.datetime.strftime(date1,'%w')
        print('%s是校历第%d周，周%s'%(str1,week1,week2))
    else:
        print('日期不在范围内！')

schooldate()