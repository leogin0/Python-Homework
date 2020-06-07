#练习1:  在window平台下练习os.path 相关方法的使用! 观察输出结果;

# import os
 
# print( os.path.basename('/root/runoob.txt') )   # 返回文件名
# print( os.path.dirname('/root/runoob.txt') )    # 返回目录路径
# print( os.path.split('/root/runoob.txt') )      # 分割文件名与路径
# print( os.path.join('root','test','runoob.txt') )  # 将目录和文件名合成一个路径
# print( os.path.abspath('/root/runoob.txt') )


# 练习2:  构造上述文件结构,分别在指定位置打开文件进行写入操作;
#同级文件夹里面打开;  同级目录下的子目录里面打开; 上一级文件目录中的其他文件夹中打开

# f2 = open( 'D:\222.txt' ,'r' , encoding='utf8')            #绝对路径
# f2.close()

# with open( r"..\homework2\333.txt","r" ) as f3:
#     print(f3.read())

# #练习3
# f = open("/Python/class.txt","r",encoding = "utf8")
# str = f.read()
# print(str)
# f.close()

# #练习4
#一个文件内容的如下,请按照行读取文件的内容,  将分数排序后输出到另外一个文件中:
 #           姓名      学号       分数
 #           张三      101         78
 #           李四      102         87
 #           王五      103         83

# def takeThird(elem):
#     return elem[2]
# l1 = []
# with open("/Python/class.txt","r",encoding= "utf8") as f1:
#     for i in range(4):
#         l1.append(f1.readline().split())

# l1.sort(key=takeThird, reverse=True)
# print(l1)

# with open("/Python/sort.txt","w") as f2:
#     for j in range(4):
#         f2.write(' '.join(l1[j]))
#         f2.write("\n")

# 练习5：
#   给定一个字典,保存了5个同学的学号,姓名,年龄;使用pickle模块将数据对象保存到文件中去;
# import pickle, pprint
# d1 = {'赵一':[101, 18],'钱二':[102, 18],'孙三':[103, 18],'李四':[104, 19],'王五':[105, 20]}
# selfref_list = [1, 2, 3 ,4 ,5]
# selfref_list.append(selfref_list)
# f1 = open('/Python/pickle.pkl','wb')
# pickle.dump(d1, f1)
# pickle.dump(selfref_list, f1, -1)
# f1.close()

# pkl_file = open('/Python/pickle.pkl', 'rb')

# data1 = pickle.load(pkl_file)
# pprint.pprint(d1)

# d2 = pickle.load(pkl_file)
# pprint.pprint(d2)

# pkl_file.close()