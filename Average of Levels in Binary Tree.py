https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3661/
  
  # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root: return 0
        queue = [root]
        ans = []
        while queue: 
            this_level, next_level = [], []
            for node in queue: 
                this_level.append(node.val)
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)
            ans.append(sum(this_level)/len(this_level))
            queue = next_level
        return ans
