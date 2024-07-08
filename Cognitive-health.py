#!/usr/bin/python3

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
        print("----------------------------------------------------------------------------------------------------------------------------"
        print("Welcome to the Memory Game!")
        print("1. Start Game")
        print("2. Instructions")
        print("3. About")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        if choice in ['1', '2', '3', '4']:
            return choice
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


#The function that is linked to 2.Help

