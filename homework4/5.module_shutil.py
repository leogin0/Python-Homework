#通过Python来模拟实现一个txt文件的拷贝过程

# shutil模块是一个文件、目录的管理接口，提供了一些用于复制文件、目录的函数 
# copyfile()函数可以实现文件的拷贝 
# copyfile(src, dst) 
# move()函数实现文件的剪切 
# move(src, dst)

import shutil

file = input('输入您要拷贝的txt文件')
copyfile = input('输入您要粘贴的路径')
print('-----正在拷贝中-----')
try:
    shutil.copyfile(file, copyfile)  
except IOError:
    print("没有找到拷贝文件！")
else:
    print('拷贝成功！')
