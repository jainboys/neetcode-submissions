class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if len(board) != 9:
            return False
        for row in board:
            if not self.is_arr_valid(row):
                return False
        for j in range(9):
            colj = [board[i][j] for i in range(9)]
            if not self.is_arr_valid(colj):
                return False
        for m in range(0, 9, 3):
            for n in range(0, 9, 3):
                square_arr = [board[m+i][n+j] for i in range(3) for j in range(3)]
                if not self.is_arr_valid(square_arr):
                    return False 
        
        return True
    
    def is_arr_valid(self, row: List[str]):
        found=set()
        for x in row:
            if x == '.':
                continue
            int_x = int(x)
            if int_x < 1 or int_x > 9:
                return False
            if int_x in found:
                return False
            found.add(int_x)
        return True
