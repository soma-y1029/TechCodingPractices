https://leetcode.com/problems/top-k-frequent-elements/

import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        #return [item[0] for item in counter.items()][:k]
        arr = []
        for item in counter.items():
            arr.append((-item[1], item[0]))
        heapq.heapify(arr)
        res = []
        for i in range(k):
            res.append(heappop(arr)[1])
            
        return res
