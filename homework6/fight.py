from dogs import dog
from people import person
import random

class fight:
    dog = []
    person = []
    #传入狗和人的列表
    def __init__(self, dog, person):
        self.dog = dog
        self.person = person
    
    def beat(self):
        # for i in range(len(self.person)):
        #     if self.person[i].blood <= 0:
        #         self.person.pop(i)

        # for i in range(len(self.dog)):
        #     if self.dog[i].blood <= 0:
        #         self.dog.pop(i)
        
        
        nump = len(self.person)
        numd = len(self.dog)
        a = random.randint(0,10)
        
        while nump != 0 and numd != 0:
            p = random.randint(0,len(self.person)-1)
            d = random.randint(0,len(self.dog)-1)
            a += 1

            if a % 2 == 0:    
                self.person[p].beatedd(self.dog[d].power)
                print('dog' + str(d) + ' is beating person' + str(p))
                print('person' + str(p) + '\nblood:' + str(self.person[p].blood) + '\npower:' + str(self.person[p].power))
                if self.person[p].blood <= 0:
                    print('person %d dead!'%p)
                    self.person.pop(p)
                    nump = len(self.person)
                print('-'*10)
            else:
                self.dog[d].beatedp(self.person[p].power)
                print('person' + str(p) + ' is beating dog'  + str(d))
                print('dog' + str(d) + '\nblood:' + str(self.dog[d].blood) + '\npower:' + str(self.dog[d].power))
                if self.dog[d].blood <= 0:
                    print('dog %d dead!'%d)
                    self.dog.pop(d)
                    numd = len(self.dog)
                print('-'*10)


        if  nump== 0 and numd != 0:
            print('dogs win!')
        elif nump != 0 and numd == 0:
            print('people win')
        elif nump == 0 and numd == 0:
            print('The game ended in a draw')


    
        
