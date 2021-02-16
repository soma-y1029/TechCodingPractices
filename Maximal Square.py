https://leetcode.com/problems/maximal-square/


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == '1': 
                    matrix[i][j] = \
                    str(min(int(matrix[i-1][j-1]), int(matrix[i-1][j]), int(matrix[i][j-1]))+1)
        max_res = 0
        for row in matrix: 
            for ele in row: 
                if int(ele) > max_res: max_res = int(ele)
                    
        return max_res**2
