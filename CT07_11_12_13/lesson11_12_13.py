import turtle
import random
print("Hello from lesson 11_12_13")

# Recap 1

def diceGuess(guess):
    randomNum = random.randint(0,7)
    return guess == randomNum

num = 1
for i in range(6):
    diceGuess(num)
    

    
# Task 1

window = turtle.Screen()
window.setup(600, 600)
window.bgcolor("#FFFFFF")

