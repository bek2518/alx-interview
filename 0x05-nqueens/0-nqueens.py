#!/usr/bin/python3
'''
Solves the N-queens puzzle challenge
'''
import sys


if len(sys.argv) < 2 or len(sys.argv) > 2:
    print('Usage: nqueens N')
    sys.exit(1)

try:
    N = int(sys.argv[1])
except Exception:
    print('N must be a number')
    sys.exit(1)

if int(sys.argv[1]) < 4:
    print('N must be atleast 4')
    sys.exit(1)

chessboard = []
for i in range(N):
    chessboard.append([0] * N)


def recursive_function(chessboard, start_col, N):
    '''
    Recursive function that loops over each column, checks if the row
    and column are free to place using checker function. Then places
    either the queen or x (unavailable) and recursively calls for the
    next column
    If the column equals N it will print the positions which the queens
    can be placed at
    '''
    for row in range(N):
        if checker(chessboard, row, start_col, N):
            chessboard[row][start_col] = 'Queen'
            recursive_function(chessboard, start_col + 1, N)
            chessboard[row][start_col] = 'x'

    if start_col == N:
        position = []
        possible_solution = []
        for i in range(N):
            for j in range(N):
                if chessboard[i][j] == 'Queen':
                    position = [i, j]
                    possible_solution.append(position)
                position = []
        print(possible_solution)
        return


def checker(chessboard, row, start_col, N):
    '''
    Checker function which checks if the place requested is available by
    first checking if a queen is present on the entire column (horizontally).
    Then checks the digonally.
    '''
    for col in range(start_col):
        if chessboard[row][col] == 'Queen':
            return False
    i = row
    j = start_col
    while i >= 0 and j >= 0:
        if chessboard[i][j] == 'Queen':
            return False
        i -= 1
        j -= 1
    i = row
    j = start_col
    while i < N and j >= 0:
        if chessboard[i][j] == 'Queen':
            return False
        i += 1
        j -= 1
    return True


recursive_function(chessboard, 0, N)
