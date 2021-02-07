class Solution:
    def check(self, nums: List[int]) -> bool:
        if len(nums) < 2: return True
        prev = nums[0]
        for i, n in enumerate(nums[1:]): 
            if n < prev: # found place of rotation
                # print(n, i+1, prev, nums)
                nums = nums[i+1:] + nums[:i+1]
                break
            prev = n
        # check sorted
        # print(nums)
        prev = nums[0]
        for n in nums[1:]:
            if prev > n: # not sorted
                return False
            prev = n
        return True
    
