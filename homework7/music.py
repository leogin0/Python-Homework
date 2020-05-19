import urllib
from urllib import parse
from urllib.error import HTTPError
import re
import requests
from bs4 import BeautifulSoup


try:
    reponse = requests.get('http://www.listeningexpress.com/studioclassroom/ad/')
    reponse.encoding = reponse.apparent_encoding
except HTTPError:
    print('httperror')
except requests.exceptions.ConnectionError:
    pass

soup = BeautifulSoup(reponse.text, 'html.parser')
webs = soup.find_all("a")
for web in webs:
    web = str(web)
    ret = re.search(r'(sc-ad).*?(mp3)', web)
    if ret:
        music_url = 'http://www.listeningexpress.com/studioclassroom/ad/' + parse.quote(str(ret.group()))
        # wget.download(music_url)    一直报错http not found 404
        urllib.request.urlretrieve(music_url ,'D://'+str(ret.group()))
        print(music_url + '下载成功！')