#前面2个元素为0，1，输出100以内的斐波那契数列；
#列表版
plist = [0,1]
for i in range(101):
    if(i == plist[len(plist) - 1] + plist[len(plist) - 2]):
        plist.append(i)    
print(plist)

#直接输出数字版
f1 = 0
f2 = 1
print(f1)
print(f2)
for i in range(1,100):
    if i == f1 + f2:
        print(i)
        f1,f2 = f2,i