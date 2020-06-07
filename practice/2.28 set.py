b = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
a = set('abc')
#b中存在的元素a不存在的元素
print(b-a)
#增
a.add('g')
print(a)
#删除
a.remove('a')
print(a)
#长度
print(len(b))