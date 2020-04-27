class dog:
    def __init__(self, blood, power):
        self.blood = blood
        self.power = power

    def beatedp(self, powerp):
        if self.power != 0 and powerp != 0:
            self.power -= 3
        self.blood -= powerp
