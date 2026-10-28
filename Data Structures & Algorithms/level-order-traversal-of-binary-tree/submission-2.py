# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        levels = [[root.val]]
        queue = deque([root])

        while queue:
            level = []
            children = []

            # extragem toate nodurile de pe nivelul curent
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node)
            
            # grupam impreuna copiii nodurilor din nivelul curent
            for node in level:
                if node.left:
                    queue.append(node.left)
                    children.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    children.append(node.right.val)
            if children:
                levels.append(children)

        return levels