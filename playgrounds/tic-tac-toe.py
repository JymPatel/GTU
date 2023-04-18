class TicTacToe:
    def __init__(self):
        self.arr = [str(i + 1) for i in range(9)]

    def __str__(self) -> str:
        string = ""
        for i in range(9):
            if i % 3 == 0 and i != 0:
                string += '\n'
                string += '-----------\n'
            elif i != 0:
                string += '|'
            
            string += f' {self.arr[i]} '
        return string
    
    def play(self, char, place):
        if char >= '1' and char <= '9':
            raise ValueError
        else:
            self.arr[place - 1] = char
            
    def check_win(self):
        diff_char = set([i for i in self.arr if i < '1' or i > '9'])
        
tictactoe = TicTacToe()
tictactoe.play('o', 1)
tictactoe.check_win()
print(tictactoe)