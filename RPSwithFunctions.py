#Kate Bohning
#RockPaperScissors with functions

import random
import turtle
import time

from Functions import *
#imports all functions from file

break_loop = False
tries = 3
pcNum = random.randint(1, 3)

player_1 = input("Player 1, Please enter rock paper or scissors: ")
data_validation(player_1)
single_player(pcNum)
print("Computer chose "+ single_player(pcNum))

game_logic(player_1,single_player(pcNum))