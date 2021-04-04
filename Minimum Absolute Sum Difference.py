https://leetcode.com/contest/weekly-contest-235/problems/minimum-absolute-sum-difference/
  class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        diff = [abs(a-b) for a, b in zip(nums1, nums2)]
        change_idx = 0
        # find index that has largest difference
        for idx, n in enumerate(diff): 
            if diff[change_idx] < n:
                change_idx = idx

        # find closed num to the nums2[change_idx] from nums1
        replace_with = min(nums1, key=lambda x: abs(x-nums2[change_idx]))
        nums1[change_idx] = replace_with
        return sum([abs(a-b) for a, b in zip(nums1, nums2)])%(10**9+7)
                
