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
pen.hideturtle


# Task 1d

Sally = turtle.Turtle()
Sally.shape("turtle")
Sally.color("#FF0000")
Sally




window.mainloop()
