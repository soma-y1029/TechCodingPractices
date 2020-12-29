https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int, mem=dict()) -> int:
        key = (min(m,n), max(m,n))
        if key in mem: return mem[key]
        if m == 1 and n == 1: return 1
        if m < 1 or n < 1: return 0
        
        mem[key] = self.uniquePaths(m-1, n, mem) + self.uniquePaths(m, n-1, mem)
        return mem[key]
