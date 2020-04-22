#请用Python定义一个函数，给定一个字符串，找出该字符串中出现次数最多的那个字符，并打印出该字符及其出现的次数。
# 例如，输入 aaaabbc，输出：a:4

def times(str1):
    d = {}
    for i in str1:
        d[i] = d.get(i,0) + 1
    sort_d = sorted(d.items(),key = lambda x: x[1],reverse=True)
    print(sort_d[0])

str1 = input('请输入一个字符串')
times(str1)