https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a, b = headA, headB
        lenA, lenB = 0, 0
        while a: 
            lenA += 1
            a = a.next 
        while b: 
            lenB += 1
            b = b.next
            
        a, b = headA, headB
        if lenB < lenA: 
            a, b = b, a
            lenA, lenB = lenB, lenA
            
        for _ in range(lenB-lenA): b = b.next
        while a and b: 
            if a == b: return a
            a, b = a.next, b.next
            
