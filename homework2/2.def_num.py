#编写一个函数,接收n个数字，求这些参数数字的和;
# def sum(number):
#     n = 0
#     for i in number:
#         n = i + n
#     print('和为:',n)

# s = []
# while 1:
#     num = int(input('请输入数字，输入q结束'))    
#     s.append(num)
#     quit = input()
#     if quit == 'q':
#         break
# sum(s)

def sum(*number):
    n = 0
    for i in number:
        n = i + n
    print('和为:',n)

sum(1,2,3,4)