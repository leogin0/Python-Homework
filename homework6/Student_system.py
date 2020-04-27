# 用面向对象,实现一个学生Python成绩管理系统;
#       学生的信息存储在文件中;学生信息的字段有(班级,学号,姓名, Python成绩)
#       实现对学生信息及成绩的增,删,改,查方法;

import linecache

class student:
    def __init__(self, clas, no, name, score):
        self.clas = clas
        self.no = no
        self.name = name 
        self.score = score

class sys:
    def __init__(self):
        pass
    def show_menu(self):
        print('--------------成绩管理系统------------------')
        print('            1.添加学生信息')
        print('            2.删除学生信息')
        print('            3.修改学生信息')
        print('            4.查询学生信息')
        print('            0.退出系统')

    def sort(self, no):
        with open('homework6/student_message.txt','r') as f2:
            line = f2.readline()
            l1 = []
            while line:
                a = line.split()
                b = a[1]
                l1.append(b)
                line = f2.readline()
        if no in l1:
            return l1.index(no)
        else:
            return 'error'
            print('error：没有此学生！')
    
    def add(self):
        clas = input('请输入班级：')
        no = input('请输入学号：')
        while True:    
            if self.sort(no) != 'error':
                print('此学号已存在，请重新输入！')
                no = input('请输入学号：')
            else:
                break

        name = input('请输入姓名：')

        score = input('请输入成绩：')
        while True:        
            if int(score) > 100 or int(score) < 0:
                print('成绩必须在0-100之间！请重新输入！')
                score = input('请输入成绩：')
            else:
                break
            

        str1 ='\n' + clas + ' ' + no + ' ' + name + ' ' + score
        with open('homework6/student_message.txt','a') as f1:
            f1.write(str1)
        print('增加学生成功！')
        
    def delete(self):
        no = input('请输入学生学号:')

        while True:
            if self.sort(no) == 'error':
                print('不存在此学号，请重新输入！')
                no = input('请输入学生学号:')
            else:
                break

        with open('homework6/student_message.txt','r') as r:
            lines = r.readlines()
        with open('homework6/student_message.txt','w') as w:
            for l in lines:
                if no not in l:
                    w.write(l)
            print('删除成功！')
        
    def modify(self):
        no1 = input('请输入学生学号:')

        while True:
            if self.sort(no1) == 'error':
                print('不存在此学号，请重新输入！')
                no1 = input('请输入学生学号:')
            else:
                break

        print('请输入修改后的学生信息：')

        clas = input('请输入班级：')
        no = input('请输入学号：')
        while True:    
            if self.sort(no) != 'error' and no != no1:
                print('此学号已存在，请重新输入！')
                no = input('请输入学号：')
            else:
                break

        
        name = input('请输入姓名：')

        score = input('请输入成绩：')
        while True:        
            if int(score) > 100 or int(score) < 0:
                print('成绩必须在0-100之间！请重新输入！')
                score = input('请输入成绩：')
            else:
                break
            

        str1 =clas + ' ' + no + ' ' + name + ' ' + score

        no2 = self.sort(no1) + 1
        theline = linecache.getline(r'homework6\student_message.txt', no2)

        with open('homework6/student_message.txt','r') as r:
            lines = r.readlines()
        with open('homework6/student_message.txt','w') as w:
            for l in lines:
                if no1 in l:                                      
                    l = l.replace(theline, str1)
                w.write(l)
        print('修改成功！')

    def find(self):
        no = input('请输入学生学号:')

        while True:
            if self.sort(no) == 'error':
                print('不存在此学号，请重新输入！')
                no = input('请输入学生学号:')
            else:
                no1 = self.sort(no) + 1
                break
        
        
        theline = linecache.getline(r'homework6\student_message.txt', no1).split()
        print('查找的信息为：')
        for i in theline:
            print(i)

s = sys()
while True:
    s.show_menu()
    choice = int(input("请选择功能:"))
    if choice == 1:
        s.add()
    elif choice == 2:
        s.delete()
    elif choice == 3:
        s.modify()
    elif choice == 4:
        s.find()
    elif choice == 0:
        sys.exit_stus()
    else:
        print("您输入有误，请重新输入")