#Kate Bohning
#Files and Strings assignment Week 8
import random

from listFunctions import *


#player 1
pcNum = random.randint(1, 3)

single_player(pcNum)
print(player_name(0) + " Chose " + player_choice(0))
print("Computer chose " + single_player(pcNum))

game_logic(single_player(pcNum), player_choice(0), player_name(0))

#player 2

pcNum = random.randint(1, 3)

single_player(pcNum)
print(player_name(1) + " Chose " + player_choice(1))
print("Computer chose " + single_player(pcNum))

game_logic(single_player(pcNum), player_choice(1), player_name(1))

#player 3

pcNum = random.randint(1, 3)

single_player(pcNum)
print(player_name(2) + " Chose " + player_choice(2))
print("Computer chose " + single_player(pcNum))

game_logic(single_player(pcNum), player_choice(2), player_name(2))

#player 4

pcNum = random.randint(1, 3)

single_player(pcNum)
print(player_name(3) + " Chose " + player_choice(3))
print("Computer chose " + single_player(pcNum))

game_logic(single_player(pcNum), player_choice(3), player_name(3))

#player 5

pcNum = random.randint(1, 3)

single_player(pcNum)
print(player_name(4) + " Chose " + player_choice(4))
print("Computer chose " + single_player(pcNum))

game_logic(single_player(pcNum), player_choice(4), player_name(4))