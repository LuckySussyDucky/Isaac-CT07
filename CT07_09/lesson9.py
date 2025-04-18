import random
import turtle
print("Hello from lesson 9")

# Task 1a

window = turtle.Screen()
window.setup(600, 600)
window.bgcolor("#3BC10A")


# Task 1b

pen = turtle.Turtle()
pen.penup()
pen.sety(250)
pen.shape("square")
pen.color("#000000")
for i in range(-290, 310, 25):
    pen.setx(i)
    pen.stamp()


# Task 1c

pen.color("#FFFF00")
pen.goto(-300, -250)
pen.pendown()
pen.seth(0)
pen.forward(600)
pen.hideturtle()


# Task 1d

Sally = turtle.Turtle()
Sally.penup()
Sally.shape("turtle")
Sally.color("#FF0000")
Sally.seth(90)
Sally.goto(0, -250)
Sally.write("Sally", align = "center", font = ('Ariel', 20))


# Task 1e

John = turtle.Turtle()
John.penup()
John.shape("turtle")
John.color("#0000FF")
John.seth(90)
John.goto(-200, -250)
John.write("John", align = "center", font = ('Ariel', 20))


Bob = turtle.Turtle()
Bob.penup()
Bob.shape("turtle")
Bob.color("#FFFFFF")
Bob.seth(90)
Bob.goto(200, -250)
Bob.write("Bob", align = "center", font = ('Ariel', 20))


# Task 1f

guessWinner = input("Guess the winner! ")


# Task 1g

winner = ""
y_axis = 250
Bob.pendown()
Sally.pendown()
John.pendown()
while True:
    Sally.seth(random.randint(75,115))
    Sally.forward(random.randint(1,20))
    John.seth(random.randint(75,115))
    John.forward(random.randint(1,20))
    Bob.seth(random.randint(75,115))
    Bob.forward(random.randint(1,20))
    if Sally.ycor() > y_axis:
            winner = "Sally"
            break
    elif John.ycor() > y_axis:
            winner = "John"
            break
    elif Bob.ycor() > y_axis:
            winner = "Bob"
            break


# Task 1h

if winner == guessWinner:
    print("You guessed it correctly! It was " + winner + "!")
else:
    print("You guesswd it wrongly. It was " + winner + ".")



window.mainloop()
