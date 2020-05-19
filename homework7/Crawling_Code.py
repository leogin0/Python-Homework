from bs4 import BeautifulSoup
import requests

url = 'https://www.programcreek.com/python/index/221/requests'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
r = requests.get(url,headers=headers).content.decode('utf-8')

soup = BeautifulSoup(r,'html.parser')
re_a = soup.find(id='api-list').find_all('a')
# print(re_a)
list = []
for i in re_a:
	list.append(i.attrs['href'])
# print(list)

data = []
for x in list:
    dict = {}
    # 请求详细页面
    test = requests.get(x, headers=headers).content.decode('utf-8')
    # print(test)

    # 解析html文档
    soup_test = BeautifulSoup(test, 'html.parser')
    # print(type(soup_test))

    # 查找练习内容
    # 查找标题
    dict['title'] = soup_test.find(id='main').h1.text

    # 查找程序代码
    list1 = []
    for tag in soup_test.find_all('pre', class_='prettyprint'):
        # print(tag)
        list1.append(tag.text)
    dict['dm'] = list1



    with open('1.txt','a+',encoding='utf-8') as file:
        file.write(dict['title']+'\n')
        for i in dict['dm']:
            file.write(i+'\n')
        file.write('*'*50+'\n')
        file.write('\n')

