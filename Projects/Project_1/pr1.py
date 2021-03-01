import random
import math
import pr1testing
import numpy as np
random.seed()


def roll(): #function that rolls 1 6-sided die, returning an integer between 0 and 5
    return random.randint(0,5)

def play():
    player1 = input("Name of Player 1?")
    player2 = input("Name of Player 2?")
    score1 = 0
    score2 = 0
    last = False
    while True:
        print()
        print(player1 + ": " + str(score1) + "   " + player2 + ": " + str(score2))
        print('It is', player1 + "'s turn.")
        numDice = int(input("How many dice do you want to roll?"))
        diceTotal = 0
        diceString = ""
        i = numDice
        while i > 0:
            d = roll()
            diceTotal += d
            diceString = diceString + " "  + str(d)
            i = i-1
        print("Dice rolled: ", diceString)
        print("Total for this turn: ", str(diceTotal))
        score1 += diceTotal
        if score1 > 100 or last:
            break
        if numDice == 0:
            last = True
        print()
        print(player1 + ": " + str(score1) + "   " + player2 + ": " + str(score2))
        print('It is', player2 + "'s turn.")
        numDice = int(input("How many dice do you want to roll?"))
        diceTotal = 0
        diceString = ""
        i = numDice
        while i > 0:
            d = roll()
            diceTotal += d
            diceString = diceString + " "  + str(d)
            i = i-1
        print("Dice rolled: ", diceString)
        print("Total for this turn: ", str(diceTotal))
        score2 += diceTotal
        if score2 > 100 or last:
            break
        if numDice == 0:
            last = True
    print(player1 + ": " + str(score1) + "   " + player2 + ": " + str(score2))
    if score1 > 100:
        print(player2 + " wins.")
        return 2
    elif score2 > 100:
        print(player1 + " wins.")
        return 1
    elif score1 > score2:
        print(player1 + " wins.")
        return 1
    elif score2 > score1:
        print(player2 + " wins.")
        return 2
    else:
        print("Tie.")
        return 3

def player_input(s, o, final): #pass through as player if human to play
  return input(" Your score is: " +str(s) + "\n The other players score is: " + str(o) + "\n Final round is: " + str(final) + "\n Your input: ")

def on_start(player_1, player_2, player_print=False, print_score=False, print_how_many_dice=False):
  score_p_1 = 0
  score_p_2 = 0
  zero_die_p1 = False #Boolean that is passed through to mark a zero die being triggered
  zero_die_p2 = False #Boolean that is passed through to mark a zero die being triggered

  while score_p_1<101 and score_p_2 <101:
    #player one final round
    if player_print==True:
      print("Player Ones turn")
    p1_input = player_1(score_p_1, score_p_2, zero_die_p2) #player one input
    print("Player one is rolling " + str(p1_input) + " dice.")
    if int(p1_input)==0:
      zero_die_p1 = True #final round
    else:
      score_p_1 += sum(np.random.choice(6, int(p1_input)))
    if zero_die_p2==True:
      break
    if score_p_1>100:
      break
    if print_score==True:
      print("Player 1: "+ str(score_p_1) + "\nPlayer 2: " + str(score_p_2))

    if player_print==True:
      print("Player Twos turn")

    p2_input = player_2(score_p_2, score_p_1, zero_die_p1) #player two input
    print("Player two is rolling " + str(p2_input) + " dice.")
    if int(p2_input)==0:
      zero_die_p2 = True
    else:
      score_p_2 += sum(np.random.choice(6, int(p2_input)))
    if zero_die_p1==True: # issues with this function
      break
    if print_score==True:
      print("Player 1: "+ str(score_p_1) + "\nPlayer 2: " + str(score_p_2))
  """
  Game has concluded, prints out score
  """
  if print_score==True:
    print("FINAL SCORE")
    print("Player 1: "+ str(score_p_1) + "\nPlayer 2: " + str(score_p_2))
  if score_p_1>100:
    return "Player 2 wins."
  if score_p_2>100:
    return "Player 1 wins."
  if score_p_1>score_p_2:
    return "Player 1 wins."
  if score_p_1<score_p_2:
    return "Player 2 wins."
  if score_p_1==score_p_2:
    return "Tie."


def autoplayLoud(strat1, strat2):
    return on_start(strat1, strat2, player_print=True, print_score=True)

def autoplay(strat1, strat2):
    return on_start(strat1, strat2)

def manyGames(strat1, strat2, n):
    strat_1_first = [on_start(strat1, strat2) for x in range(n//2)]
    strat_1_wins = strat_1_first.count("Player 1 wins.")
    strat_2_wins = strat_1_first.count("Player 2 wins.")
    ties = strat_1_first.count("Tie")

    strat_2_first = [on_start(strat2, strat1) for x in range(n//2)]
    strat_1_wins += strat_2_first.count("Player 1 wins.")
    strat_2_wins += strat_2_first.count("Player 2 wins.")
    ties += strat_2_first.count("Tie")

    print("Player 1 wins: " + str(strat_1_wins))
    print("Player 2 wins: " + str(strat_2_wins))
    print("Ties: " + str(ties))


def sample1(myscore, theirscore, last):
    if myscore > theirscore:
        return 0
    else:
        return 12

def sample2(myscore, theirscore, last):
    if myscore<=50:
        return 30
    if 51<= myscore and myscore<80:
        return 10
    if myscore>80:
        return 0

def improve(strat1):
    def new_strat(myscore, theirscore, last):
        if myscore==100:
            return 0
        else:
            strat1

    return new_strat

def myStrategy(self, other, final): # Annie Get your gun (anything you can do I can do better)
  if self>=97 and final!=True: #in a low move position
    if other>=self:
        return 1
    else:
      return 0

  """
  The below simulates several possible rolling scenarios
  """
  simulation = []
  lower_bound = 1 # rolls at least one dice
  upper_bound = min([int((100-self)//2)+1, 40]) #rolls at most 45 dice
  trials = 200 # num sim throws ber num dice
  for x in range(lower_bound,upper_bound): #Rolls between
    holder = []
    for y in range(trials):
      holder.append(sum(np.random.choice(6, x)))
    simulation.append(holder)

  """
  The below selects number of dice for first round move
  """
  if self==0 or other==0: #First round moves
    if other!=0: #Moving second
      other_lead = other
      rolls_greater_than_other = [n for n, i in enumerate([np.percentile(x, 30) for x in simulation], lower_bound) if i>other_lead] #returns rolls that will likely exceed the other computer
      rolls_less_than_100 = [n for n, i in enumerate([np.percentile(x, 80) for x in simulation], lower_bound) if i<=100] #returns rols that will likely be less than 100
      possible_rolls = list(set(rolls_greater_than_other) & set(rolls_less_than_100)) #intersection of the two
      if possible_rolls!=[]:
        return int(np.percentile(possible_rolls, 35))
      else:
        rolls_less_than_100[-1]
    if other==0:
      rolls_less_than_100 = [n for n, i in enumerate([np.percentile(x, 90) for x in simulation], lower_bound) if i<=100] #Returns rolls that
      return int(np.percentile(rolls_less_than_100, 75)) #Returns a roll that doesn't exceed 100

  """
  The below selects number of dice if there is a final round
  """
  if final==True:
    if self>=other: #Is willing to tie, or just be ahead
      return 0
    if self<98 and self>95:
      return 1

    else:
      other_lead=other-self #How far ahead is the other player
      distance_hundred = 100-self #distance to 100
      rolls_greater_than_other = [n for n, i in enumerate([np.percentile(x, 30) for x in simulation], lower_bound) if i>other_lead] #returns rolls that will likely exceed the other computer 30% of the time
      rolls_less_than_100 = [n for n, i in enumerate([np.percentile(x, 80) for x in simulation], lower_bound) if i<=distance_hundred] #returns rolls that will likely be less than 100 80% of the time
      possible_rolls = list(set(rolls_greater_than_other) & set(rolls_less_than_100)) #intersection of the two lists (SET CONVERSION!!!)
      if possible_rolls==[] and rolls_less_than_100!=[]: #if No matching elements is
        return int((rolls_less_than_100[-1])) #50% chance of not exceeding
      elif rolls_less_than_100==[]: #no rolls less than 100, which would be odd
        return 1
      else:
        return int(np.percentile(possible_rolls, 80)) # 80th percentile recommended role

  """
  The below selects number of dice if the other person is ahead
  """
  if other>self:
    other_lead=other-self
    distance_hundred = 100-self
    rolls_greater_than_other = [n for n, i in enumerate([np.percentile(x, 30) for x in simulation], lower_bound) if i>other_lead] #returns rolls that will likely exceed the other computer
    rolls_less_than_100 = [n for n, i in enumerate([np.percentile(x, 80) for x in simulation], lower_bound) if i<distance_hundred] #returns rols that will likely be less than 100
    possible_rolls = list(set(rolls_greater_than_other) & set(rolls_less_than_100)) #intersection of the two
    if possible_rolls==[]: #No matching elements
      return 1 #50% chance of not exceeding
    else:
      return int(np.percentile(possible_rolls, 30)) # Roles barley above the other person

  """
  The below selects number of dice if ahead
  """
  if self>=other: # ahead of other
    good_idea_to_pass = False
    if good_idea_to_pass == True: #WIP, decides wheter to pass or not
      return 0
    else: #
      distance_hundred = 100-self
      rolls_less_than_100 = [n for n, i in enumerate([np.percentile(x, 75) for x in simulation], lower_bound) if i<distance_hundred]
      if rolls_less_than_100==[]:
        return 1
      else:
        return int(np.percentile(rolls_less_than_100, 20))