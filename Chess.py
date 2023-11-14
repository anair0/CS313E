#  File: Chess.py

#  Description: Finds total number of ways that the max number of queens can fit on a given chess
#               board without attacking each other

#  Student Name: Arjun Nair

#  Student UT EID: asn922

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 3/20/2022

#  Date Last Modified: 3/21/2022

import sys


class Queens(object):
    def __init__(self, n=8):
        self.board = []
        self.n = n
        for i in range(self.n):
            row = []
            for j in range(self.n):
                row.append('*')
            self.board.append(row)
        self.sol = 0

    # print the board
    def print_board(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.board[i][j], end=' ')
            print()
        print()

    # check if a position on the board is valid
    def is_valid(self, row, col):
        for i in range(self.n):
            if (self.board[row][i] == 'Q') or (self.board[i][col] == 'Q'):
                return False
        for i in range(self.n):
            for j in range(self.n):
                row_diff = abs(row - i)
                col_diff = abs(col - j)
                if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
                    return False
        return True

    # do the recursive backtracking
    def recursive_solve(self, col):
        if (col == self.n):
            return True
        else:
            for i in range(self.n):
                if (self.is_valid(i, col)):
                    self.board[i][col] = 'Q'
                    if (self.recursive_solve(col + 1)):
                        return True
                    self.board[i][col] = '*'
            return False

    # if the problem has a solution print the board
    def solve(self):
        for i in range(self.n):
            if (self.recursive_solve(i)):
                self.print_board()

    # prints the number of solutions
    # Same as the recursive solve function except it keeps going looking for total number of solutions
    def solutions(self, col=0):
        #Everytime there is a solution we increment the solution total from self
        if(col == self.n):
            self.sol += 1
            return self.sol
        else:
            for i in range(self.n):
                if(self.is_valid(i, col)):
                    self.board[i][col] = 'Q'
                    self.solutions((col + 1))
                    self.board[i][col] = '*'

def main():
    # read the size of the board
    line = sys.stdin.readline()
    line = line.strip()
    n = int(line)

    # create a chess board
    game = Queens(n)

    # place the queens on the board and count the solutions
    game.solutions()
    solutions = game.sol
    # print the number of solutions
    print(solutions)

if __name__ == "__main__":
    main()