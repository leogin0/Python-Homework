#写函数，统计字符串中有几个字母，几个数字，几个空格，几个其他字符，并返回结果;

def count(s):
    num = char = space = other = 0
    for i in s:
        if i.isdigit():
            num += 1
        elif i.isalpha():
            char += 1
        elif i == ' ':
            space += 1
        else:
            other += 1
    print('数字%d个，字母%d个，空格%d个，其他字符%d个' %(num,char,space,other))

str1 = input('输入一串字符')
count(str1)