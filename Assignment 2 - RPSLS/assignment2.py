"""
This is a program used to simulate the popular "RPSLS" game (rock-paper-scissors-lizard-Spock) from the
TV-show "The Big Bang Theory."
"""
def choice_to_number(choice):
    """
    This function converts each possible move in RPSLS (rock, paper, scissors, lizard, Spock) into a 
    numerical value (0, 1, 2, 3, 4) to make it easier for the program to "play" the game. If the given
    move is not accepted by the game, it will return -1.
    """
    if choice == 'rock':
        return 0
    elif choice == 'Spock':
        return 1
    elif choice == 'paper':
        return 2
    elif choice == 'lizard':
        return 3
    elif choice == 'scissors':
        return 4
    else:
        return -1

def number_to_name(num):
    """
    This function converts each numerical value (0, 1, 2, 3, 4) back into its corresponding move in 
    RPSLS (rock, paper, scissors, lizard, Spock).
    """
    if num == 0:
        return 'rock'
    elif num == 1:
        return 'Spock'
    elif num == 2:
        return 'paper'
    elif num == 3:
        return 'lizard'
    elif num == 4:
        return 'scissors'

#The following was just my work to try and find the mathematical relationship between RPSLS moves.
#-rock 0
#rock tie 0-0 = 0
#Spock lose 0-1 = -1
#paper lose 0-2 = -2
#lizard win 0-3 = -3
#scissors win 0-4 = -4
#
#-Spock 1
#rock win 1-0 = 1
#Spock tie 1-1 = 0
#paper lose 1-2 = -1
#lizard lose 1-3 = -2
#scissors win 1-4 = -3
#
#-paper 2
#rock win 2-0 = 2
#Spock win 2-1 = 1
#paper tie 2-2 = 0
#lizard lose 2-3 = -1
#scissors lose 2-4 = -2
#
#-lizard 3
#rock lose 3-0 = 3
#Spock win 3-1 = 2
#paper win 3-2 = 1
#lizard tie 3-3 = 0
#scissors lose 3-4 = -1
#
#-scissors 4
#rock lose 4-0 = 4
#Spock lose 4-1 = 3
#paper win 4-2 = 2
#lizard win 4-3 = 1
#scissors tie 4-4 = 0

def winner(player, computer):
    """
    The following function will decide the winner (or determine if there is a tie) between two RPSLS
    moves.
    """
    if (player - computer) % 5 == 0:
        return 'Player and computer tie.'
    elif (player - computer) % 5 == 1:
        return 'Player wins!'
    elif (player - computer) % 5 == 2:
        return 'Player wins!'
    elif (player - computer) % 5 == 3:
        return 'Computer wins!'
    elif (player - computer) % 5 == 4:
        return 'Computer wins!'
    else:
        return 'Error. Please try again.'

import random
#The random module is imported to select a random computer move.
def rpsls(choice):
    """
    This function will take a string 'choice' and simulate a round of RPSLS. The computer's choice 
    is randomized and is not dependent on the decision of the human player. This function controls
    the actual gameplay.
    """
    comp_choice_num = random.randrange(0,5,1)
    player_choice_num = choice_to_number(choice)
    player_str = ' '
    computer_str = number_to_name(comp_choice_num)
    if player_choice_num == 0:
        player_str = 'rock'
    elif player_choice_num == 1:
        player_str = 'Spock'
    elif player_choice_num == 2:
        player_str = 'paper'
    elif player_choice_num == 3:
        player_str = 'lizard'
    elif player_choice_num == 4:
        player_str = 'scissors'
    else:
        return 'Player chooses ' + choice + '.  Improper player choice.'

    return 'Player chooses ' + player_str + '.  Computer chooses ' + computer_str + '.  ' + winner(player_choice_num,comp_choice_num)

# The following are some sample tests.  Uncomment to use.
#print rpsls("rock")
#print rpsls("paper")
#print rpsls("scissors")
#print rpsls("lizard")
#print rpsls("Spock")
#print rpsls("rocket")