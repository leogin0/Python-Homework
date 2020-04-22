#通过Python来实现显示给定文件夹下的所有文件和文件夹,以及时间，如果是文件，显示大小;

import os,time

print('名称                         日期                      类型       大小')
for file in os.listdir(os.getcwd()):
    print(file.ljust(26),end='')
    print(time.ctime(os.path.getmtime(file)),end='     ')
    if os.path.isfile(file):
        print('文件',end='      ')
        print(str(os.path.getsize(file)) + 'kb',end='   ')
    else:
        print('文件夹',end='   ')
    print('\n')