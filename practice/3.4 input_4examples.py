
# #1
# name = input("name:")
# age = input("age:")
# skill = input("skill:")
# salary = input("salary:")
# info = ''' --- info of ''' + name + ''' name: ''' + name + ''' age: ''' + age + ''' skill: ''' + skill + ''' salary: ''' + salary + ''' '''
# print(info)

# #2
# name = input("name:")
# age = input("age:")
# skill = input("skill:")
# salary = input("salary:")
# info1 = ''' --- info of %s --- Name:%s Age:%s Skill:%s Salary:%s ''' % (name,name,age,skill,salary) #注意这里的变量要一 一对应，缺少一个就会报错
# print(info1)

# #3
# name = input("username：")
# age = input("age：")
# skill = input("skill：")
# salary = input("salary：")
# info = ''' --- info of {_name} Name：{_name} Age：{_age} Skill：{_skill} Salary：{_salary} '''.format(_name=name, _age=age, _skill=skill, _salary=salary) #此处是赋值
# print(info)

#4
name = input("name：")
age = input("age：")
skill = input("skill：")
salary = input("salary：")
info = ''' --- info of {0}--- Name：{0} Age：{1} Skill：{2} Salary：{3} '''.format(name, age, skill, salary)
print(info)