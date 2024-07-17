#!/usr/bin/python3
import os

LEADERBOARD_FILE = "leaderboard.txt"

# Function to update the leaderboard
def update_leaderboard(player_name, elapsed_time):
    with open(LEADERBOARD_FILE, "a") as file:
        file.write(f"{player_name},{elapsed_time}\n")
