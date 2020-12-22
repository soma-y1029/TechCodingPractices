https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def inorder(root):
            if not root: return 
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
            
        res = []
        inorder(root)
        return res
    
    def iterative(self, root):
        res, stack = [], []
        while stack or root: 
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res
