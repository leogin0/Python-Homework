import os
 
#创建文件
try:
    f1 = open('homework3/blowing in the wind.txt','w')
    f1.write('How many roads must a man walk down \n')
    f1.write('Before they call him a man \n')
    f1.write('How many seas must a white dove sail \n')
    f1.write('Before she sleeps in the sand \n')
    f1.write('How many times must the cannon balls fly \n')
    f1.write('Before they\'re forever banned \n')
    f1.write('The answer my friend is blowing in the wind \n')
    f1.write('The answer is blowing in the wind\n')
    f1.close()
 
    with open('homework3/Blowing in the wind.txt','r') as f2:
        l1 = f2.read().splitlines()
        l1.insert(0,'Blowing in the wind')
        l1.insert(1,'Bob Dylan')
        l1.insert(len(l1),'1962 by Warner Bros.Inc')
    

    with open('homework3/Blowing in the wind.txt','w') as f3:
        f3.write('\n'.join(l1))

    with open('homework3/Blowing in the wind.txt','r') as f4:
        pages = f4.readlines()
        for i in pages:
            print(i)

except IOError:
    print('Error:没有找到文件或文件读取失败')