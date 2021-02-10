https://leetcode.com/problems/coin-change/submissions/

class Solution:
    def coinChange(self, coins: List[int], amount: int, num_coin=0) -> int:
        dp = [0] + [float('inf')]*amount
        for amt in range(1, amount+1):
            for coin in coins:
                if amt-coin >=0: dp[amt] = min(1 + dp[amt-coin], dp[amt])
        return dp[amount] if dp[amount] != float('inf') else -1
        
        
