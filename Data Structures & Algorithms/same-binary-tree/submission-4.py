# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p, q):
            # neither node exists
            if not p and not q:
                return True
            # one node is on one side and the other one is on the other side or non-existant
            if not p or not q:
                return False
            # both nodes exists but values are different
            if p.val != q.val:
                return False
            return dfs(p.left, q.left) and dfs(p.right, q.right)
        return dfs(p, q)