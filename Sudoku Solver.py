https://leetcode.com/problems/sudoku-solver/submissions/
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(num, pos): 
            # check row
            row, col = pos 
            for ele in board[row]: 
                # print(board[row])
                if num == ele: return False
            
            # check col
            for r in board: 
                if r[col] == num: return False
            
            # check square
            s_row, s_col = row//3*3, col//3*3
            for i in range(s_row, s_row+3):
                for j in range(s_col, s_col+3): 
                    # print(i,j, board[i][j])
                    if board[i][j] == num: return False
                    
            return True
        
        def getEmpty(): 
            for i in range(len(board)): 
                for j in range(len(board[0])): 
                    if board[i][j] == '.': 
                        return (i, j)
            
#         print('\n\n')
#         for row in board: 
#             print(row)
            
        def solve(): 
            pos = getEmpty()
            if not pos: return True
            
            i, j = pos
            for num in range(1, 10): 
                if isValid(str(num), (i, j)): 
                    board[i][j] = str(num)
                    if solve(): 
                        return True
                    board[i][j] = '.' 
            return False
                        
        solve()
                    
