import random
from game_files.tictactoe import TicTacToe

# gets player name
# print("Hey there! Welcome to Tic-Tac-Toe! Please input your name:")
# name = input().capitalize()

# gets player x or o
# print(f"Pleased to meet you, {name}! Do you want to be x's or o's?")
# while True:
#     try:
#         x_o = input().capitalize()
#         if x_o == "X" or x_o == "O":
#             break
#         else:
#             print("Please make a valid selection: 'X' or 'O'.")
#     except:
#         continue

# creates boolean list whether the player goes first or not
# first = [True, False]

# create game instance
# game = TicTacToe(name, random.choice(first), x_o)

game = TicTacToe("Wesatt", True, "X")

# initiate game
game.start_game()