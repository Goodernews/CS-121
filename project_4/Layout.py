class Layout:
  def __init__(self,
               df):
    self.df = df
    self.max_x = max(df.columns)
    self.max_y = max(df.index)

  def walk_valid(self, x, y):
    valid_directions = ["North", "East", "South", "West"]
    if not self.path_clear(x, y-1):
      valid_directions.remove("North")
    if not self.path_clear(x, y+1):
      valid_directions.remove("South")
    if not self.path_clear(x+1, y):
      valid_directions.remove("East")
    if not self.path_clear(x-1, y):
      valid_directions.remove("West")
    return valid_directions

  def mine_valid(self, x, y):
    pass

  def display(self, x, y):
    valid_directions = ["North", "East", "South", "West"]
    if not self.path_clear(x+1, y):
      valid_directions.remove("North")
    if not self.path_clear(x-1, y):
      valid_directions.remove("South")
    if not self.path_clear(x, y+1):
      valid_directions.remove("East")
    if not self.path_clear(x, y-1):
      valid_directions.remove("West")
  
    
    print("You can travel: ", valid_directions)
    print("You can mine: ")
    
    if self.items_to_pickup(x,y)==[]:
      print("Nothing to pickup")
    else:
      items = self.unique_items(x,y)
      count = self.count_items(x,y)
      if sum(count)>1:
        print("There are several items you can pickup: ")
      else:
        print("There is one thing you can pick up: ")
      for z in range(len(items)):
        if count[z]>1:
          print(items[z].capitalize() + " (" + str(count[z]) + ")")
        else:
          print(items[z].capitalize())

  def place(self, x, y, item): # put item down
    self.df[x][y]["items"].append(item)

  def delete_item(self, x, y, item):
    self.df[x][y]["items"].remove(item)


  def path_clear(self, x, y):
    if y>self.max_y or x>self.max_x: #out of range
      return False
    if y<0 or x<0: #out of range
      return False
    return self.df[x][y]["walkable"] #checks squeate

  def unique_items(self, x,y):
    lst = []
    for item in self.df[x][y]["items"]:
      if type(item) is list:
        lst.append(item[0])
      else:
        lst.append(item)
    return list(set(lst))


  def count_items(self, x,y):
    return [self.df[x][y]["items"].count(z) for z in self.unique_items(x,y)]

  def items_to_pickup(self, x, y):
    return self.df[x][y]["items"]


