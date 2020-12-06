edible = ["apple", "canned bread"]
energy_item = [5, 10]

healing = ["band aid", "inhaler"]
healing_item = [5, 10]

eatable = lambda x : x in edible


class Character:
  def __init__(self, 
              max_health = 100, 
              health = 100,
              max_energy = 100,
              energy = 100,
              inventory = [["basic pick axe", 0],
                            "apple",
                            "apple",
                            "apple",
                            "canned bread",
                            "band aid"],
              money = 25, 
              equipped = None
              ):
    self.max_energy = max_energy
    self.max_health = max_health
    self.health = health
    self.energy = energy
    self.inventory = inventory
    self.money = money
    self.max_inventory = 25
    if equipped is None:
      self.equipped = inventory[0]
    else:
      self.equipped = equipped

  def save(self):
    save_dict = dict()
    save_dict["max_health"] = self.max_health
    save_dict["health"] = self.health
    save_dict["max_energy"] = self.max_energy
    save_dict["inventory"] = self.inventory
    save_dict["money"] = self.money
    save_dict["max_health"] = self.max_health

    return save_dict

  def heal(self, parsed):
    pass

  def display(self):
    print("Health: " + str(self.health) + "/" + str(self.max_health))
    filled_bars = round(self.health/self.max_health*20)
    print("[" + "█"*filled_bars + "-"*(20-filled_bars)+ "]")
    print("Energy: " + str(self.energy) + "/" + str(self.max_energy))
    filled_bars = round(self.energy/self.max_energy*20)
    print("[" + "█"*filled_bars + "-"*(20-filled_bars)+ "]")
    if self.equipped is not None:
      if type (self.equipped) is list:
        print("Currently equipped: " + self.equipped[0])
      else:
        print("Currently equipped: " + self.equipped)
    else:
      print("You haven't equipped anything")

  def print_inventory(self):
    if self.unique_inventory()==[]:
      print("You don't have anything in your inventory")
    else:
      print("In your inventory you have: ")
      print_inv_items = self.unique_inventory()
      counts = self.count_items()
      for x in range(len(print_inv_items)):
        if counts[x]>1: # more than one of an item
          if type(print_inv_items[x]) is list:
            print(print_inv_items[x][0] + " X " + str(counts[x]))
          else:
            print(print_inv_items[x] + " X " + str(counts[x]))
        else:
          if type(print_inv_items[x]) is list:
            print(print_inv_items[x])
          else:
            print(print_inv_items[x])


  def unique_inventory(self):
    return list(set([x[0] if type(x)==list else x for x in self.inventory]))

  def count_items(self):
    invent_items = [x[0] if type(x)==list else x for x in self.inventory]
    return [invent_items.count(y) for y in list(set(invent_items))]

  def in_inventory(self, item):
    return bool(set(self.unique_inventory()) & set([item]))

  def add_item(self, item):
    self.inventory.append(item)

  def delete_item(self, item):
    self.inventory.remove(item)

  def eat_item(self, item): #eats one checked item

    self.delete_item(item)
    self.energy += energy_item[edible.index(item)]
    if self.energy > self.max_energy:
      self.energy = self.max_energy

  def equip(self, parsed):
    if "item" not in parsed.keys():
      print("Item has not been specified")
    else:
      if self.in_inventory(parsed["item"]):
        pass
      else:
        print("That item is not in your inventory") 


  def eat(self, parsed):
    if self.energy == self.max_energy:
      print("Your energy is already maxxed out")
      return
    if bool(set(self.unique_inventory()) & set(edible)): #check if edible foods in inventory
      if "item" in parsed.keys(): #check if eat by specific item
        item = parsed["item"]
        if eatable(item): # item is edible
          if "countItems" in parsed.keys(): #user wants to eat more than one
            num_item = self.count_items()[self.unique_inventory().index(item)]
            num_eat = parsed["countItems"]
            if num_item<num_eat: # User asks to eat more than in inventory
              print("You don't have ", str(num_eat), " in your inventory.")
              print("Eating ", str(num_item), " instead.")
              num_eat = num_item
            for x in range(int(num_eat)):
              self.eat_item(item)
            print("Ate " + str(x) + " " + str(item))
          else:
            self.eat_item(item)
            print("Ate 1 " + str(item))
        else:
          print("That won't taste too good")
      elif "inventNum" in parsed.keys(): #check if eat by inventory number 
        inventory_position = parsed["inventNum"]
        if inventory_position>len(self.unique_inventory()):
          print("That isn't a ", str(inventory_position), "th item in your inventory")
        else:
          item = self.unique_inventory()[inventory_position-1]
          if eatable(item): # item is edible
            self.eat_item(item)
            print("Ate 1 " + str(item))
          else:
            print("Hmmm, you can't eat a", item) 
      else: #eat first edible thing
        item = list(set(self.unique_inventory())&set(edible))[0]
        self.eat_item(item)
        print("Ate 1 " + str(item))
    else:
      print("There's nothing edible in your inventory")
