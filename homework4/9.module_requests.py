#从网络上下载一张图片，保存到计算机的指定目录；（requests和os模块）

import os
import requests

url = "http://pic49.nipic.com/file/20140922/2531170_191654419000_2.jpg"

path ='D:/'  + url.split('/')[-1]

try:

    if not os.path.exists(path):

        r = requests.get(url).raise_for_status().content

        with open(path,'w') as f:

            f.write(r)

            print("图片保存成功")

    else:

        print("图片已存在")

except:

    print("图片获取失败")