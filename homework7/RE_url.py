#给定一个文件，请用正则表达式，逐行匹配提取其中的URL链接信息，并保存到另外一个文件中；
#   提示，文件有1000行，注意控制每次读取的行数；

import re

url = []

with open('webspiderUrl.txt', 'r', encoding='utf8') as f1:
    line = f1.readline()
    while line:
        ret = re.findall(r'http://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', line)
        if ret:
            for i in ret:
                url.append(i)
        line = f1.readline()

with open('url.txt', 'w') as f2:
    for i in url:
        f2.write(i + '\n')