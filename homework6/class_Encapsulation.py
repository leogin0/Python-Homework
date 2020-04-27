# 封装一个学生类，有姓名，有年龄，有性别，有英语成绩，数学成绩，语文成绩，
#       封装方法，求单个学生的总分，平均分，以及打印学生的信息。


class student:
    def setname(self, name):
        self.__name = name

    def getname(self):
        return self.__name
    name = property(getname, setname)

    def setage(self, age):
        if isinstance(age, int):
            self.__age = age
        else:
             print("error:age is not 'int'")

    def getage(self):
        return self.__age
    age = property(getage, setage)

    def setsex(self, sex):
        if sex == 'boy' or sex == 'girl':
            self.__sex = sex            
        else:
            print('sex must be girl or boy')

    def getsex(self):
        return self.__sex
    sex = property(getsex, setsex)

    def setenglish(self, english):
        if english > 100 or english < 0:
            print("error:english must in [0,100]")
        else:     
            self.__english = english

    def getenglish(self):
        return self.__english
    english = property(getenglish, setenglish)

    def setmath(self, math):
        if math > 100 or math < 0:
            print("error:math must in [0,100]")
        else:
            self.__math = math

    def getmath(self):
        return self.__math
    math = property(getmath, setmath)

    def setchinese(self, chinese):
        if chinese > 100 or chinese < 0:
            print("error:chinese must in [0,100]")
        else:
            self.__chinese = chinese

    def getchinese(self):
        return self.__chinese
    chinese = property(getchinese, setchinese)

    def  total(self):
        total = self.__english + self.__math + self.__chinese
        return str(total)
    
    def average(self):
        total = self.__english + self.__math + self.__chinese
        average = total / 3
        return str(average)

    def message(self):
        print("name:" + self.__name)
        print("age:" + str(self.__age))
        print("sex:" + self.__sex)
        print("english:" + str(self.__english))
        print("math:" + str(self.__math))
        print("chinese:" + str(self.__chinese))

s = student()
s.name = 'tom'
s.age = 18
s.sex = 'boy'
s.english = 90
s.math = 90
s.chinese = 90
s.message()
print('total：' + s.total())
print('average:' + s.average())

