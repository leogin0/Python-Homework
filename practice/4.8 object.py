class Dog:
    count = 0
    def __init__(self,colour,name):
        self.colour = colour
        self.name = name
        Dog.count += 1
    def bark(self):
        print("%s is barking"%self.name)

dog1 = Dog('green','bob')
dog2 = Dog('yellow','aa')

print(Dog.count)