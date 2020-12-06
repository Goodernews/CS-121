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





from __future__ import unicode_literals, print_function

#!wget 'https://raw.githubusercontent.com/Goodernews/CS-121/main/project_4/parser.yaml'

#!wget https://raw.githubusercontent.com/Goodernews/CS-121/main/project_4/logo.txt
logo = open("logo.txt", "r").read()
#!wget https://raw.githubusercontent.com/Goodernews/CS-121/main/project_4/tutorial.txt
tutorial = open("tutorial.txt", "r").read()
#!wget https://raw.githubusercontent.com/Goodernews/CS-121/main/project_4/help.txt
gen_help = open("help.txt", "r").read()


!snips-nlu generate-dataset en parser.yaml > dataset.json

with io.open("dataset.json") as f:
  dataset = json.load(f)
nlu_engine = SnipsNLUEngine(config=CONFIG_EN)
nlu_engine = nlu_engine.fit(dataset)

############# Custom classes



#################

hum_type(logo, speed = 550)

#Sets up game assuming no previous file
if upload_game=="":
  map, x_loc, y_loc = gen_map(size_x, size_y)
  map = Map(map)
  character = Character()
  info = Info(x_loc, y_loc) 
else: 
  map, character, info = open_game(upload_game)

if upload_game=="": # intro and tutorial
    hum_type(tutorial, speed=500)
    input()

while True: 
  if character.health<=0:
    print("GAME OVER")
    print("You have run out of health and died")
    break
  
  print("--- \n\n\n")
  print("Character information:")
  character.display()

  print("--- \n\n")
  map.display(info.x, info.y)

  user_input = parse(input("Enter command: "))
  os.system('cls' if os.name == 'nt' else 'clear')
  if user_input is None:
    intent = None
  else:
    intent = user_input["intent"]
  
  
  if intent == "move":
    if not check_move(intent[1:]): #move is invalid
      print("You cannot move ", intent[1], ". Check ___")
    else: # move valid
      #move
      info.round +=1
  elif intent == "mine":
    mine()
      info.round +=1
  elif intent == "help":
    print(gen_help)
  elif intent == "sell":
    Store.sell(character, user_input, hash(str(map.df.to_numpy().tolist()))+info.round) #uses current round and map to fix seed
  elif intent == "buy":
    Store.buy(character, user_input, hash(str(map.df.to_numpy().tolist()))+info.round)
  
  elif intent == "save":
    while True:
      file_out = input("Input a file path or return to exit")
      if file_out== "":
        break
      if bool(re.search(".+(\.csv)$", file_out)):
        save_game(file_out, map, character, info)
        print("Game saved")
        break
      else:
        print("Make sure that you input is a valid csv file")

  elif intent == "end":
    # Might need to confirm, make intent
    print("Ending game")
    break
  elif intent == "open":
    if user_input["pullUp"]=="map":
      pass
    elif user_input["pullUp"]=="inventory":
      character.print_inventory()
    elif user_input["pullUp"]=="store":
      Store.display(hash(str(map.df.to_numpy().tolist()))+info.round)
    elif user_input["pullUp"]=="stats":
      info.display()
    else:
      print("Please specify if you want to open: map, inventory, store, or stats")
  elif intent == "drop":
    drop(map,character, info, user_input)
  elif intent == "eat":
    character.eat(user_input)
  elif intent == "equip":
    character.equip(user_input)
  elif intent == "heal":
    character.heal(user_input)
  else:
    print("Could not execute command")
