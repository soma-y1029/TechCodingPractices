https://leetcode.com/problems/k-closest-points-to-origin/submissions/

import math
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def minheapify(arr, n, p): 
            smallest = p 
            smallest_d = math.sqrt(arr[p][0]**2 + arr[p][1]**2)

            l, r = 2*p+1, 2*p+2
                        
            if l < n: 
                ld = math.sqrt(arr[l][0]**2 + arr[l][1]**2)
                if ld < smallest_d: smallest = l; smallest_d = ld
            if r < n: 
                rd = math.sqrt(arr[r][0]**2 + arr[r][1]**2)
                if rd < smallest_d: smallest = r; smallest_d = rd
            if smallest != p: 
                arr[smallest], arr[p] = arr[p], arr[smallest]
                minheapify(arr, n, smallest)
                
        def heapsort(arr=points, K=K): 
            n = len(arr)
            for p in reversed(range(n)): 
                minheapify(arr, n, p)
                
            for i in reversed(range(n)): 
                arr[i], arr[0] = arr[0], arr[i]
                minheapify(arr, i, 0)
                
                K -= 1
                if K == 0: 
                    return arr[i:][::-1]
                
            return 
        return heapsort()
