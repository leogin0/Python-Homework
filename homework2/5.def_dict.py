#写函数，检查传入字典的每一个value长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者;

def length(dict1):
    for key,value in dict1.items():
        if len(value) > 2:
            dict1[key] = value[0 : 2]
    return dict1

dict1 = {'a':'123','b':'45','c':'9890'}
print(length(dict1))