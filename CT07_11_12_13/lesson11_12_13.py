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

def initialiseBoard():
    board = [
]
    for i in range(3):
        row = [
]
        for i in range(3):
            row.append(' ')
        board.append(row)
    return board

def printBoard(board):
    global cellNumber
    print("\nBoard Layout:")
    cellNumber = 1
    for row in board:
        for cell in row:
            if cell != " ":
                print("", str(cell), "", end = " ")
            else:
                print("", cellNumber, "", end = " ")
            if cellNumber % 3 != 0:
                print("|", end = " ")
            cellNumber = cellNumber + 1
        if cellNumber <= 9:
            print("\n---------------")
    print("\n")

def playerMove(currentPlayer):
    moveInput = input("Player " + currentPlayer + ". Enter your move: (1 - 9): ")
    if moveInput.isdigit() and int(moveInput) < 10:
        move = int(moveInput) - 1
        row = move // 3
        column = move % 3
        if board[row][column] == "X" or "O":
            board[row][column] = currentPlayer
        else:
            print("That spot is already taken. Please choose another.")
    else:
        print("Invalid. Please put a number from 1 - 9.")

def checkWin(board):
    global winConditions
    winConditions = [
    # Horizontal
    [board[0][0], board[0][1], board[0][2]],
    [board[1][0], board[1][1], board[1][2]],
    [board[2][0], board[2][1], board[2][2]],
    # Vertical
    [board[0][0], board[1][0], board[2][0]],
    [board[0][1], board[1][1], board[2][1]],
    [board[0][2], board[1][2], board[2][2]],
    # Diagonal
    [board[0][2], board[1][1], board[2][0]],
    [board[0][0], board[1][1], board[2][2]],
]
    for formula in winConditions:
        if formula[0] == formula[1] == formula[2] and formula[0] != ' ':
            return True
    return False

def switchPlayer(currentPlayer):
    if currentPlayer == 'X':
        return 'O'
    return 'X'
    

board = initialiseBoard()
currentPlayer = 'X'
while True:
    printBoard(board)
    playerMove(currentPlayer)
    if checkWin(board):
        printBoard(board)
        print("Player " + currentPlayer + ". ")
        break
    currentPlayer = switchPlayer(currentPlayer)


                

    