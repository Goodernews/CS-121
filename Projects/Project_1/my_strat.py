
import numpy as np
import math


def myStrategy(self, other, final):
  if self>=97: #in a low move position
    if other>=self:
        return 1
    else:
      return 0

  if final==False:
    if self==0 and other==0:
      return 25
    if self==0 and other!=0:
      return max([1, other*-0.04189018901890407+ 22.84545454545455])
    if self>=other:
      return max([1, round((self*-0.07454092348010295)+ (other*-8.964161722307962e-05)+7.618268398268405)])
#    if self==other:
#      return max([1, round((self*0.036525652565258235) + (other*-0.03652565256525485)+ 7.589090909090911)])
    if self<other:
      return max([1, round((self*-0.1928190466105245)+ (other*-0.04628227528636203)+ 22.081564744709773)])
      #return max([1, round((-0.9581150738781469*self)+ (other*-1.010174705275749) +(1.2681782459*self*other)+ ((self**2)*0.011103722990161546)+ ((other**2)*-0.0009494164955137774)+0.0009494164955137774)])
  if final==True:
    if self>=other: #Is willing to tie, or just be ahead
      return 0
    else:
      return max([1, round(self*-0.3815247647213692+other*0.08016703711187506+28.847965367965354)])




def agyg(self, other, final): # Annie Get your gun (anything you can do I can do better)
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
  trials = int(4000//upper_bound) # num sim throws ber num dice
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