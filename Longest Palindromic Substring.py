https://leetcode.com/problems/longest-palindromic-substring/
  
  class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[0 if st != end else 1 for end in range(len(s))] for st in range(len(s)) ]
        max_st, max_end = 0, 0
        for end_st in range(1, len(s)): 
            st = 0
            for end in range(end_st, len(s)):
                # print(f'{dp=}\n{st=}, {end=}\n{s[st:end+1]}')
                if st == end: dp[st][end] = 1
                elif end - st == 1: 
                    if s[st] == s[end]: dp[st][end] = 1
                    else: dp[st][end] = 0
                        
                else: 
                    if s[st] != s[end]: dp[st][end] = 0
                    else: 
                        if dp[st+1][end-1]: dp[st][end] = 1
                        else: dp[st][end] = 0
                # print(dp[st][end])
                if dp[st][end] and (max_end - max_st + 1) < (end - st + 1): 
                    max_st, max_end = st, end
                    # print('New MAX')
                st += 1
        return s[max_st:max_end+1]
