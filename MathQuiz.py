import random
# 1. Generate two random single-digit integers (0–9)
number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

# 2. If number1 < number2, swap number1 with number2
if number1 < number2:
   temp = number1
   number1 = number2
   number2 = temp

# 3. Prompt the student to answer "What is number1 - number2?"
answer = int(input(f"What is {number1} - {number2}? "))

# 4. Grade the answer and display the result
if number1 - number2 == answer:
   print("You are correct!")
else:
   print("Your answer is wrong.")
   print(f"{number1} - {number2} should be {number1 - number2}.")
