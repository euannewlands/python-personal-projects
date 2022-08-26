import numpy as np

# TODO: Add some docstrings for each method

class NaughtsAndCrosses:
    def __init__(self):
        start = [" "]*9
        raw_board = np.array(start)
        self.board = raw_board.reshape(3,3)

    def nlp_position(self, row, col):
        '''Function converts user entry to array index'''
        try:
            # convert row string to array value
            if row.lower() in ["top", "t", "upper", "1", "u"]:
                row = 0
            elif row.lower() in ["middle", "m", "2"]:
                row = 1
            elif row.lower() in ["lower", "bottom", "b", "l", "3"]:
                row = 2
            else:
                raise Exception()

            if col.lower() in ["left", "l", "1"]:
                col = 0
            elif col.lower() in ["middle", "m", "2"]:
                col = 1
            elif col.lower() in ["right", "r", "3"]:
                col = 2
            else:
                raise Exception()

            return row, col

        except:
            print("Unrecognised position. Try again.")

    def validate_pos(self, pos):
        try:
            if len(pos) == 2:
                row, col = pos[0],pos[1]
            elif len(pos) == 3:
                row, col = pos[0], pos[2]
            else:
                raise Exception()
        except:
            print("Invalid position format. Enter as tm or 12.")
            return None
        return row, col

    def ask_user(self):
        pos = None
        while pos == None:
            pos = input("\nEnter position [row,column]: ")
            try:
                row, col = self.validate_pos(pos)
                row, col = self.nlp_position(row, col)
            except:
                pos = None
        return row, col

    def update_board(self, row, col, player):
        if player == 1:
            icon = 'X'
        else:
            icon = 'O'
        
        # update board if space is empty
        if self.board[row][col] == ' ':
            self.board[row][col] = icon
            return True
        else:
            print(f"Space is already occupied by {self.board[row][col]}.")
            return False

    def display_raw_board(self):
        print("\n",self.board)

    def check_end(self):
        # check rows
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != ' ':
                return True

        # check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return True

        # check diagonals
        i, j = [0,2],[2,0]
        for check in range(2):
            if self.board[0][i[check]] == self.board[1][1] == self.board[2][j[check]] != ' ':
                return True

        return False

    @staticmethod
    def select_player():
        # generator object: alternates between players
        while True:
            yield 1
            yield 2         

    def main_loop(self):

        self.main_display()
        game_done = False
        players = self.select_player()
        turns = 0

        while game_done == False:
            turn_played = False
            player = next(players)
            while turn_played == False:
                row, col = self.ask_user()
                turn_played = self.update_board(row, col, player)
            game_done = self.check_end()
            
            self.main_display() ### display subject to change

            if game_done == True:
                print(f"\nPlayer {player} wins!")
            print("\n")

            turns+=1
            if turns == 9 and game_done == False:
                print("Game over! Stalemate :o\n")
                break

    def main_display(self):
        b = self.board
        print("    1   2    3")
        print(f'1   {b[0][0]} | {b[0][1]} | {b[0][2]}')
        print(f'    --|---|--')
        print(f'2   {b[1][0]} | {b[1][1]} | {b[1][2]}')
        print(f'    --|---|--')
        print(f'3   {b[2][0]} | {b[2][1]} | {b[2][2]}')

    def play(self):
        self.main_loop()