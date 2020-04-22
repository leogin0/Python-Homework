#编写一个程序，读取文件中保存的10个学生成绩名单信息(学号,姓名, Python课程分数); 然后按照分数从高到低进行排序输出
d1 = {} 
l2 = []
try:
    with open('/homework3/student.txt','r',encoding='utf8') as f1:
        line = f1.read().strip()
        l1 = line.split('\n')
        for i in l1:
            l2.append(i.split(' '))
        l2.sort(key = lambda x:x[2])
        l2.reverse()
        print(l2)
except IOError:
    print('Error:没有找到文件或文件读取失败')