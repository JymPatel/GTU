from termcolor import cprint, colored 0

class TicTacToe:
    def __init__(self, player1, player2):
        self.arr = [str(i + 1) for i in range(9)]
        self.player1 = player1
        self.player2 = player2
        self.currentTurn = player1
        self.winner = None
        self.moves = []


    def __str__(self) -> str:
        string = ""
        for i in range(9):
            if i % 3 == 0 and i != 0:
                string += '\n'
                string += '---+---+---\n'
            elif i != 0:
                string += '┆'
            
            string += f' {self.arr[i]} '
        return string
    
    
    def play(self, place):
        if self.arr[place - 1] < '1' or self.arr[place - 1] > '9':
            raise ValueError('incorrect move!')   
        self.arr[place - 1] = self.currentTurn.char
        self.moves.append(place - 1)
        self.change_turn()
            
            
    def change_turn(self):
        if self.currentTurn == self.player1:
            self.currentTurn = self.player2
        else:
            self.currentTurn = self.player1
            
            
    def check_win(self):
        pass


class Player:
    def __init__(self, name, char, score=0):
        self.name = name
        self.score = score
        self.char = char


class Games:
    def __init__(self, players, games_to_play=[]):
        self.played = []
        self.to_play = games_to_play
        self.players = players
        
    def create_games(self):
        pass


player1 = Player('jayam', 'X')
player2 = Player('pratham', 'O')
tictactoe = TicTacToe(player1, player2)
# tictactoe.play(1)
# tictactoe.play(3)
tictactoe.check_win()
print(tictactoe)


new_tictac = TicTacToe(player2, player1)
for i in range(9):
    new_tictac.play(int(input("enter number: ")))
    print(new_tictac)
    