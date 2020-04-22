#写一个程序，读取键盘输入的任意行文字信息
# 当输入空行时结束输入，将读入的字符串存于列表;然后将列表里面的内容写入到文件input.txt中；

l1 = []
print('请输入任意行文字信息：')
while True:
    p1 = input()
    if p1.strip() == '':
        break
    else:
        l1.append(p1)

try:
    with open("homework3\\input.txt",'w') as f1:
        f1.write('\n'.join(l1))
except IOError:
    print("Error:没有找到文件或文件读取失败")
else:
    print("内容写入文件成功")
    
