https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3658/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        arr = [0]*(len(nums)+1)
        res = [0, 0]
        for n in nums: arr[n] += 1
        for i in range(len(arr)): 
            if arr[i] == 0: res[1] = i
            if arr[i] == 2: res[0] = i
        return res
        
            
