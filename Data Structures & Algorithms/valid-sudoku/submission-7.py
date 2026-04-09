from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if self.validrows(board) and self.validcols(board) and self.validgrids(board):
            return True
        return False
    def validgroup(self, group: List[str]) -> bool:
            group = [num for num in group if num != "."]
            return len(group) == len(set(group))
    
    def validrows(self, board) -> bool:
        for row in board:
            if not self.validgroup(row):
                return False
        return True

    def validcols(self, board) -> bool:
        for col in range(9):
            column = [board[row][col] for row in range(9)]
            if not self.validgroup(column):
                return False
        return True


    def validgrids(self, board) -> bool:
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                subgrid = [board[r][c] for r in range(i, i + 3) for  c in range(j, j + 3)]
                if not self.validgroup(subgrid):
                    return False
        return True
