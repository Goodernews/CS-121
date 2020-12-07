import time
import random
import numpy as np
import pandas as pd
import scipy.stats as stats




break_items = ["apple"]
mine_items = ["basic pick axe"]

sellable = ["apple", "canned bread", "gold"]

mineable = ["diamond", "gold", "silver" "iron", "cobble", "coal", None] 
mine_chances = [0.02, 0.03, 0.04, 0.05, 0.2, 0.1, 0.66]

def mine(info, character, layout, parsed):
  pass

def open_game(file_location):
  pass

def move(info, character, layout, parsed):
  x = info.x
  y = info.y
  new_loc = [x,y]
  move_directions = layout.walk_valid(x, y)
  direct_move = parsed["direction"]
  if direct_move.capitalize() not in move_directions:
    print("You cannot move in that direction")
    return info, character, layout
  directions = ["north", "east", "south", "west"]
  direction_trans = [[1,0], [0,1], [-1,0], [0,-1]]
  transformation = direction_trans[directions.index(parsed["direction"])]
  if "steps" not in parsed.keys():
    steps = 1
  else:
    steps = parsed["steps"]
  for z in range(1, 1+steps):
    new_loc = [sum(a) for a in zip(new_loc, transformation)]
    if layout.path_clear(new_loc[0],new_loc[1]):
      info.x = new_loc[0]
      info.y = new_loc[1]
    else:
      print("Only moved: " + str(z) + " steps.")
      info.steps += z
      info.rounds += 1
      new_loc = [new_loc[a] - transformation[a] for a in range(len(new_loc))]
      info.x = new_loc[0]
      info.y = new_loc[1]
      return info, character, layout
  print("Moved " + parsed["direction"] + " "+ str(steps) + " steps")
  info.x = new_loc[0]
  info.y = new_loc[1]
  info.steps += z
  info.rounds += 1
  return info, character, layout

  

def hum_type(t, speed=150):
  for l in t:
    print(l, end='')
    time.sleep(random.random()*10.0/speed)
  print('')

def drop(layout, character, info, parsed):
  x = info.x
  y = info.y #need position
  if "inventNum" in parsed.keys(): #dropping by inventory number
    inventory_position = parsed["inventNum"]
    if inventory_position>len(character.unique_inventory()): #out of range
      print("There isn't a " + str(inventory_position) + "th item in your inventory")
    else:
      item = character.unique_inventory()[inventory_position-1]
      layout.place(x, y, item)
      print("Dropping: " + item)

  elif "item" in parsed.keys(): #drop by item name 
    item = parsed["item"]
    if bool(set(character.unique_inventory()) & set([item])): # item in inventory
      if "countItems" in parsed.keys(): #user wants to eat more than one
        num_item = character.count_items()[character.unique_inventory().index(item)]
        num_drop = parsed["countItems"]
        if num_item<num_drop: # User asks to eat more than in inventory
          print("You don't have ", str(num_drop), " in your inventory.")
          print("Dropping ", str(num_item), " instead.")
          num_drop = num_item
        for _ in range(num_drop):
          character.delete_item(item)
          layout.place(x, y, item)
      else: # only drop one
        character.delete_item(item)
        layout.place(x, y, item)
        print("Dropping: " + item)
      if item == character.equipped:
        if character.inventory !=[]:
          character.equipped = character.inventory[0]
        else:
          character.equipped = None
    else:
      print("You do not have a " + str(item))

  else: #Drop equipped item
    if len(character.unique_inventory())!=0:
      item = character.equipped
      if type(item) is list:
        print("Dropped: ", item[0])
      else:
        print("Dropped: ", item)
      character.delete_item(item)
      layout.place(x, y, item)

      if character.inventory==[]: #if afterwards no more items
        character.equipped = None
      else:
        character.equipped= character.inventory[0]
    else:
      print("Your inventory is already cleared")


def pickup(layout, character, info, parsed):
  x = info.x
  y = info.y
  grabable = layout.items_to_pickup(x, y)
  if grabable==[]:
    print("There is nothing to pick up")
  elif len(character.inventory)==character.max_inventory:
    print("You can't pick up anything else")
  elif "item" in parsed.keys(): #pickup by name
    item = parsed["item"]
    if item not in grabable:
      print("There is no " +  str(item) + " on the ground")
    else:
      if "countItems" in parsed.keys(): #user wants to pick up more than one
        num_space = character.max_inventory - len(character.inventory)
        num_pickup = parsed["countItems"]
        if num_space<num_pickup: # User asks to pick up more than space
          print("You don't have space for" + str(num_pickup) + " items in your inventory.")
          print("Picking up ", str(num_space), " instead.")
          num_pickup = num_space
        for _ in range(num_pickup):
          character.add_item(item)
          layout.delete_item(x, y, item)
      else:
        layout.delete_item(x, y, item)
        character.add_item(item)


  else: #pickup first item
    if "countItems" not in parsed.keys():
      item = grabable[0]
      layout.delete_item(x, y, item)
      character.add_item(item)
      print("Picked up: " + str(item))
    else: #pickup more than one
      num_space = character.max_inventory - len(character.inventory)
      num_pickup = parsed["countItems"]
      if num_space<num_pickup: # User asks to pick up more than space
        print("You don't have space for" + str(num_pickup) + " items in your inventory.")
        print("Picking up " + str(num_space) + " items instead.")
        num_pickup = num_space
      for _ in range(num_pickup):
        item = grabable[0] 
        character.delete_item(item)
        layout.place(x, y, item)
        
#@title Helper functions

def parse(text, nlu_engine): #parses user input 
  parsing = nlu_engine.parse(text) #clean string
  intent = parsing["intent"]["intentName"]
  entities = [x["slotName"] for x in parsing["slots"]]
  values = [y["value"]["value"] for y in parsing["slots"]]
  combined = dict(zip(entities + ["intent"], values + [intent])) 
  if "countItems" in combined.keys():# check if int item in dict
    if combined["countItems"].is_integer():
      combined["countItems"] = int(combined["countItems"])
    else:
      print("Please give an interger value when specifying a count.")
      return
  if "inventNum" in combined.keys():# check if int item in dict
    if combined["inventNum"].is_integer():
      combined["inventNum"] = int(combined["inventNum"])
    else:
      print("Please give an interger value when specifying an inventory number.")
      return
  if "steps" in combined.keys():# check if int item in dict
    if combined["steps"].is_integer():
      combined["steps"] = int(combined["steps"])
    else:
      print("Please give an interger value when specifying the number of steps to walk.")
      return
  if "repeats" in combined.keys():# check if int item in dict
    if combined["repeats"].is_integer():
      combined["repeats"] = int(combined["repeats"])
    else:
      print("Please give an interger value when specifying the number of steps to walk.")
      return

  if intent==None: #nothing parsed
    print("Intent not recognized")
    
  elif intent=="move":
    if "direction" in entities:
      return combined
    else: # no direction specified
      print("Please specify a direction")
  elif intent =="open":
    if "pullUp" in entities:
      return combined
    else: # nothing requested to display
      print("Please specify what you would like to display")
  elif intent =="buy":
    if "item" in entities:
      return combined
    else: # nothing to buy 
      print("Please specify what you would like to buy")
  else:
    return combined



def norm_rand(lower,
              upper, 
              mean, 
              std):
  X = stats.truncnorm(
  (lower - mean) / std, (upper - mean) / std, loc=mean, scale=std)
  return X.rvs(1)[0]

#@title Generate map

def clear_path(layout, loc, seen=False):
  x, y = loc[0], loc[1]
  layout[x][y]["health"] = 0
  layout[x][y]["walkable"] = True
  layout[x][y]["Seen"] = seen
  return layout


def gen_map(size_x, size_y):
  layout = pd.DataFrame(columns=list(range(size_x)))
  for i in range(size_y):
    layout.loc[i] = [{"seen":False, "walkable":False, "items":[], "health":100, "damage":0}]*size_x
  # blank map created

  #choose start position
  squares = size_x * size_y
  x_loc = int(norm_rand(0,size_x, size_x//2, size_x/10))
  y_loc = int(norm_rand(0,size_y, size_y//2, size_y/10))

  #tunnel out clearing
  layout = clear_path(layout, [x_loc, y_loc])
  dig_position = [x_loc, y_loc]
  cleared = 0
  want_cleared = int((squares**0.5)/2.5)
  directions = ["n", "e", "s", "w"]
  direction_trans = [[1,0], [0,1], [-1,0], [0,-1]]
  while cleared<want_cleared:
    dig_remaining = want_cleared-cleared
    direction_dig = random.choice(directions)
    dig_amount = int(norm_rand(0,max([1, dig_remaining]), (dig_remaining**0.5)//1.5, dig_remaining/10))
    for _ in range(max([1, dig_amount])):
      new_loc = [sum(x) for x in zip(dig_position, direction_trans[directions.index(direction_dig)])]
      if new_loc[0] in range(size_x) and new_loc[1] in range(size_y):
        dig_position = new_loc
        layout = clear_path(layout, dig_position)
        cleared +=1
      else:
        break
  
  random_drop_num = int(norm_rand(0,squares, (squares**0.5)//6, (squares**0.5)//15))
  random_drop_items = ["apple", "diamond", "bandaid", "iron", "coal", "cobble"]
  random_drop_freqs = [0.2, 0.01, 0.2, 0.1, 0.05, 0.44]
  for _ in range(random_drop_num):
    rand_item = np.random.choice(random_drop_items, p = random_drop_freqs)
    rand_x = random.randint(0, size_x-1)
    rand_y = random.randint(0, size_y-1)
    layout[rand_x][rand_y]["items"].append(rand_item) 


  return layout, x_loc, y_loc

