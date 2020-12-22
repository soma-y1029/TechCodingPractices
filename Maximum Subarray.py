https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_so_far, total_max = float('-inf'), float('-inf')
        for num in nums:
            sum_so_far = max(num, sum_so_far+num)
            total_max = max(sum_so_far, total_max)
        return total_max
