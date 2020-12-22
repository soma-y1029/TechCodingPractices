https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        queue = [root]
        while queue:
            vals, this_level = [], []
            while queue:
                root = queue.pop(0)
                if root.left: 
                    this_level.append(root.left)
                    vals.append(root.left.val)
                else: vals.append(None)
                if root.right: 
                    this_level.append(root.right)
                    vals.append(root.right.val)
                else: vals.append(None)
            if vals[::-1] != vals: return False
            queue = this_level
        return True

    def isSymmetric2(self, root):
        def inner(root1, root2):
            if not root1 and not root2: return True
            if not root1 or not root2: return False
            return root1.val == root2.val and inner(root1.left, root2.right) and inner(root1.right, root2.left)
        
        return inner(root, root)
