# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            # default case
            if not node:
                return 0
            
            # get local left height
            left = dfs(node.left)
            if left == -1: return -1 # broken condition => send -1 to parents
            
            # get local right height
            right = dfs(node.right)
            if right == -1: return -1 # broken condition => send -1 to parents
            
            # broken condition => send -1 to parents
            if abs(left - right) > 1:
                return -1
                
            # return max height between left and right + 1
            return max(left, right) + 1

        return dfs(root) != -1