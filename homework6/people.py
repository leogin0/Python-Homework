class person:
    def __init__(self, blood, power):
        self.blood = blood
        self.power = power
    
    def beatedd(self, powerd):
        if self.power != 0 and powerd != 0:
            self.power -= 2
        self.blood -= powerd
    
