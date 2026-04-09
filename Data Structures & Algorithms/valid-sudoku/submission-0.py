from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.is_valid_rows(board) and self.is_valid_columns(board) and self.is_valid_subgrids(board)
    
    def is_valid_rows(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.is_valid_group(row):
                return False
        return True
    
    def is_valid_columns(self, board: List[List[str]]) -> bool:
        for col in range(9):
            column = [board[row][col] for row in range(9)]
            if not self.is_valid_group(column):
                return False
        return True
    
    def is_valid_subgrids(self, board: List[List[str]]) -> bool:
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                subgrid = [board[r][c] for r in range(row, row + 3) for c in range(col, col + 3)]
                if not self.is_valid_group(subgrid):
                    return False
        return True
    
    def is_valid_group(self, group: List[str]) -> bool:
        group = [num for num in group if num != '.']
        return len(group) == len(set(group))
