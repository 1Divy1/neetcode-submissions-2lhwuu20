# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # the "Same tree" problem solution
        def subtree(p, q) -> False:
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return subtree(p.left, q.left) and subtree(p.right, q.right)
        
        # 1. Find the root of the subtree in the big tree - BFS
        queue = deque([root])
        foundSubRoot = root
        while queue:
            node = queue.popleft()
            res = subtree(node, subRoot)
            if res == True:
                return res
            left = node.left
            right = node.right
            if left:
                queue.append(left)
            if right:
                queue.append(right)
        
        # 2. Run the subtree algorithm
        return subtree(foundSubRoot, subRoot)