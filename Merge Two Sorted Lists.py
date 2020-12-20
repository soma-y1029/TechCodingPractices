https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = res_head = ListNode()
        while l1 and l2:
            if l1.val <= l2.val:
                res.next = ListNode(l1.val)
                l1 = l1.next
            elif l2.val < l1.val:
                res.next = ListNode(l2.val)
                l2 = l2.next
            res = res.next
            
        if l1: res.next = l1
        elif l2: res.next = l2
                
        return res_head.next
