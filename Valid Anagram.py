https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = [0] * 26
        if len(s) != len(t): return False
        for letter_s, letter_t in zip(s, t):
            letters[ord(letter_s)-ord('a')] += 1
            letters[ord(letter_t)-ord('a')] -= 1
        for ele in letters:
            if ele:
                return False
        return True
