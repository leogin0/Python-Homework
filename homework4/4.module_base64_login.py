#模拟用户登录:
#5个同学的姓名,账号和密码(加密后的),保存在一个文件上;   
#系统提示,请输入登录同学姓名, 正确后,请输入账号, 正确后,提示请输入密码（输入明文）;  
#如果都正确,打印提示, 您登录成功(失败);

import base64
import re

with open('D:/homework4/classmates','r') as f1:
    line = f1.readline()
    l1 = []
    while line:
        a = line.split()
        b = a[0]
        l1.append(b)
        line = f1.readline()

name = input('请输入登录同学姓名：')

if name in l1:
    with open('D:/homework4/classmates','r') as f2:
        l2 = []
        for line in f2:
            if line.strip():
                tmp = re.split("\s+",line.strip())
            if tmp[0] == name:
                l2 = tmp.copy()
    #print(l2)
    account = input('请输入账号：')
    if account == l2[1]:
        password = input('请输入密码:')
        pw = bytes(l2[2],encoding='utf8')
        decode = base64.b64decode(pw).decode("utf8")
        if decode == password:
            print('登录成功!')
        else:
            print('密码错误，登录失败！')
    else:
        print('输入账号错误！')
else:
    print('没有此同学！')



