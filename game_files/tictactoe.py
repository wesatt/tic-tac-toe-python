class TicTacToe:
    def __init__(self, player_name, first, x_o):
        self.player_name = player_name
        self.first = first
        self.x_o = x_o

    def start_game(self):
        if self.first == True:
            print(f"Hello {self.player_name}! You are '{self.x_o.capitalize()}' and you are going first!")
        elif self.first == False:
            print(f"Hello {self.player_name}! You are '{self.x_o.capitalize()}' and you are going second!")
