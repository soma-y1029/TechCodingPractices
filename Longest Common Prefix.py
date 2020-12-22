https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        for chs in zip(*strs):
            cand = chs[0]
            for ch in chs[1:]:
                if cand != ch: return prefix
            prefix += cand
        return prefix
