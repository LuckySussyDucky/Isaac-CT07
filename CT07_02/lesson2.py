print("Hello from lesson 2")


# Task 1

for i in range(0,21):
    print(i)

for i in range(1,31):
    print(i)

for i in range(2,25,2):
    print(i)


# Task 2

counter = 0
while counter < 21:
    print(counter)
    counter += 1

counter = 1
while counter < 31:
    print(counter)
    counter += 1

counter = 2
while counter < 25:
    print(counter)
    counter += 2


# Task 3

counter = 1
while True:
    print(counter)
    counter += 1
    if counter == 6:
        break


# Task 4a

counter = 1
while True:
    print(counter)
    counter += 1
    if counter == 11:
        break
print("YAY")


# Task 4b

counter = 1
while counter <= 10:
    print(counter)
    counter += 1
    if counter == 6:
        break
else:
    print("YAY")


# Task 5

toppings = input("What toppings would you like on your pizza? ")
stuff = "cheese"
while True:
    toppings2 = input("What other toppings would you like on your pizza? ")
    if toppings2 == "end":
        print("Your pizza has " + stuff + " and " + toppings + "!")
        break
    else:
        stuff = stuff + ", " + toppings2


# Task 6

questions = "What is 1 + 1? "
answer = 2 #integer type --> data type eg, integer, double, float ,string (str)
UserAnswer = 0
while UserAnswer != answer:
    UserAnswer = int(input(questions))
    if UserAnswer == answer:
        print("YAY! You got it correct!")
        break
    else:
        print("You got it wrong!")

# answer = input("What is the colour of the Orange?") 
# while (answer != "orange"):
#     print("answer wrong, try again")
#     answer = input("What is the colour of the Orange?") 

# print("answer correct")

QuestionAnswer = ["What is 1 + 1? ", "2"
                    "What is 3 - 1? ", "2"
                    "What is 2 - 0? ", "2"
                    ]
for i in range(0, len(QuestionAnswer), 2):
    questions = QuestionAnswer(i)
    answer = QuestionAnswer(i + 1)
    UserAnswer = input(questions)
    while UserAnswer != answer:
        print("You got it wrong!")
        UserInput = input(questions)
    print("YAY! You got it correct!")
    
