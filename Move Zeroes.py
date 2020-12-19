https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = []
        for i in range(len(nums)):
            if not nums[i]: zeros.append(i)
            elif zeros:
                zero = zeros.pop(0)
                nums[zero], nums[i] = nums[i], nums[zero]
                zeros.append(i)
        
