https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        queue, res = [root], []
        while queue:
            next_level = []
            res.append([node.val for node in queue])
            for root in queue:
                if root.left: next_level.append(root.left)
                if root.right: next_level.append(root.right) 
            queue = next_level
        return res
