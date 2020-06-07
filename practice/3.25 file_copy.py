import os

l1 = []
def copy(path1 , path2):
    if os.path.exists(path1):
        with open(path1 , 'r') as f1:
            l1.append(f1.read())
        with open(path2 , 'w') as f2:
            f2.write(''.join(l1))
    else:
        print('文件不存在!')

copy(r'D:\homework3\input.txt',r'D:\123.txt')
        