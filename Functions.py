import turtle
import random
import time

def turtle_H():
    '''this function draws an H on the screen if you win against the computer'''
    window = turtle.Screen()
    tim = turtle.Turtle()

    tim.color('blue')
    tim.pensize(8)

    tim.right(90)
    tim.forward(100)
        # tim.penup(50)
    tim.left(180)
    tim.forward(50)
    tim.right(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(50)
    tim.right(180)
    tim.forward(100)
    sleep(10)
    window.mainloop()

def turtle_C():
    window = turtle.Screen()
    tim = turtle.Turtle()
    tim.color('red')
    tim.pensize(8)
    turtle.circle(120, -200)

    window.mainloop()

def turtle_tie():
    window = turtle.Screen()
    tim = turtle.Turtle()
    tim.draw_star(80)
    sleep(5)
    window.mainloop()

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

def data_validation(answer):
    '''This function will validate rock paper scissors input, and terminate if correct answer
    is not given within 5 tries'''
    break_loop = False
    tries = 5
    while break_loop == False:
        tries = tries - 1
        if answer == "rock" or answer == "scissors" or answer == "paper" or tries == 0:
            break_loop = True
            print("Player 1 chose " + answer)
        else:
            print("that is not a valid input! ")
            answer = input("Please enter rock paper or scissors: ")


def game_logic(player_1, player_2):
    '''This function requires two player inputs and returns a winner'''

    if (player_1 == "rock" and player_2 == "paper"):
        print("Computer wins!")
        turtle_C()
    elif (player_1 == "rock" and player_2 == "scissors"):
        print("Human wins!")
        turtle_H()
    elif (player_1 == "paper" and player_2 == "rock"):
        print("Human wins!")
        turtle_H()
    elif (player_1 == "paper" and player_2 == "scissors"):
        print("Computer wins!")
        turtle_C()
    elif (player_1 == "scissors" and player_2 == "rock"):
        print("Computer wins!")
        turtle_C()
    elif(player_1 == "scissors" and player_2 == "paper"):
        print("Human wins!")
        turtle_H()
    else:
        print("It's a Tie!")


'''this function takes an integer referring to index line of namesfile.txt
and creates a new array of just that line. Returns player name'''
def player_name(x:int):
    open('namesfile.txt', "r")
    namesfile = open("namesfile.txt", "r")

    playerName = namesfile.readlines()[x]
    namesfile.close()

    playerName = playerName.split()
    #playerName is now an array of ['name', '-', and 'choice']
    return playerName[0]




'''this function takes an integer referring to index line of namesfile.txt
and creates a new array of just that line. Returns player name'''
def player_choice(x:int):
    open('namesfile.txt', "r")
    namesfile = open("namesfile.txt", "r")

    playerChoice = namesfile.readlines()[x]
    namesfile.close()

    playerChoice = playerChoice.split()
    # playerChoice is now an array of ['name', '-', and 'choice']
    return playerChoice[2]

'''this function will: 
    * open namesfile.txt
    * check for file with try/except
    * use len() function to find out how long each line is'''


def phase_one():
    open('namesfile.txt', "r")
    namesfile = open("namesfile.txt", "r")



    namesfile.close()

