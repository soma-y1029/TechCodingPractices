https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        res, stack = None, []
        
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res = root.val
            k -= 1
            if not k: return res
            root = root.right
