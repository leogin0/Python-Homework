#定义一个函数, 打印输出n以内的斐波那契数列;
def fibonacci(a,b,n):
    f1 = a
    f2 = b
    print(f1)
    print(f2)
    for i in range(1,n):
        if i == f1 + f2:
            print(i)
            f1,f2 = f2,i

n = int(input('请输入数字限定数列范围'))
a = int(input('输入第一个数字'))
b = int(input('第二个数字'))
fibonacci(a,b,n)