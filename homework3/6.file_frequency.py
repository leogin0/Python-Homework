#对一篇英文小说，进行词频统计，输出前20个出现频率最高的单词；

def getText():
    try:
        txt = open('D:\homework3\《老人与海》[英文版].txt','r',encoding='utf8').read()
    except IOError:
    print('Error:没有找到文件或文件读取失败')
    txt = txt.lower()
    for ch in '|"#$%&^*()_+{}:<>?@\,~!.\n':
        txt = txt.replace(ch,' ')
    return txt

def times(str1):
    d = {}
    l1 = str1.split(' ')
    l2 = filter(lambda x : x,l1)
    for i in l2:          
        d[i] = d.get(i,0) + 1
    sort_d = sorted(d.items(),key = lambda x: x[1],reverse=True)
    for i in range(20):
        print(sort_d[i])

times(getText())

