#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

import os
import time


def playTic():
    print("Welcome to Tic-Tac-Toe Game!")
    print("Please enter the number of the cell you want to play.")
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")
    print("-----------")

    # Create a list to keep the cells
    cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    # Show the empty cells
    showCells(cells)

    # Set the first player
    player = "X"

    # Repeat until the game is over
    while True:
        # Get a move from the player
        move = getMove(cells, player)

        # Update cells
        cells[move] = player

        # Show the cells
        showCells(cells)

        # Check if the player wins
        if isWon(cells, player):
            print(player, "won")
            break

        # Check if the game is over
        if isFull(cells):
            print("Draw")
            break

        # Switch player
        if player == "X":
            player = "O"
        else:
            player = "X"

    # Ask if the player wants to play again
    answer = input("Do you want to play again? (y/n): ").lower()
    if answer == "y":
        playTic()


def showCells(cells):
    print(cells[1] + " | " + cells[2] + " | " + cells[3])
    print("-----------")
    print(cells[4] + " | " + cells[5] + " | " + cells[6])
    print("-----------")
    print(cells[7] + " | " + cells[8] + " | " + cells[9])
    print("-----------")


def getMove(cells, player):
    while True:
        move = eval(input("Enter a move for " + player + ": "))
        if move < 1 or move > 9:
            print("The cell number must be between 1 and 9")
        elif cells[move] != " ":
            print("The cell is not empty")
        else:
            return move


def isWon(cells, player):
    return (cells[1] == player and cells[2] == player and cells[3] == player) or \
           (cells[4] == player and cells[5] == player and cells[6] == player) or \
           (cells[7] == player and cells[8] == player and cells[9] == player) or \
           (cells[1] == player and cells[4] == player and cells[7] == player) or \
           (cells[2] == player and cells[5] == player and cells[8] == player) or \
           (cells[3] == player and cells[6] == player and cells[9] == player) or \
           (cells[1] == player and cells[5] == player and cells[9] == player) or \
           (cells[3] == player and cells[5] == player and cells[7] == player)


def isFull(cells):
    for i in range(1, 10):
        if cells[i] == " ":
            return False

    return True


def main():
    playTic()

    # Ask if the player wants to play again
    answer = input("Do you want to play again? (y/n): ").lower()
    if answer == "y":
        playTic()
    else:
        print("Thank you for playing the game. Goodbye!")
        time.sleep(2)
        os.system("cls")


if __name__ == "__main__":
    main()
