https://leetcode.com/problems/excel-sheet-column-number

class Solution:
    def titleToNumber(self, s: str) -> int:
        res, power = 0, 0
        for letter in s[::-1]:
            i = ord(letter) - ord('A') + 1 
            res += 26 ** power * i
            power += 1
        return res
