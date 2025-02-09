import time
import random
print("Hello from lesson 3")


# # Task 1 

# studyTimeMin = int(input("How much time do you wish to spend on studying in minutes? "))
# studyTimeSec = studyTimeMin * 60
# while studyTimeSec != 0:
#     time.sleep(1)
#     print(studyTimeSec)
#     studyTimeSec = studyTimeSec - 1


# Task 2 

days = 0 
savings = 0 
while savings < 100:
    money = int(input("How much did you save? "))
    savings = savings + money
    days = days + 1
    if savings >= 100:
        break
print("It took you", days, "days to get at least $100!")


# Task 3 

totalQuestion = 15
lives = 3
for i in range(totalQuestion):
    num1 = random.randint(2, 20)
    num2 = random.randint(2, 20)
    correctAnswer = num1 * num2
    while lives > 0:
        answer = input(f"What is {num1} x {num2}? ")
        if correctAnswer == answer:
            print("Correct! Let's move i")