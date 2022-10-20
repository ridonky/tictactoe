class ticTacToe():

    def __init__(self,player1="X",player2="O"): #track current player
        self.player1 = player1
        self.player2 = player2
        self.current = player1 # automatically set curent player to 1
        self.next = player2
        self.boardmap = {}
        self.gameboard = [[0] * 3] * 3
        print("New Game!")
    
    def newTurn(self):
        board = self.gameboard
        # show whose turn it is - current player
        print(f"It's your turn, {self.current} !")
        # print the board
        self.printBoard()
    
    def selectMove(self):
        print(f"choose your move by indicating which number space you want to place your {self.current}:")
        # show the possible moves for current player
        self.printBoard(num=1)
        # request an input from the user asking for their number and wait for it...
        move = input("Spot number: ")
        return int(move)

    def printBoard(self,num=False):
        board = self.gameboard
        for i,row in enumerate(board):
            for j,spot in enumerate(row):
                if not num:
                    print("_ ",end='') if spot == 0 else print(f'{self.gameboard[i][j]} ',end='')
                else:
                    # Create the boardmap
                    self.boardmap[num] = [i,j]
                    print(f"{num} ",end='') if spot == 0 else print(f'_ ',end='')
                    num+=1
            print("")
        # print(f'boardmap is {self.boardmap}')

    def checkValidMove(self,move=None):
        # map the move
        # if int(move): # is an eerror
        #     pass
        #     help it along.
        if move < 0 or move > 10 or move not in self.boardmap:
            #its bad, tell them that
            print("trash move baby")
            self.selectMove()
        elif move in self.boardmap:
            # it is one of the available moves!
            # update gameboard with that shit.
            self.gameboard[self.boardmap[move][0]][self.boardmap[move][1]] = self.current
            # clear the boardmap
            self.boardmap = {}
        else:
            print("thats an invalid move.")
            self.selectMove()

    def checkWin(self):
        # all spots in any row are occupied by current player
        for row in self.gameboard:
            if row == [f'{self.current}',f'{self.current}',f'{self.current}']:
                # its a win!
                return True
        # all spots with shared col are occupied by current player
        for i in range(3):
            if self.gameboard[0][i] == self.gameboard[1][i] == self.gameboard[2][i] == self.current:
                # its a win!
                return True
        # 2 diags
        if self.gameboard[0][0] == self.gameboard[1][1] == self.gameboard[2][2] == self.current or self.gameboard[0][2] == self.gameboard[1][1] == self.gameboard[2][0] == self.current:
            return True
        else:
            return False

    def checkGameover(self):
        if 0 not in self.gameboard:
            return True
        return False

    def switchTurns(self):
        self.current, self.next = self.next, self.current
    
    def gameover(self):
        self.printBoard()
        print(f"{ttt.current} wins! Nice job.") if ttt.checkWin() else print(f"its a tie")
        return


if __name__ == '__main__':
    # start game
    ttt = ticTacToe()
    while not ttt.checkWin() or not ttt.checkGameover():
        ttt.switchTurns()
        ttt.newTurn()
        move = ttt.selectMove()
        ttt.checkValidMove(move)
    ttt.gameover()
