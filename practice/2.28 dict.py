d1 = {'no':100,'name':'tom','class':'1','age':18}
d2 = {'a':101,'b':102,'c':103,'d':104,'e':105}
print(d1['name'])
print(d1.keys())
print(d1.values())
print(d2)
#增
d2['f'] = 106
print(d2)
#修改
d1['no'] = 10
print(d1)
#删除
d2.pop('a')
print(d2)