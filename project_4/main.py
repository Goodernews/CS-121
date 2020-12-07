from __future__ import unicode_literals, print_function

##### Tuning

size_x = 25 #
size_y = 25 #
upload_game = "" # Upload a map

######### Import and setup
#!pip install snips-nlu
#!snips-nlu download en

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import scipy.stats as stats
import re
import sys
import random
import time
import os
import io
import json
from snips_nlu import SnipsNLUEngine
from snips_nlu.default_configs import CONFIG_EN
from pathlib import Path



logo = Path('project_4\logo.txt').read_text()
#print(logo)
gen_help = Path("project_4\help.txt").read_text()
#print(gen_help)
welcome = open('project_4\welcome.txt', "r").read()


with io.open("project_4\dataset.json") as f:
  dataset = json.load(f)
nlu_engine = SnipsNLUEngine(config=CONFIG_EN)
nlu_engine = nlu_engine.fit(dataset)

############# Custom classes

#from Character as Character
import funcs
import Layout
Layout = Layout.Layout
import Info
Info = Info.Info
import Store
import Character
Character = Character.Character
#################

funcs.hum_type(logo, speed = 550)

#Sets up game assuming no previous file
if upload_game=="":
  layout, x_loc, y_loc = funcs.gen_map(size_x, size_y)
  layout = Layout(layout)
  character = Character()
  info = Info(x_loc, y_loc) 
else: 
  pass
  #layout, character, info = funcs.open_game(upload_game)

if upload_game=="": # intro and tutorial
  print("\n\n\n")
  funcs.hum_type(welcome, speed=5000)
  input("Press return to Start ")

while True: 
  if character.health<=0:
    print("GAME OVER")
    print("You have run out of health and died")
    break
  
  print("--- \n\n\n")
  print("Character information:")
  character.display()

  print("--- \n\n")
  layout.display(info.x, info.y)
  user_input = funcs.parse(input("Enter command: "), nlu_engine)
  #print(user_input) #check parsed
  print("Location: " + str([info.x, info.y]))
  os.system('cls' if os.name == 'nt' else 'clear')
  if user_input is None:
    intent = None
  else:
    intent = user_input["intent"]
  
  
  if intent == "move":
    info, character, layout = funcs.move(info, character, layout, user_input)
  elif intent == "mine":
    funcs.mine(info, character, layout, user_input)
    info.rounds +=1
  elif intent == "help":
    print(gen_help)
    input("Press return to close")
  elif intent == "sell":
    print("Selling not implemented")
    Store.sell(character, user_input, hash(str(layout.df.to_numpy().tolist()))+info.rounds) #uses current round and map to fix seed
  elif intent == "buy":
    print("Buying not implemented")
    Store.buy(character, user_input, hash(str(layout.df.to_numpy().tolist()))+info.rounds)
  
  elif intent == "save":
    print("Not impelemented completley, but there is a regex example")
    while True:
      file_out = input("Input a file path or return to exit")
      if file_out== "":
        break
      if bool(re.search(r".+(\.csv)$", file_out)):
        #save_game(file_out, layout, character, info)
        print("Game saved")
        break
      else:
        print("Make sure that you input is a valid csv file")

  elif intent == "end":
    # Might need to confirm, make intent
    end_input = input("Press return to close game, or enter another key then return to continue")
    if end_input=="":
      print("Ending game")
      break
    else:
      funcs.hum_type("Continuing game...")
  elif intent == "open":
    if user_input["pullUp"]=="map":
      print("Not impemented")
    elif user_input["pullUp"]=="inventory":
      character.print_inventory()
    elif user_input["pullUp"]=="store":
      Store.display(hash(str(layout.df.to_numpy().tolist()))+info.rounds)
    elif user_input["pullUp"]=="stats":
      info.display()
    else:
      print("Please specify if you want to open: map, inventory, store, or stats")
  elif intent == "drop":
    funcs.drop(layout,character, info, user_input)
  elif intent == "pickup":
    funcs.pickup(layout,character, info, user_input)
  elif intent == "eat":
    character.eat(user_input)
  elif intent == "equip":
    character.equip(user_input)
  elif intent == "heal":
    character.heal(user_input)
  else:
    print("Could not execute command")
