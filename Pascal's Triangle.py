https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # if not numRows: return []
        
        triangle = [[1],[1,1]]
        if numRows <= 2: return triangle[:numRows]
        for row in range(2, numRows):
            this_row = [1]
            for i in range(1, row):
                this_row.append(triangle[row-1][i-1]+triangle[row-1][i])
            triangle.append(this_row+[1])
        return triangle
