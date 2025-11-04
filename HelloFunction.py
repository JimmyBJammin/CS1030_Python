def hello(name):
    print("Hello, World!")
    print("Hello, " + name + "!")

userInput = input("What is your name?\n")

hello(userInput)

def addNine(number):
    number += 9
    return number

userNumber = int(input("Please enter a number.\n"))

print("Here's your number plus nine!")
print(addNine(userNumber))