
# 元素输出和查找：  请输出0-50之间的奇数，偶数，质数；能同时被2和3整除的数；

print('奇数：',[x for x in range(50) if x % 2 != 0])
print('偶数：',[x for x in range(50) if x % 2 == 0])
p = [2,]
for i in range(2,50):
    for j in range(2,i):
        if i % j == 0:
            break
        if j == i-1:
            p.append(i) 
print('质数:',p)
print('同时被2,3整除的数：',[x for x in range(50) if x % 2 == 0 and x % 3 == 0])  #只能用and
        
