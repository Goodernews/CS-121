dist = lambda x0, y0, x1, y1 :(((x0-x1)**2+(y0-y1)**2)**0.5)
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
    def getMoney(self):
        return self.money
    def pay(self, amount):
      self.money -= amount
    def fillUp(self, amount):
      self.tank+= amount

dist = lambda x0, y0, x1, y1 :(((x0-x1)**2+(y0-y1)**2)**0.5)

class GasStation:
  def __init__(self, x, y, price):
    self.x = x
    self.y = y
    self.price = price
  def refillCar(self, customer):
    if dist(customer.x, customer.y, self.x, self.y)<=0.001:
      if customer.getMoney()>=customer.getToFill()*self.price:
        customer.pay(customer.getToFill()*self.price)
        customer.fillUp(customer.getToFill())
        return True
    return False
