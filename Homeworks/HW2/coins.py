def coins(x):
    big_coins = x//66
    small_coins = (x-(66*big_coins))//6
    pennies= x-((big_coins*66)+(small_coins*6))
    return big_coins+small_coins+pennies