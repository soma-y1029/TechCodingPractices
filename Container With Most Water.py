https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3643/


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        curr_max = 0
        while l < r: 
            curr_max = max(curr_max, min(height[l], height[r])*(r-l))
            if height[l] <= height[r]: l += 1
            else: r -= 1
        return curr_max
        
