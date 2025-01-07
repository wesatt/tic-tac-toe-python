class TicTacToe:
    def __init__(self, player_name, first, x_o):
        self.player_name = player_name
        self.first = first
        self.x_o = x_o
        self.board = [[" - "]*3]*3
        self.game_ongoing = True

    def start_game(self):
        if self.first == True:
            print(f"Welcome {self.player_name}! You are '{self.x_o}' and you are going first!")
            while self.game_ongoing == True:
                self.print_board()
                self.user_turn()
                if self.game_ongoing == True:
                    self.print_board()
                    self.computer_turn_random()
            print("Game Over!")
            print("More to come soon!")
        elif self.first == False:
            print(f"Welcome {self.player_name}! You are '{self.x_o}' and you are going second!")

    def print_board(self):
        b = self.board
        print("   ", " A ", " B ", " C ")
        print(" 1 ", b[0][0], b[0][1], b[0][2])
        print(" 2 ", b[1][0], b[1][1], b[1][2])
        print(" 3 ", b[2][0], b[2][1], b[2][2])

    def user_turn(self):
        move_check_result = False
        while move_check_result == False:
            print("Please make a valid move (e.g. A1, b2, c3)")
            player_move = input().capitalize()
            move_check_result = self.move_check(player_move)
        game_status = self.check_win()
        if game_status == 'win':
            print(f'{self.player_name} wins!')
            self.game_ongoing = False
        elif game_status == 'tie':
            print('Tie game!')
            self.game_ongoing = False

    def computer_turn_random(self):
        print("Computer makes a random move")
        game_status = self.check_win()
        if game_status == 'win':
            print('Computer wins!')
            self.game_ongoing = False
        elif game_status == 'tie':
            print('Tie game!')
            self.game_ongoing = False

    def move_check(self, move):
        move_dictionary = {
            'A1': (0,0),
            'A2': (1,0),
            'A3': (2,0),
            'B1': (0,1),
            'B2': (1,1),
            'B3': (2,1),
            'C1': (0,2),
            'C2': (1,2),
            'C3': (2,2)
        }
        if move in move_dictionary.keys():
            m = move_dictionary[move]
            if self.board[m[0]][m[1]] == ' - ':
                return True
            else:
                return False
        else:
            return False

    def check_win(self):
        return 'tie'
