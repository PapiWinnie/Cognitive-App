#!/usr/bin/python3
import os

# Function to print the game board
def print_board(board, revealed):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if revealed[i][j]:
                print(board[i][j], end=' ')
            else:
                print('X', end=' ')
        print()

# Initialize game variables
board = [
    ['A', 'B', 'C', 'D'],
    ['E', 'F', 'G', 'H'],
    ['I', 'J', 'K', 'L'],
    ['M', 'N', 'O', 'P']
]
revealed = [[False] * 4 for _ in range(4)]

# Get the first card
row1 = int(input('Enter the row for the first card (0-3): '))
col1 = int(input('Enter the column for the first card (0-3): '))
revealed[row1][col1] = True

os.system('clear')
print_board(board, revealed)

# Get the second card
row2 = int(input('Enter the row for the second card (0-3): '))
col2 = int(input('Enter the column for the second card (0-3): '))
revealed[row2][col2] = True

# Show the updated board
os.system('clear')
print_board(board, revealed)
