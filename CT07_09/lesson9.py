import turtle
print("Hello from lesson 9")

# Task 1a

window = turtle.Screen()
window.setup()
window.bgcolor("#3BC10A")


# Task 1b

pen = turtle.Turtle()
pen.penup()
pen.sety(250)
pen.shape("square")
pen.color("#000000")
for i in range(-290, 330, 25):
    pen.setx(i)
    pen.stamp()


window.mainloop()
