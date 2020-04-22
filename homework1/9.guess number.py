#设计一个猜数字 游戏；最多只能猜测N次，在N次之内猜不出，就退出程序，提示猜测失败；

import random
n = random.randint(1,10)    #随机生成一个1~10之间的数
for i in range(6):          #猜5次
    x = int(input("猜数字第%d次："%i))
    if x == n:
        print('恭喜你！猜对了') 
        break            
    elif i == 5 and x!= n:
        print('很遗憾，您未猜对,数字为：',n)