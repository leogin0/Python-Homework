#写函数，判断用户传入的对象（字符串、列表、元组）长度,并返回给调用者。
def length(a):
    return len(a)

num = eval(input('请输入字符串，列表或者元组'))
print('长度为:',length(num))