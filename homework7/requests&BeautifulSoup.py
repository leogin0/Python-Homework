# 给定100个企业网站首页链接地址（用1中给出的URL地址）；请爬取每个页面上，企业介绍的链接地址；
#     说明，满足企业介绍网址的条件是， 标题包含：企业介绍，关于我们，企业发展，发展历史，企业概况等关键字的URL地址；
#     提示：要用到requests库，BeautifulSoup库

import requests
import re
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        reponse = requests.get(url)
        reponse.encoding = reponse.apparent_encoding
    except HTTPError:
        print('httperror')
    except requests.exceptions.ConnectionError:
        pass
    else:
        soup = BeautifulSoup(reponse.text, 'html.parser')
        title = soup.find_all("a")
        for h in title:
            hh = h.get('href')
            if hh and 'html' in hh:
                try:
                    reponse1 = requests.get('http://www.chrtc.cn')
                    reponse1.encoding = reponse1.apparent_encoding
                except HTTPError:
                    print('httperror')
                except requests.exceptions.ConnectionError:
                    pass
                else:
                    soup1 = BeautifulSoup(reponse1.text, 'html.parser')
                    title1 = soup1.find_all("a", text='公司介绍')
                    if title1:
                        if 'http' not in hh:
                            print(url + hh)
                        else:
                            print(hh)
                    break


with open('url.txt', 'r') as f1:
    count = 1
    while count < 100:
        line = f1.readline()
        while line:
            line = line.strip()
            getTitle(line)
            line = f1.readline()
            count += 1







