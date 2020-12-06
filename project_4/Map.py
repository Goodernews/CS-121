class Map:
  def __init__(self,
               df):
    self.df = df
    self.max_x = max(df.columns)
    self.max_y = max(df.index)

  def display(self, x, y):
    valid_directions = ["North", "East", "South", "West"]
    if not self.path_clear(x, y-1):
      valid_directions.remove("North")
    if not self.path_clear(x, y+1):
      valid_directions.remove("South")
    if not self.path_clear(x+1, y):
      valid_directions.remove("East")
    if not self.path_clear(x-1, y):
      valid_directions.remove("West")
    print("You can travel: ", valid_directions)
    
    if self.items_to_pickup(x,y)==[]:
      print("Nothing to pickup")
    else:
      items = self.unique_items(x,y)
      if len(items)>1:
        print("There are several items you can pickup: ")
      else:
        print("There is one thing you can pick up: ")
      counts = self.count_items(x,y)
      for z in range(len(items)):
        if counts[z]>1:
          print(items[z] + " X " + str(counts[z]))
        else:
          print(items[z])

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
    return list(set(self.df[x][y]["items"]))


  def count_items(self, x,y):
    return [self.df[x][y]["items"].count(y) for z in self.unique_items(x,y)]

  def items_to_pickup(self, x, y):
    return self.df[x][y]["items"]


