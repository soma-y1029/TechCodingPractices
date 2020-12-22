https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:        
        carry_out, i = 1, len(digits)-1
        while i > 0: 
            digits[i] += carry_out
            carry_out, digits[i] = divmod(digits[i], 10)
            i -= 1
        digits[0] += carry_out
        if digits[0] > 9: 
            digits.insert(0, 1)
            digits[1] %= 10
        return digits
