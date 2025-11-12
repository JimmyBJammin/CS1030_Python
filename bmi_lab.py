#Get_Positive_Number will return a inputted user value and ensure that it's positive
def Get_Positive_Number(prompt):
    positive_value = int(input(prompt))

    while positive_value <= 0:
        print("That is a negative value. Please enter a positive number.")
        positive_value = int(input(prompt))
    
    return positive_value

#BMI_Calculator will take in user's inputted height and weight and return the calculated BMI value
def BMI_Caluclator(weight, height):
    BMI = round((weight / (height * height)) * 703, 2)

    return BMI

#Get_Category will take the BMI value and return what category it reflects
def Get_Category(BMI):
    if BMI <= 18.5:
        category = "Underweight"
    elif BMI <= 25:
        category = "Healthy Weight"
    elif BMI <= 30:
        category = "Overweight"
    else:
        category = "Obese"
    
    return category


#Get user input
name = input("What is your name? ")
weight = Get_Positive_Number("What is your weight, in pounds? ")
height = Get_Positive_Number("What is your height, in height? ")

BMI = BMI_Caluclator(weight, height)

#Print out values
print("\nYour name is " + name + ". You weigh " + str(weight) + " pounds and you're " + str(height) + " inches tall.")

print("Your BMI is " + str(BMI))
print("Your BMI category is: " + Get_Category(BMI))