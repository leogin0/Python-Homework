#写一个程序，从input.txt中读取之前输入的数据，存入列表中，再加上行号打印显示；格式如下
#第一行： xxxx
#第二行： xxxx

try:
    with open("/homework3/input.txt",'r',encoding='utf8') as f1:
        line = f1.read().strip()
        l1 = line.split('\n')        
except IOError:
    print('Error:没有找到文件或文件读取失败')


for i in range(0,len(l1)):
    print('第%d行:'%(i+1),end = '')
    print(l1[i])


