import random
import tkinter
random.seed()

def plot(xvals, yvals):
    # This is a function for creating a simple scatter plot.  You will use it,
    # but you can ignore the internal workings.
    root = tkinter.Tk()
    c = tkinter.Canvas(root, width=700, height=400, bg='white') #was 350 x 280
    c.grid()
    #create x-axis
    c.create_line(50,350,650,350, width=3)
    for i in range(5):
        x = 50 + (i * 150)
        c.create_text(x,355,anchor='n', text='%s'% (.5*(i+2) ) )
    #y-axis
    c.create_line(50,350,50,50, width=3)
    for i in range(5):
        y = 350 - (i * 75)
        c.create_text(45,y, anchor='e', text='%s'% (.25*i))
    #plot the points
    for i in range(len(xvals)):
        x, y = xvals[i], yvals[i]
        xpixel = int(50 + 300*(x-1))
        ypixel = int(350 - 300*y)
        c.create_oval(xpixel-3,ypixel-3,xpixel+3,ypixel+3, width=1, fill='red')
    root.mainloop()

#Constants: setting these values controls the parameters of your experiment.
injurycost = 11 #Cost of losing a fight
displaycost = 1 #Cost of displaying
foodbenefit = 8 #Value of the food being fought over
init_hawk = 0
init_dove = 0
init_defensive = 0
init_evolving = 10

class Bird():
  def __init__(self, world):
    self.health = 100
    world.birds.append(self)
    self.master = world
  def eat(self):
    self.health+=foodbenefit
  def injured(self):
    self.health-=injurycost
  def display(self):
    self.health-=displaycost
  def die(self):
    self.master.birds.remove(self)
    del self
  def update(self):
    self.health-=1
    if self.health<=0:
      self.die()
    if self.health>=200:
      self.health-=100
      [Dove, Hawk, Defensive][["Dove", "Hawk", "Defensive"].index(self.species)](self.master)

class World(Bird):
  def __init__(self):
    self.birds = []

  def update(self):
    for z in self.birds:
      z.update()

  def free_food(self, for_grabs):
    [random.choice(self.birds).eat() for x in range(0,for_grabs)]
  def conflict(self, num_conflicts):
    fight_club = random.sample(self.birds, 2)
    fight_club[0].encounter(fight_club[1])
  def status(self):
    species = [x.species for x in self.birds]
    print("There are ", str(species.count("Hawk"))," hawks.")
    print("There are ", str(species.count("Dove"))," doves.")
    print("There are ", str(species.count("Defensive"))," defensive.")
    print("There are ", str(species.count("Evolving"))," evolving.")
  def evolvingPlot(self):
    evolving_birds = [x for x in self.birds if x.species=="Evolving"]
    evolve_weight = [y.weight for y in evolving_birds]
    evolve_agression = [z.agression for z in evolving_birds]
    plot(evolve_weight, evolve_agression)

class Hawk(Bird):
  def __init__(self, world):
    super().__init__(world)
    self.species="Hawk"
  def defend_choice(self):
    return True
  def encounter(self, new_friend):
    if new_friend.defend_choice()==False:
      self.eat()
    else:
      hunger_games = [self, new_friend]
      random.shuffle(hunger_games)
      hunger_games[0].eat()
      hunger_games[1].injured()

class Dove(Bird):
  def __init__(self, world):
    super().__init__(world)
    self.species="Dove"
  def defend_choice(self):
    return False
  def encounter(self, new_friend):
    if new_friend.defend_choice()==True:
      new_friend.eat()
    else:
      self.display()
      new_friend.display()
      random.choice([self, new_friend]).eat()

class Defensive(Bird):
  def __init__(self, world):
    super().__init__(world)
    self.species="Defensive"
  def defend_choice(self):
    return True
  def encounter(self, new_friend):
    new_friend.eat()


class Evolving(Bird):
  def __init__(self, world, parent=None):
    super().__init__(world)
    self.species="Evolving"
    if parent == None:
      self.agression = random.random()
      self.weight = random.uniform(1,3)
    else:
      self.agression = min([max([0,parent.agression+random.uniform(-0.05,0.05)]), 1])
      self.weight = min([max([1,parent.weight+random.uniform(-0.1,0.1)]), 3])
  def defend_choice(self):
    if random.random() <=self.agression:
      return True
    return False
  def encounter(self, new_friend):
    me_fight = self.defend_choice()
    friend_fight = new_friend.defend_choice()
    if me_fight==True and friend_fight==True:
      if random.random() <=(self.weight/(self.weight+new_friend.weight)):
        self.eat()
        new_friend.injured()
      else:
        new_friend.eat()
        self.injured()
    if me_fight==False and friend_fight==True:
      new_friend.eat()
    if me_fight==True and friend_fight==False:
      self.eat()
    if me_fight==False and friend_fight==False:
      self.display()
      new_friend.display()
      random.choice([self, new_friend]).eat()
  def update(self):
    self.health-=0.4+(0.6*self.weight)
    if self.health<=0:
      self.die()
    if self.health>=200:
      self.health-=100
      Evolving(self.master, self)

########
# The code below actually runs the simulation.  You shouldn't have to do anything to it.
########
w = World()
for i in range(init_dove):
    Dove(w)
for i in range(init_hawk):
    Hawk(w)
for i in range(init_defensive):
    Defensive(w)
for i in range(init_evolving):
    Evolving(w)

for t in range(10000):
    w.free_food(10)
    w.conflict(5)
    w.update()

w.status()
w.evolvingPlot()  #This line adds a plot of evolving birds. Uncomment it when needed.
