import random

def game_logic(pcNum, list_player, player_name):
    '''This function requires two player inputs and returns a winner'''
    if pcNum == "rock" and list_player == "paper":
        print(player_name + " wins!")
    elif pcNum == "rock" and list_player == "scissors":
        print(player_name + " wins!")
    elif pcNum == "paper" and list_player == "rock":
        print("Computer wins!")
    elif pcNum == "paper" and list_player == "scissors":
        print(player_name + " wins!")
    elif pcNum == "scissors" and list_player == "rock":
        print("Computer wins!")
    elif pcNum == "scissors" and list_player == "paper":
        print("Computer wins!")
    else:
        print("It's a tie!")

def player_choice(x:int):
    open('namesfile.txt', "r")
    namesfile = open("namesfile.txt", "r")

    playerChoice = namesfile.readlines()[x]
    namesfile.close()

    playerChoice = playerChoice.split()
    # playerChoice is now an array of ['name', '-', and 'choice']
    return playerChoice[2]

def player_name(x:int):
    open('namesfile.txt', "r")
    namesfile = open("namesfile.txt", "r")

    playerName = namesfile.readlines()[x]
    namesfile.close()

    playerName = playerName.split()
    #playerName is now an array of ['name', '-', and 'choice']
    return playerName[0]

def single_player(rand_num):
    '''This function inputs a number from 1-3 and assigns it a string'''
    global player_2
    if (rand_num == 1):
        player_2 = "rock"

    elif (rand_num == 2):
        player_2 = "paper"

    else:
        player_2 = "scissors"
    return(player_2)
