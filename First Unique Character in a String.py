https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hm = dict()
        for l in s:
            if hm.get(l): hm[l] += 1
            else: hm[l] = 1
                
        for i, l in enumerate(s):
            if hm[l] == 1: return i
            
        return -1
                
