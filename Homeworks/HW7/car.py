class Car:
    def __init__(self, mpg, full, money):
        self.x = 0
        self.y =  0
        self.tank = full #set tank to fill
        self.mpg = mpg
        self.full = full
        self.money = money
    def driveTo(self, newX, newY):
        gallons_req = (((self.x-newX)**2+(self.y-newY)**2)**0.5)/self.mpg
        if gallons_req<=self.tank:
            self.tank = self.tank-gallons_req
            self.x=newX
            self.y=newY
            return True
        else:
            return False

    def getLocation(self):
        return [self.x, self.y]#returns coordinate point
    def getGas(self):
        return self.tank #returns how many gals left
    def getToFill(self):
        return self.full-self.tank
