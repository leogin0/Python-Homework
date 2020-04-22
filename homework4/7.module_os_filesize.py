#使用python代码统计一个文件夹中所有文件的总大小

import os

size = 0

for file in os.listdir(os.getcwd()):
    if os.path.isfile(file):
        size = size + os.path.getsize(file)

print('%s下的所有文件大小为%dkb'%(os.getcwd(),size))