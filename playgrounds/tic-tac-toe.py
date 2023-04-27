# from termcolor import cprint, colored

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
            
            string += ' ' + str(self.arr[i]) + ' '
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
        wins = [[0, 1, 2], [3,4,5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [6, 4, 2]]
        for player in [self.player1, self.player2]:
            for win in wins:
                for index in win:
                    if self.arr[index] == player.char:
                        continue
                    break
                else:
                    return player
            else:
                break
        else:
            return None
        


class Player:
    def __init__(self, name, char, score=0):
        self.name = name
        self.score = score
        self.char = char


    def __str__(self) -> str:
        return self.name + ' has score ' + str(self.score)


class Games:
    def __init__(self, players, games_to_play=[]):
        self.played = []
        self.to_play = games_to_play
        self.players = players
        
    def create_games(self):
        for player in self.players:
            for other_player in self.players:
                if player != other_player:
                    self.to_play.append(TicTacToe(player, other_player))

    def add_player(player):
        self.players.append(player)


def Main():
    inpt = int(input("number of players: "))
    game = Games([])
    for i in range(inpt):
        name = input('name: ')
        char = input('character: ')
        player = Player(name, char)
player1 = Player('jayam', 'X')
player2 = Player('pratham', 'O')
player3 = Player('ravi', 'R')

game = Games([player1, player3, player2])
game.create_games()

for g in game.to_play:
    for i in range(9):
        print(g)
        print(g.player1.name)
        print(g.player2.name)
        try:
            g.play(int(input("number: ")))
        except ValueError:
            continue
        if (g.check_win()):
            print('winner is:', g.check_win().name)
            g.check_win().score += 1
            continue

print(player1, player2, player3)
