https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lA, lB = headA, headB
        # find length of two list
        lenA, lenB = 0, 0
        while lA or lB:
            if lA:
                lA = lA.next
                lenA += 1
            if lB:
                lB = lB.next
                lenB += 1
        
        lA, lB = headA, headB
        if lenA < lenB:
            lA, lB = headB, headA
            lenA, lenB = lenB, lenA
         # A is always longer
        
        for _ in range(lenA-lenB): lA = lA.next
        while lA or lB:
            if lA == lB: return lA
            lA, lB = lA.next, lB.next
