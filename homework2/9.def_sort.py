#定义一个函数，函数接收一个数组，并把数组里面的数据从小到大排序(冒泡排序,  也可以直接使用相关的函数);
#sort是对列表内部排序，不会返回任何值

def sort1(list1):   #函数排序
    list1.sort()
    print(list1)

list1 = [2,3,4,1,2,1]
sort1(list1)



# def sort2(list1):      #冒泡排序
#     n = len(list1)
#     for j in range(0, n - 1):
#         for i in range(0, n - 1 - j):
#             if list1[i] > list1[i + 1]:
#                 list1[i], list1[i + 1] = list1[i + 1], list1[i]
#     print(list1)

# l = [2,3,4,1,2,1]
# sort2(l) 
