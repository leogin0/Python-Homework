import urllib.request
import urllib

from lxml import etree
from lxml.etree import tostring
import threading
import time
import pymysql


def get_one_item(items):  # 获得一个信息条目的所有信息
    info=[]
    try:
        item = items[0].getchildren()
    except IndexError:
        print("完毕")
        avg_sa = calculate_avg()
        print("北京python开发工程师平均工资:{:.2f}元/月".format(avg_sa))
        exit(0)
    try:
        for it in item:
            content = tostring(it, encoding="utf-8").decode('utf-8')
            # print(content)

            if ('<p class="t1' in content):  # 获取标题
                title = content.split('<a target="_blank" title="')[1]
                title = title.split('" href="')[0]
                info.append(title)

            if ('<span class="t2' in content):  # 获取公司名称
                company = content.split('<a target="_blank" title="')[1]
                company = company.split('" href="')[0]
                info.append(company)

            if ('<span class="t3' in content):  # 获取公司地址
                address = content.split('"t3">')[1]
                address = address.split('</span>')[0]
                info.append(address)

            if ('<span class="t4' in content):  # 获取工资
                salary = content.split('"t4">')[1]
                salary = salary.split('</span>')[0]
                info.append(salary)

            if ('<span class="t5' in content):  # 获取发布日期
                date = content.split('"t5">')[1]
                date = date.split('</span>')[0]
                info.append(date)
    except IndexError:
        info=[]
        return info
        pass

    return info

#一个页面中的所有信息
def get_page_info(url):
    req = urllib.request.Request(url)
    html = urllib.request.urlopen(req).read()

    # 解析html为HTML DOM文档
    selector = etree.HTML(html)
    # 抓取一项信息
    page_info = []
    for i in range(4, 54):  # 获取所有的信息项目

        xpa = '//*[@id="resultList"]/div[' + str(i) + ']'
        items = selector.xpath(xpa)
        if(len(get_one_item(items))!=0):
            page_info.append(get_one_item(items))
            # print(get_one_item(items))

    return page_info

#多线程执行的函数
def run_get(pagenum,name):
     url='https://search.51job.com/list/000000,000000,0000,' \
        '00,9,99,python%25E5%25BC%2580%25E5%258F%2591%25E5%25B7%25A' \
        '5%25E7%25A8%258B%25E5%25B8%2588,2,'+str(pagenum[0])+'.html?lang=c&postchannel=0000&w' \
        'orkyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
     pagenum[0]+=1
     pageInfo=get_page_info(url)
     print(name)
     print(pageInfo)


     # 存入数据库
     # 连接MYSQL数据库
     db = pymysql.connect(host='127.0.0.1', user='root', password='root', db='jobinfo', port=3306)
     print('连接数据库成功！')
     conn = db.cursor()  # 获取指针以操作数据库
     # conn.execute('set names utf8')
     for ite in pageInfo:
         for i in range(len(ite)):
             ite[i] = '"' + ite[i] + '"'
         sql = 'insert into `table`(岗位,公司名称,公司地址,薪资,发布日期) values({},{},{},{},{})'.format(ite[0], ite[1], ite[2], ite[3],
                                                                                         ite[4])
         conn.execute(sql)
         db.commit()
     db.close()

def calculate_avg():#计算北京地区的平均薪资
    # 读取数据库
    # 连接MYSQL数据库
    db = pymysql.connect(host='127.0.0.1', user='root', password='root', db='jobinfo', port=3306)

    print('连接数据库成功！')
    conn = db.cursor()  # 获取指针以操作数据库
    # conn.execute('set names utf8')
    sql = "SELECT 薪资 FROM `table` WHERE 公司地址 LIKE '北京%'"
    conn.execute(sql)

    desc = conn.description  # 获取字段的描述，默认获取数据库字段名称，重新定义时通过AS关键重新命名即可
    data_dict = [dict(zip([col[0] for col in desc], row)) for row in conn.fetchall()]  # 列表表达式把数据组装起来
    db.commit()
    db.close()
    total=0.0
    for dic in data_dict:
        if("万/月" in dic['薪资']):
            value=dic['薪资'].split('万')[0]
            value=value.split('-')
            a=float(value[0])*10000
            b=float(value[1])*10000
            total+=(a+b)/2
        elif("千/月" in dic['薪资']):
            value = dic['薪资'].split('千')[0]
            value = value.split('-')
            a = float(value[0]) * 1000
            b = float(value[1]) * 1000
            total += (a + b) / 2
        elif("万/年" in dic['薪资']):
            value = dic['薪资'].split('万')[0]
            value = value.split('-')
            a = float(value[0]) * 10000/12
            b = float(value[1]) * 10000/12
            total += (a + b) / 2
        elif("元/天" in dic['薪资']):
            value = dic['薪资'].split('元')[0]
            a = float(value[0]) * 30
            total += a
        else:
            value = dic['薪资'].split('元')[0]
            a = float(value[0]) * 30*24
            total += a

    avg=total/len(data_dict)
    return avg



if __name__ == '__main__':
     num=[1]
     while num[0]<38:
         t1 = threading.Thread(target=run_get(num,'thread_1'))
         t1.start()
         t2 = threading.Thread(target=run_get(num,'thread_2'))
         t2.start()
         t3 = threading.Thread(target=run_get(num, 'thread_3'))
         t3.start()
         t4 = threading.Thread(target=run_get(num, 'thread_4'))
         t4.start()

     # avg_sa=calculate_avg()
     # print("北京python开发工程师平均工资:{:.2f}元/月".format(avg_sa))
