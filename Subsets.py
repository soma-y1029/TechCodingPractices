https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def recursive(curr=[], i=0):
            if i > len(nums): return 
            res.append(curr)
            for s in range(i, len(nums)):
                recursive(curr+[nums[s]], s+1)
        res = []
        recursive()
        return res
