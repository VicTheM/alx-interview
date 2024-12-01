#!/usr/bin/python3
"""
SOLUTION TO THE AGE LONG BACTRACKING PROBLEM
THIS FILE SOLVES THE N-QUEEN PROBLEM USING BACKTRACKING

WHAT DOES IT TAKE TO HAVE N NON-ATTACKING QUEENS ON AN
N * N CHWSS BOARD?
    1) No two queens on the same row
    2) No two queens on the same column
    3) No two queens on the same diagonal (left or right)
"""
import sys


def nonAttackingQueens(n):
    def is_safe(board, row, col):
        # Check the same column
        for i in range(row):
            if board[i] == col:
                return False

        # Check the main diagonal
        for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if board[i] == j:
                return False

        # Check the anti-diagonal
        for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
            if board[i] == j:
                return False

        return True

    def backtrack(row, board):
        # If all queens are placed successfully, add solution to result
        if row == n:
            solution = [[i, board[i]] for i in range(n)]
            result.append(solution)
            return

        for col in range(n):
            if is_safe(board, row, col):
                # Place the queen at board[row] = col
                board[row] = col

                # Recur to place the rest of the queens
                backtrack(row + 1, board)

                # Remove the queen to backtrack
                board[row] = -1

    result = []
    board = [-1] * n
    # Board is a 1D vector of length n
    # The indixes represent the row while the value
    # there represents the column
    backtrack(0, board)

    for oneSolution in result:
        print(oneSolution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    nonAttackingQueens(n)
