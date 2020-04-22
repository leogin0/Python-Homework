# 在2个文件中存放了英文计算机技术文章(可以选择2篇关于Python技术文件操作处理技巧的2篇英文技术文章), 
# 请读取文章内容,进行词频的统计;并分别输出统计结果到另外的文件存放;
# 比较这2篇文章的相似度(如果词频最高的前10个词,重复了5个,相似度就是50%;重复了6个,相似度就是60% ,......);

def getText(str1):
    txt = open(str1,'r',encoding='utf8').read()
    txt = txt.lower()
    for ch in '|"#$%&^*()_+{}:<>?@\,~!.\n':
        txt = txt.replace(ch,' ')
    return txt

def times(str2,str3):
    d = {}    
    l1 = str2.split(' ')
    l2 = filter(lambda x : x,l1)
    l3 = []
    for i in l2:          
        d[i] = d.get(i,0) + 1
    sort_d = sorted(d.items(),key = lambda x: x[1],reverse=True)
    with open(str3,'w') as f1:
        f1.write('\n'.join('%s %s' % x for x in sort_d))
    for i in range(10):
        l3.append(sort_d[i][0])
    return l3

def contrast(l1,l2):
    l3 = [x for x in l1 if x in l2]
    print('相似度为：%d'%(len(l3)*10))

l1 = []
l2 = []
l1 = times(getText('D:\homework3\d1.txt'),'D:\homework3\c1.txt')
l2 = times(getText('D:\homework3\d2.txt'),'D:\homework3\c2.txt')
contrast(l1,l2)


