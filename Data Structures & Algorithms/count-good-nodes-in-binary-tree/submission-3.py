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
            isGoodNode = 1 if node.val >= maxParent else 0
            maxParent = max(maxParent, node.val)
            return isGoodNode + dfs(node.left, maxParent) + dfs(node.right, maxParent)

        return dfs(root, -101)