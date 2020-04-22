#定义2个列表，并初始化；  找出这2个列表中，相同的元素并输出；
list1 = [1,3,'hhh','hello','bye']
list2 = ['hello',3,5,7,'bye']
for i in list1:
    for j in list2:
        if i == j:
            print(i)