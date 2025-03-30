import turtle
print("Hello from lesson 9")

# Recap 1a

window2 = turtle.Screen()


# Recap 1b

window2.setup(600, 400)


# Recap 2

t = turtle.Turtle()
t.shape("turtle")
t.fillcolor("#FF8000")
t.seth(0)
t.pendown()
while True:
    for i in range(4):
        t.forward(100)
        t.left(90)
    break


# Recap 3

notT = turtle.Turtle()
notT.shape("turtle")
notT.fillcolor("#FF8000")
notT.seth(0)
notT.pendown()
while True:
    for i in range(4):
        notT.forward(100)
        notT.left(90)
    break
window2.mainloop()a