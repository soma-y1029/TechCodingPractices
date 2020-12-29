https://leetcode.com/problems/combination-sum/submissions/

class Solution:
    def combinationSum(self, candidates: List[int], target: int, comb=[], i=0) -> List[List[int]]:
                
        def recursion(target=target, comb=[]):
            if target == 0: return ans.add(tuple(sorted(comb)))
            if target < 0: return 
            
            for num in candidates:
                recursion(target-num, comb+[num])
            
        ans = set()
        recursion()
        return list(ans)
