https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = sum(range(n+1))
        for num in nums:
            ans -= num
        return ans
