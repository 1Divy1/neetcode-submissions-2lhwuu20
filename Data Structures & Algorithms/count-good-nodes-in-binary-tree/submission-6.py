# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxParent) -> int:
            if not node:
                return 0
            goodNodes = 1 if node.val >= maxParent else 0
            maxParent = max(maxParent, node.val)
            goodNodes += dfs(node.left, maxParent) 
            goodNodes += dfs(node.right, maxParent)
            return goodNodes

        return dfs(root, -101)