class TicTacToe:
    def __init__(self, player_name, first, x_o):
        self.player_name = player_name
        self.first = first
        self.x_o = x_o
        self.board = [[" - "]*3]*3

    def start_game(self):
        if self.first == True:
            print(f"Welcome {self.player_name}! You are '{self.x_o}' and you are going first!")
        elif self.first == False:
            print(f"Welcome {self.player_name}! You are '{self.x_o}' and you are going second!")

        self.print_board()

        print("More to come soon!")

    def print_board(self):
        b = self.board
        print("   ", " A ", " B ", " C ")
        print(" 1 ", b[0][0], b[0][1], b[0][2])
        print(" 2 ", b[1][0], b[1][1], b[1][2])
        print(" 3 ", b[2][0], b[2][1], b[2][2])

    def user_turn(self):
        print("player makes a move")

    def computer_turn_random(self):
        print("Computer makes a random move")

    def move_check(self):
        print("checks if a move is valid")

    def check_win(self):
        print("checks win, lose, tie, ongoing")
