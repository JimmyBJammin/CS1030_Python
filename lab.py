# This program asks for your name and calculates your average and highest test scores
# It contains several errors (syntax, runtime, and logic) for you to find and fix


#Welcoming the user, collecting a name through user input
print("Welcome to the Debugging Lab!")

name = input("Enter your name: ")
print("Hello " + name + "!" + " Let's calculate your test scores.")

#List of scores
scores = [85, 90, 78, 88, 92]

#Totaling the [scores] list
total = 0
for score in scores:
    total = total + score

#Calculating the average with total and the length of [scores]
average = total / len(scores)
print("Your average score is:" + str(average))

#Determing the highest score by cycling through
highest = 0
for s in scores:
    if s > highest:
        highest = s

print("Your highest score was:" + str(highest))

