#Password Generator
import random

#List of valid characters for the password
char = ['1', '2','3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Ask user for how many passwords they need and how long the passwords should be
amountPasswords = int(input("How many passwords do you need? "))
amountCharacters = int(input("How long does it need to be? "))

#Can I check for input data type? YES -----> .isdigit()

#Loop to create as many passwords as the user needs
for count in range(amountPasswords):
    
    #Clear the password every loop
    password = ""

    #Loop to create a password the length defined by the user
    for count in range(amountCharacters):
        newChar = random.choice(char)
        password += newChar

    #Print the password
    print(password)