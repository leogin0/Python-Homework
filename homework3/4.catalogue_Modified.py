#在当前目录新建目录img, 里面包含10个文件, 10个文件名各不相同(X4G5.png)
# 将当前img目录所有以.png结尾的后缀名改为.jpg

import random
import string
import os

try:
    name = [''.join(random.sample(string.ascii_letters + string.digits, 4)) for i in range(10)] 
    os.mkdir('img')
    for i in name:
        os.mkdir('img/' + i + '.png')
except OSError:
    print('目录已存在，无法创建目录')

    files = os.listdir("D:\\myyy\\img")#列出当前目录下所有的文件
    for filename in files:
      portion = os.path.splitext(filename)#分离文件名字和后缀
      if portion[1] == ".png" :
          newname = portion[0] + ".jpg"    
          os.chdir("D:\\myyy\\img")
          os.rename(filename,newname)
          print("修改%s - %s成功！"%(filename,newname))
