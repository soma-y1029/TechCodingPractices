https://leetcode.com/contest/weekly-contest-231/problems/minimum-elements-to-add-to-form-a-given-sum/
  
  class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        s = sum(nums)
        if goal == s: return 0
        q, m = divmod(goal-s, limit)
        if q > 0: return q + 1 if m else q
        else: return abs(q)
            

