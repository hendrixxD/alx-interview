#!/usr/bin/env python3

import sys


def print_board(board):
    """
    Prints the current state of the chess board.

    Args:
        board (List[List[str]]): The chess board to print.
    """
    for row in board:
        print(" ".join(row))
    print()


def is_safe(board, row, col, n):
    """
    Determines whether a queen can be safely placed on the current
    chess board at the given row and column.

    Args:
        board (List[List[str]]): The chess board to check.
        row (int): The row to check.
        col (int): The column to check.
        n (int): The size of the board.

    Returns:
        bool: True if the queen can be safely placed, False otherwise.
    """
    # check row
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # check upper diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # check lower diagonal
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True


def solve(board, col, n):
    """
    Recursively solves the N Queens problem by placing queens on the
    chess board one column at a time.

    Args:
        board (List[List[str]]): The chess board to solve.
        col (int): The current column being processed.
        n (int): The size of the board.

    Returns:
        bool: True if a solution was found, False otherwise.
    """
    if col == n:
        print_board(board)
        return True

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 'Q'

            solve(board, col + 1, n)

            board[i][col] = '.'

    return False


def nqueens(n):
    """
    Solves the N Queens problem for a given board size.

    Args:
        n (int): The size of the board.

    Returns:
        int: 0 if successful, 1 otherwise.
    """
    if not isinstance(n, int):
        print("N must be a number")
        return 1
    elif n < 4:
        print("N must be at least 4")
        return 1

    board = [['.' for _ in range(n)] for _ in range(n)]

    solve(board, 0, n)


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
        print('N must be at least 4')
        exit(1)

    nqueens(n)
