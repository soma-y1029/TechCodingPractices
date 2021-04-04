https://leetcode.com/contest/weekly-contest-235/problems/number-of-different-subsequences-gcds/
 
import math
class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        subs = []
        def permutation(current, start): 
            if current: subs.append(current)
            for i, n in enumerate(nums[start:]):
                permutation(current+[n], start+i+1)
        
        permutation([], 0)

        gcds = set()
        # find GCD
        for sub in subs: 
            if len(sub) <= 1: gcds.add(sub[0]); continue
            n1, n2 = sub[0], sub[1]
            gcd = math.gcd(n1, n2)
            for i in range(2, len(sub)): 
                gcd = math.gcd(gcd, sub[i])
            gcds.add(gcd)
            print(sub, gcd)
        return len(gcds)
            
                
