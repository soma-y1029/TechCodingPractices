https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def rec(nums, curr=[]):
            if not nums: return curr
            
            for i, num in enumerate(nums):
                temp = rec(nums[:i]+nums[i+1:], curr+[num])
                if temp: res.append(temp)
        
        res = []
        rec(nums)
        return res
