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

class Taxi(Car):
  def __init__(self, mpg, full, money):
    super().__init__(mpg, full, money)
    self.occupied = False
    self.fare = 0
    self.trip = 0

  def pickup(self):
    if self.occupied ==True:
      return False
    else:
      self.occupied = True
      self.fare = 2
      self.trip = 0
      return True

  def driveTo(self, newX, newY):
    distance =  (((self.x-newX)**2+(self.y-newY)**2)**0.5)
    gallons_req = distance/self.mpg
    if gallons_req<=self.tank:
        self.tank = self.tank-gallons_req
        self.x=newX
        self.y=newY
        if self.occupied == True:
          self.trip += distance
          self.fare += 3*distance
        return True
    else:
        return False

  def dropoff(self):
    if self.occupied==False:
      return False
    else:
      self.occupied=False
      self.money +=self.fare
      return True

class Dispatcher:
  def __init__(self):
    self.fleet = []

  def hire(self, new_hire):
    self.fleet.append(new_hire)

  def hail(self, call_x, call_y):
    dist_cust = lambda x, y: dist(call_x, call_y, x, y)
    not_hired = list(filter(lambda i: i.occupied==False, self.fleet))
    enough_gas = list(filter(lambda i: i.tank*i.mpg>=dist_cust(i.x, i.y), not_hired))
    closest_taxis = sorted(enough_gas, key = lambda i : dist_cust(i.x, i.y))
    if closest_taxis !=[]:
      closest_taxis[0].driveTo(call_x, call_y)
      closest_taxis[0].pickup()
      return closest_taxis[0]
    return None