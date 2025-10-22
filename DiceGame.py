#Dice Game! Using random, roll two numbers between 1 and 6, calculate total
import random

die1 = random.randint(1, 6)
die2 = random.randint(1, 6)

total = die1 + die2

#Introduce rules. Require input from the user to continue
userContinue = input("Welcome to the Dice Game! Roll a 7, 11, or doubles to win, 12 is the jackpot! \nPress ENTER to start!")

#Print rolls and outcome
print("\nYou rolled a " + str(die1) + " and a " + str(die2) + ".")
print("Your total was " + str(total) + ".")

if die1 == die2:
    if die1 == 6 and die2 == 6:
        print("WOW! JACKPOT! Congratulations!")
    else:
        print("Sweet, you got double " + str(die1) + "'s! You win!")
elif total == 7 or total == 11:
    print("You win! :)")
else:
    print("Sorry, you lose. :(")