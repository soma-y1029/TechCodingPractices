https://leetcode.com/contest/weekly-contest-231/problems/check-if-binary-string-has-at-most-one-segment-of-ones/

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        zero = False
        for bit in s: 
            if bit == '0': zero = True
            elif bit == '1' and zero: return False
        return True
