https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        pair = {')': '(', '}': '{', ']': '['}
        stack = []
        for ch in s:
            if ch in pair:
                if not stack: return False
                if stack.pop() != pair[ch]: return False
                else: pass
            else: stack.append(ch)
        if stack: return False
        return True
