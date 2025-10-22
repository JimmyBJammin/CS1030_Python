#Call random, generate computer choice with 1-3 and equate to an option
import random

choice = random.randint(1,3)

if choice == 1:
    computer = 'r'
elif choice == 2:
    computer = 'p'
else:
    computer = 's'

#Introduce rules, collect user input
print("Let's play rock, paper, scissors!")
player = input("Choose either rock (r), paper (p), or scissors (s)")

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