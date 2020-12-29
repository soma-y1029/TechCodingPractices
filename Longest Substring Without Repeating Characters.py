https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = j = 0
        max_length = 0
        seen = set()
        while j < len(s):
            if s[j] not in seen:
                seen.add(s[j]) 
                max_length = max(max_length, j-i+1)
                j += 1
            else:
                seen.remove(s[i])
                i += 1
        
        return max_length
