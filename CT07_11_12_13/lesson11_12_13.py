import random
print("Hello from lesson 11_12_13")

# Recap 1

# def diceGuess(guess):
#     randomNum = random.randint(1,6)
#     return guess == randomNum

# num = 1
# for i in range(6):
#     if diceGuess(num):
#         num = num + 1
#         print("Correct!")
#     else:
#         print("Wrong!")
    

    
# Task 1

board = [
]
for i in range(3):
    row = [
]
    for i in range(3):
        row.append(' ')
    board.append(row)

def printBoard():
    global cellNumber
    cellNumber = 1
    for row in board:
        for cell in row:
            if cell != " ":
                print("", str(cell), "", str(cell), end = " ")
            else:
                print("", cellNumber, "", end = " ")
            if cellNumber % 3 != 0:
                print(" | ", end = " ")
            cellNumber = cellNumber + 1
        if cellNumber <= 9:
            print("---------")

printBoard()


                

    