# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goods = 0

        def dfs(curr: TreeNode, maxPath):
            nonlocal goods
            
            if not curr:
                return
            
            if curr.val >= maxPath:
                maxPath = curr.val
                goods += 1

            dfs(curr.left, maxPath)
            dfs(curr.right, maxPath)
        
        dfs(root, -101)
        return goods