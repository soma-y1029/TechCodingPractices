https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        for ele in counter.items():
            if ele[1] == 1:
                return ele[0]
