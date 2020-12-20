https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res, sub = 0, 0
        for i in range(len(s)):
            # if i+1, i+2 is larger than i, 
            # it is about subtraction
            num = roman[s[i]]
            if (i < len(s)-1 and roman[s[i+1]] > num) or \
            (i < len(s)-2 and roman[s[i+2]] > num):
                sub += num
            else:
                res += num-sub
                sub = 0
                
        return res
