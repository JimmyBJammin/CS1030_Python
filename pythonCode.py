#Declare name, hobby, birth year, current year and use inputs to collect values
name = str(input("What is your name? "))
hobby = str(input("What do you like to do? "))
birth_year = int(input("What year were you born? "))
current_year = int(input("What year is it now? "))

#Print the name and hobby
print("\nHi "+ name + "!")
print("I hear you like to " + hobby + "?")

#Declare age and calculate with birth year and current year
age = current_year - birth_year

#Print name and age
#age needs to be made into a string to print
print("\n" + name + ", if my calculations are correct, you must be " + str(age) + " years old!")


