https://leetcode.com/problems/first-bad-version/
  
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left < right:
            mid = (right-left)//2 + left
            print(mid)
            if isBadVersion(mid): right = mid
            else: left = mid+1
            
        return left
            
        
