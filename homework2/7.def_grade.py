'''随机生成20个学生的成绩; 判断这20个学生成绩的等级; 用函数来实现;  
    A---成绩>=90;  
    B-->成绩在 [80,90)
    C-->成绩在 [70,80)
    D-->成绩<70
'''
import random

def grade(g):
    l = {}
    for i in g:
        if i >=90:
            l[i] = 'A'
        elif i >=80 and i < 90:
            l[i] = 'B'
        elif i >=70 and i < 80:
            l[i] = 'C'
        else:
            l[i] = 'D'
    print(l)


list1 = [random.randint(0,100) for x in range(20)]
grade(list1)