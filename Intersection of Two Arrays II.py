https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        cnt1, cnt2 = collections.Counter(nums1), collections.Counter(nums2)
        if len(cnt1) < len(cnt2): cnt1, cnt2 = cnt2, cnt1
        for key2, val2 in cnt2.items():
            if cnt1.get(key2):
                while cnt1[key2] and val2:
                    cnt1[key2] -= 1
                    val2 -= 1
                    res.append(key2)
        return res
