https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # count length 
        list_A, list_B = headA, headB
        len_A, len_B = 0, 0
        
        # get length for A and B
        while list_A or list_B:
            if list_A:
                list_A = list_A.next
                len_A += 1
            if list_B:
                list_B = list_B.next
                len_B += 1

        list_A, list_B = headA, headB
        
        print(len_A, len_B)
        # move pointer of longer list to match position
        for _ in range(abs(len_A - len_B)):
            if len_A > len_B:
                list_A = list_A.next
            else:
                list_B = list_B.next
        
        # print(list_A, list_B)
        # now both headA and headB points same position
        # check for intersection
        while list_A != list_B:
            list_A, list_B = list_A.next, list_B.next
            
        return list_A
