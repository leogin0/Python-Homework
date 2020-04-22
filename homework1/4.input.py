#判断用户输入的年份是否为闰年

a = int(input("请输入一个年份："))
if(a % 4 == 0):
    print('%d是闰年' %a)
else:
    print('%d不是闰年' %a)

