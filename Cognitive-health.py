#!/usr/bin/python3
import random
import os
import time


#List of symbols for the cards
symbols = ['❤','🤩','🤑','🤡','😎','😂','😏','🥵']
symbols = symbols * 2 #to make pairs

#to shuffle the symbols randomly
random.shuffle(symbols)

#List of numbers for the cards
numbers = ['2','4','6','8','10','12','14','16']
numbers =numbers * 2 #to make pairs
random.shuffle(numbers)

#List of letters for cards 
letters = ['A','F','H','U','L','T','C','Z']
letters = letters * 2 #to make pairs
random.shuffle(letters)

#the menu display of the game 
def display_menu():
    while True:
        os.system('clear')
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("✨ Welcome to the Memory Game ✨")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("1. Start Game")
        print("2. Instructions")
        print("3. About")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        if choice in ['1', '2', '3', '4']:
            return choice
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


#The function that is linked to 2.Instructions
def display_instructions():
    os.system('clear')
    print("📜 Memory Game Instructions:")
    print("1. The game board contains 8 pairs of hidden symbols.")
    print("2. On each turn, you can reveal two cards.")
    print("3. If the symbols on the cards match, they remain revealed.")
    print("4. If they do not match, they will be hidden again.")
    print("5. The game continues until all pairs are matched.")
    print("Goodluck 🤞") 
    print("\nPress Enter to return to the menu.")
    input()  # Waits for the user to press Enter sp that they can go back to the menu

#The fuction that is linked to 3.about
def display_about():
    os.system('clear')
    print("📜 About Memory Game:")
    print("Version: 1.0")
    print("Author: NegPod 9")
    print("This game is a simple memory matching game developed as a project that aims to support cognitive health for all in Africa and beyond.")
    print("\nPress Enter to return to the menu.")
    input()  # Wait for the user to press Enter

#The loop that includes the menu and the gane together so that it can run together 
#Write the rest of your code before this not after this needs to come last
if __name__ == "__main__":
    while True:
        choice = display_menu()
        if choice == '1':
            main_game()
        elif choice == '2':
            display_instructions()
        elif choice == '3':
            display_about()
        else:
            print("Goodbye!👋")
            break
