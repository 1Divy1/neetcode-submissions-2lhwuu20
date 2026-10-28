# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, minBound, maxBound) -> bool:
            if not node:
                return True
            left = right = True
            if not (minBound < node.val < maxBound):
                return False
            return dfs(node.left, minBound, node.val) and dfs(node.right, node.val, maxBound)
            
        return dfs(root, -float('inf'), float('inf'))