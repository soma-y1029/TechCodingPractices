https://leetcode.com/problems/reverse-nodes-in-k-group/
  
 # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int, last_tail=None) -> ListNode:

        length = 0
        copy = head
        while copy: 
            copy = copy.next
            length += 1
            
        if length < k: return
        
        dest, dest_prev = head, head

        for _ in range(k): 
            dest_prev = dest
            dest = dest.next
        dest_prev.next = None 
        
        prev = dest 
        curr = head
        while curr: 
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        if last_tail: last_tail.next = prev
        self.reverseKGroup(dest, k, head)
        
        return prev
