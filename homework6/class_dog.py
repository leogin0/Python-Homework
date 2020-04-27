#定义一个狗类,里面有一个 列表成员变量(列表的元素是字典), 分别记录了 3种颜色的狗的颜色, 数量,和价格;
#    实现狗的买卖交易方法;  打印输出经过2-3次买卖方法后,剩下的各类狗的数量;

class dog:
    #颜色：（数量，价格）
    def __init__(self):
        self.dogs = [{'colour':'red', 'quantity':3, 'money': 100}, {'colour':'green','quantity':2, 'money': 150}, 
        {'colour':'yellow', 'quantity':5,'money': 80}]
    
    def sell(self, colour, quantity):
        for i in range(3):
            if self.dogs[i]['colour'] == colour:
                self.dogs[i]['quantity'] -= quantity
                print('sell %d %s dog'%(quantity, colour))
                break
        else:
            print('no dog match this colour ！')
    
    def buy(self, colour, quantity, money):
        for i in range(len(self.dogs)):
            if self.dogs[i]['colour'] == colour:
                self.dogs[i]['quantity'] += quantity
                break
        else:
            self.dogs.append({'colour' : colour , 'quantity': quantity, 'money': money})
        print('spend % d buy %d %s dog'%(money, quantity, colour))
    def count(self):
        print('The number of different breeds of dogs left：')
        #print(self.dogs)
        for i in range(len(self.dogs)):
            print(self.dogs[i]['colour'] + '  ' + str(self.dogs[i]['quantity']))

d = dog()
d.buy('blue', 1, 100)
d.sell('yellow', 2)
d.count()

