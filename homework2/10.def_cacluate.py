# 编写一个函数cacluate, 可以实现2个数的运算(加,减 乘,除)

def cacluate(a,b,n):
    if(n == '+'):
        return a+b
    elif(n == '-'):
        return a-b
    elif(n == '*'):
        return a*b
    elif(n == '/'):
        if(b == 0):
            return 'false'
        else:
            return a/b
    else:
        return 'false'

print('请输入两个数字(空格隔开)：')
a,b = map(int,input().split())
n = input('请输入您要进行的运算(+,-,*,/):')
print('结果为:',cacluate(a,b,n))

