import random
import os
import time
from leaderboard import update_leaderboard, display_leaderboard

# Define the symbols for the cards
symbols = ['🍎', '🍌', '🍓', '🍇', '🍒', '🍍', '🍉', '🥝']
symbols = symbols * 2  # We need pairs

# Shuffle the symbols
random.shuffle(symbols)

# Create the game board
board = [symbols[i:i+4] for i in range(0, len(symbols), 4)]

# Function to print the game board
def print_board(board, revealed):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if revealed[row][col]:
                print(board[row][col], end=' ')
            else:
                print('❓', end=' ')
        print()
    print()

# Initialize the revealed board
revealed = [[False]*4 for _ in range(4)]

# Function to check if all pairs are matched
def all_matched(revealed):
    return all(all(row) for row in revealed)

# Main game loop
moves = 0
start_time = time.time()
while not all_matched(revealed):
    os.system('clear')  # Clear the console (use 'cls' for Windows)
    print_board(board, revealed)

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

    os.system('clear')
    print_board(board, revealed)

    # Check if the cards match
    if board[row1][col1] != board[row2][col2]:
        print('No match! Try again.')
        time.sleep(2)  # Pause to let the user see the result
        revealed[row1][col1] = False
        revealed[row2][col2] = False
    else:
        print('Match found!')

    moves += 1

# End of the game
os.system('clear')
print_board(board, revealed)
end_time = time.time()
elapsed_time =end_time - start_time
print(f'Congratulations! You completed the game in {moves} moves.')
player_name =input("Enter your name for the leaderboard:")
update_leaderboard(player_name,elapsed_time)
