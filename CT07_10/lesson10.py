import turtle
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

def square():
    notT.pendown()
    for i in range(4):
        notT.forward(20)
        notT.left(90)
window2 = turtle.Screen()
window2.setup(600, 400)
notT = turtle.Turtle()
notT.fillcolor("#FF007F")
notT.seth(0)

square()

window2.mainloop()
