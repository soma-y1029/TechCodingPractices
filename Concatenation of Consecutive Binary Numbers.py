https://leetcode.com/contest/weekly-contest-218/problems/concatenation-of-consecutive-binary-numbers/

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        bin_str = ''
        for x in range(1, n+1):
            bin_str += str(bin(x))[2:]
        return int(bin_str, 2) % (10**9+7)
