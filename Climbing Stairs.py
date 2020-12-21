https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int, dp=dict()) -> int:
        if n in dp: return dp[n]
        if n == 0: return 1
        if n < 0: return 0
        
        dp[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return dp
    def climbStairs2(self, n):
        n1, n2 = 1, 2
        if n < 3: return n
        for _ in range(3, n+1):
            n3 = n1 + n2
            n1, n2 = n2, n3
        return n2
