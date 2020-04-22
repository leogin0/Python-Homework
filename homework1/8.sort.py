#设计一个数据结构，用来存放10个员工的信息并初始化，每个员工信息包括：工号，姓名，工龄，工资；  将这10个员工，按照工资从高到低打印输出；
#  提示：可以组合使用我们的序列数据类型

member = [{'name':'bob','number':120,'year':1,'price':4000},
 {'name':'cindy','number':121,'year':1,'price':2000},
 {'name':'lisa','number':122,'year':2,'price':2600},
 {'name':'kay','number':123,'year':3,'price':1800},
 {'name':'kate','number':124,'year':1,'price':2100},
 {'name':'bitty','number':125,'year':2,'price':3000},
 {'name':'kaw:','number':126,'year':2,'price':2500},
 {'name':'wendy','number':127,'year':1,'price':1500},
 {'name':'jenny','number':128,'year':3,'price':1600},
 {'name':'gisoo','number':129,'year':1,'price':2200}]

sorted_member  = sorted(member,key = lambda x : x['price'],reverse = True)
print('按照工资排序后：',sorted_member )

