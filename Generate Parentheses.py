https://leetcode.com/problems/generate-parentheses/submissions/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(curr='', opn=0, close=0):
            if close > opn: return
            if opn > n or close > n: return
            if opn+close == 2*n: res.append(curr)
            backtrack(curr+'(', opn+1, close)
            backtrack(curr+')', opn, close+1)
        res = []
        backtrack()
        return res
