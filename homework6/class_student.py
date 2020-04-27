# 定义一个学生Student类。有下面的类属性：
# 1 姓名 name
# 2 年龄 age
# 3 成绩 score（语文，数学，英语) [每课成绩的类型为整数]
# 类方法：
# 1 获取学生的姓名：get_name() 返回类型:str
# 2 获取学生的年龄：get_age() 返回类型:int
# 3 返回3门科目中最高的分数。get_course() 返回类型:int
# 写好类以后，可以定义2个同学测试下:

class Student:
    # name = ''
    # age = 0
    # score = [0, 0, 0]

    @property
    def name(self):
        print('name:' + self._name)

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError('name must be an str!')
        self._name = value
    
    @property
    def age(self):
        print('age:' + str(self._age)) 

    @age.setter
    def age(self, age):
        if not isinstance(age, int):
            raise ValueError('score must be an integer!')
        self._age = age

    @property
    def course(self):
        m = max(self.score[0], self.score[1], self.score[2])
        
        if self.score.index(m) == 0:
            str1 = 'chinese'
        elif self.score.index(m) == 1:
            str1 = 'math'
        else:
            str1 = 'english'
        print('the highest score is:' +  str1 + ' ' + str(m))

    @course.setter
    def course(self, score):
        if not isinstance(lambda x : x in score, int):
            raise ValueError('score must be an integer!')
        if (lambda x : x in score) < 0 or (lambda x : x in score) > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = score


s1 = Student()
s1.name = 'Tom'
s1.age = 18
s1.score = [91,92,93]
s1.name
s1.age
s1.course