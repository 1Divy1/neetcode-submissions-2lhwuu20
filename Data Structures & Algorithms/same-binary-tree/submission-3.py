# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def sameTree(p, q):
            # ambele nu exista
            if p is None and q is None:
                return True

            # unul exista iar celalalt nu exista
            if p is None or q is None:
                return False

            # ambele exista, si sunt pe aceeasi ramura, dar valorile sunt diferite
            if p.val != q.val:
                return False
                
            return sameTree(p.left, q.left) and sameTree(p.right, q.right)

        return sameTree(p, q)