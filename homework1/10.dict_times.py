'''给定一段英文文本，统计每个单词出现的次数；打印输出，按照词频从高到低输出：
提示：可以用字典来统计：key 是单词，value 是单词出现次数；
先创建一个字典，然后遍历刚刚取出的单词列表，接着做一个判断： 
如果字典中 key 已经出现了这个单词，那么它对应的 value ，也就是出现次数就 +1； 
如果这个单词没出现过，就直接 插入这个单词及 value 为 1 到 字典中；'''

word = "you never know how strong you really are until being strong is the only choice you have."
word = word.replace(',','').replace('.','')
word = word.split()
print(word)
d = {}
for i in word:
    d[i] = d.get(i,0) + 1
sort_d = sorted(d.items(),key = lambda x: x[1],reverse=True)

print('排序后：',sort_d)
    
