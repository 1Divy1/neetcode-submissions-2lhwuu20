# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        rightSide = [root.val]
        queue = deque([root])
        
        while queue:
            level = []
            for i in range(len(queue)):
                level.append(queue.popleft())

            children = []
            for node in level:
                if node.left:
                    children.append(node.left.val)
                    queue.append(node.left)
                if node.right:
                    children.append(node.right.val)
                    queue.append(node.right)

            if children:
                rightSideNode = children[-1]
                rightSide.append(rightSideNode)

        return rightSide