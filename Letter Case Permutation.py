https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3642/

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        def recursion(curr=S, i=-1):
            # print(curr, i)
            res.append(curr)
            
            for index in range(i+1, len(curr)):
                letter = curr[index]
                if letter.isalpha():
                    if letter.islower(): 
                        recursion(curr[:index]+letter.upper()+curr[index+1:], index)
                    if letter.isupper(): 
                        recursion(curr[:index]+letter.lower()+curr[index+1:], index)
                        
            
        res = []
        recursion()
        return res
