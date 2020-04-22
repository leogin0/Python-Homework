#打印输出9*9乘法表
for i in range(1,10):
    for j in range(1,10):
        if(i >= j):
            m = i * j
            print('%d×%d=%d'%(j,i,m),end="  ")   #end="" 不换行
    print('\n')