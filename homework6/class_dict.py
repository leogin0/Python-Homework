# 定义一个字典类：dictclass。完成下面的功能：
# dict = dictclass({你需要操作的字典对象})
# 1 删除某个key
# del_dict(key)
# 2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"
# get_dict(key)
# 3 返回键组成的列表：返回类型;(list)
# get_key()
# 4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)
# update_dict({要合并的字典})

class dictclass:
    d = {}
    def __init__(self, d):
        self.d = d

    def get_dict(self, key):
        if key in self.d.keys():
            return self.d[key]
        else:
            return 'not found'

    def del_dict(self, key):
        if key not in self.d.keys():
            return 'no this key'
        else:
            self.d.pop(key)
            return 'delete success'
    
    def get_key(self):
        l1 = []
        for key in self.d.keys():
            l1.append(key)
        return l1
    
    def update_dict(self, d2):
        dictMerged2 = self.d.copy()
        dictMerged2.update( d2 )
        return dictMerged2

d = dictclass({'one':1, 'two':2, 'three':3})
print(d.get_dict('one'))
print(d.del_dict('three'))
print(d.get_key())
print(d.update_dict({'four':4, 'five':5}))


