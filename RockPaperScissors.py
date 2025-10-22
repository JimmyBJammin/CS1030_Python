#Import random for computer choice, define variables
import random

pChoice = str("")
player = str("")
cChoice = int(0)
computer = str("")
playAgain = str("")
outcome = str("")
wins = int(0)
draws = int(0)
loses = int(0)

#Introduce game, set loop-check variable, playAgain to 'y' for true
print("Let's play rock, paper, scissors!")

playAgain = "y"

#Will replay as long as user chooses to at the end of the loop
while playAgain == 'y' or playAgain == 'Y':
    pChoice = input("Choose either rock (r), paper (p), or scissors (s) ->")

    #Will require the player to choose a valid choice
    while not(pChoice == 'r' or pChoice == 'p' or pChoice == 's'):
        print("Invalid choice. Try again.\n")
        pChoice = input("Choose either rock (r), paper (p), or scissors (s) ->")
        
    #Will translate the computer and player choices to ASCII versions and print
    if pChoice == 'r':
        player = '()'
    elif pChoice == 'p':
        player = '__'
    else:
        player = '>8'

    cChoice = random.randint(1,3)

    if cChoice == 1:
        computer = '()'
    elif cChoice == 2:
        computer = '__'
    else:
        computer = '>8'

    print("Computer vs. Player")
    print("   " + computer + "          " + player + "\n")

    #Calculate outcome and count wins/draws/loses
    if player == computer:
        print("Draw!\n")
        draws += 1
    elif player == '()':
        if computer == '>8':
            print("Rock smashes scissors. You win!\n")
            wins += 1
        elif computer == '__':
            print("Paper covers rock. You lose! :(\n")
            loses += 1
    elif player == '__':
        if computer == '()':
            print("Paper covers rock. You win!\n")
            wins += 1
        elif computer == '>8':
            print("Scissors cut paper. You lose! :(\n")
            loses += 1
    elif player == '>8':
        if computer == '__':
            print("Scissors cut paper. You win!\n")
            wins += 1
        elif computer == '()':
            print("Rock smashes scissors. You lose! :(\n")
            loses =+ 1


    print("Wins/Draws/Loses")
    print(str(wins) + "/" + str(draws) + "/" + str(loses) + "\n")

    #Will end the loop if the user enters anything other than 'y' or 'Y'
    playAgain = input("Do you want to play again? y/n -> ")
    print()
"""
    #If user doesn't pick 'r', 'p', 's' - end, otherwise, output outcome
    if not(player == 'r' or player == 'p' or player == 's'):
        print("Sorry, that wasn't one of the valid choices. Choose 'r', 'p', or 's' and try again later.")
    elif computer == player:
        print("DRAW!")
    elif computer == 'r':
        if player == 'p':
            print("Paper covers rock. You win!")
        else:
            print("Rock smashes scissors. Sorry, you lose!")
    elif computer == 'p':
        if player == 'r':
            print("Paper covers rock. Sorry, you lose!")
        else:
            print("Scissors cut paper. You win!")
    elif computer == 's':
        if player == 'r':
            print("Rock smashes scissors. You win!")
        else:
            print("Scissors cut paper. Sorry, you lose!")

"""