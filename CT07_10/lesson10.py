import turtle
import random
print("Hello from lesson 9")

# # Recap 1a

# window2 = turtle.Screen()


# # Recap 1b

# window2.setup(600, 400)


# # Recap 2

# t = turtle.Turtle()
# t.shape("turtle")
# t.fillcolor("#FF8000")
# t.seth(0)
# t.pendown()
# while True:
#     for i in range(4):
#         t.forward(100)
#         t.left(90)
#     break


# # Recap 3

# notT = turtle.Turtle()
# notT.shape("turtle")
# notT.fillcolor("#FF007F")
# notT.seth(0)
# notT.pendown()
# for i in range(5):
#     notT.forward(100)
#     notT.left(72)
# window2.mainloop()


# Task 1

def alert():
    print("Motion Detected")

alert()
alert()
alert()


# Task 2

def square(length):
    notT.pendown()
    for i in range(4):
        notT.forward(length)
        notT.left(90)
    notT.penup()
window2 = turtle.Screen()
window2.setup(600, 400)
notT = turtle.Turtle()
notT.fillcolor("#FF007F")
notT.seth(0)


# Task 3

def multiply(num1, num2):
    answer = num1 * num2
    print(answer)

multiply(3, 5)


# Task 4

def moveableSquare(axisX, axisY):
    notT.penup()
    notT.goto(axisX, axisY)
    notT.pendown()
    for i in range(4):
        notT.forward(20)
        notT.left(90)
    notT.penup()

moveableSquare(-50, -50)
moveableSquare(50, 50)
moveableSquare(-50, 50)
moveableSquare(50, -50)


# Task 5

def isElderly(age):
    if age > 65:
         return True

age = input("What is your age? ")    
if isElderly(int(age)):
    print("You are worthy for our 1 cent discount! ")
else:
    print("Such a fool to come here! You are not worthy for our 1 cent discount! ")
isElderly(30)
isElderly(70)


# Task 6

def turtleCoordinates(name):
    xcor = name.xcor()
    ycor = name.ycor()
    return xcor, ycor

xcor, ycor = turtleCoordinates(notT)
print("The turtle coordinates after drawing is: " + str(xcor) + ", " + str(ycor))


# Task 7

def WhatsAppME(number):
    print("WhatsApp me at https://wa.me/65" + str(number))

WhatsAppME(82667414)

number = ""
for i in range(100):
    firstDigit = str(random.randint(8, 9))
    number
    for i in range(7):
        lastSeven = str(random.randint(0, 9))
        number = number + lastSeven
        





window2.mainloop()
