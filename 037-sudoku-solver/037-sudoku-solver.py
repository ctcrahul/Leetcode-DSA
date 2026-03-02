from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Solves the given Sudoku puzzle in-place using backtracking.
        """

        def isValid(board: List[List[str]], row: int, col: int, c: str) -> bool:
            """
            Check if placing character `c` at position (row, col) is valid.
            - Row check
            - Column check
            - 3x3 subgrid check
            """
            for i in range(9):
                # Row check
                if board[row][i] == c:
                    return False
                # Column check
                if board[i][col] == c:
                    return False
                # Subgrid check
                subRow = 3 * (row // 3) + i // 3
                subCol = 3 * (col // 3) + i % 3
                if board[subRow][subCol] == c:
                    return False
            return True

        def solve(board: List[List[str]]) -> bool:
            """
            Backtracking function:
            - Try filling empty cells ('.') with digits 1–9.
            - If valid, recurse further.
            - If stuck, backtrack.
            """
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':  # Empty cell found
                        for c in map(str, range(1, 10)):  # Try digits 1–9
                            if isValid(board, i, j, c):
                                board[i][j] = c  # Place digit
                                if solve(board):  # Recurse
                                    return True
                                board[i][j] = '.'  # Backtrack
                        return False  # No valid digit found → backtrack
            return True  # Puzzle solved

        solve(board)
