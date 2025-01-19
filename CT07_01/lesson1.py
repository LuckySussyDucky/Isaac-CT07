print("Hello from lesson 1")

# variable called 'glass'
# variable called 'paper'
# variable called 'plastic'
# if item is glass 
#     say 'it is a glass'
# else 
#     if item is paper
#         say 'it is a paper'
#     else
#         if item is plastic
#             say 'it is a plastic'
#         else
#             say 'this is not a recyclable'


# Task 1

RedPlates = 1
BluePlates = 2 
GreenPlates = 3
AmountR = int(input("How many red plates of sushi did you eat? "))
AmountB = int(input("How many blue plates of sushi did you eat? "))
AmountG = int(input("How many green plates of sushi did you eat? "))
CostR = AmountR * RedPlates
CostB = AmountB * BluePlates
CostG = AmountG * GreenPlates
TotalCost = CostR + CostB + CostG
print("You spent $", TotalCost, "on sushi!")


# Task 2 

# There is a total of 3 bugs in the following program.
# Identify and fix the bugs:
score_one = 80
score_two = 90
score_three = 75
total = score_one + score_two + score_three
average_score = total / 3
student_name = "Alex"
print("Average score for ", student_name, " is: ", average_score)


# Task 3

score = int(input("What was your score for PSLE? "))
if score > 100:
    print("You are a liar")
elif score >= 75:
    print("Your grade is A.")
elif score >= 60:
    print("Your grade is B.")
elif score >= 50:
    print("Your grade is C.")
else:
    print("You failed really badly womp womp!")


