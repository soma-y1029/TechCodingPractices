https://leetcode.com/contest/weekly-contest-228/problems/count-number-of-homogenous-substrings/


class Solution:
    def countHomogenous(self, s: str) -> int:
        if len(s) == 1: return 1
        subs, res = 1, 0
        L = len(s)
        # print('new')
        for i, l in enumerate(s[1:], 1):
            # print(i, l)
            if s[i-1] != s[i]: # calculate subs
                res += sum(range(subs+1))
                subs = 1
            else: 
                subs += 1
        res += sum(range(subs+1))
        return res % (10**9+7)
