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
            # extragem toate nodurile de pe nivel
            level = []
            for i in range(len(queue)):
                level.append(queue.popleft())

            # extragem copiii nodurilor de pe nivel
            children = []
            for node in level:
                if node.left:
                    children.append(node.left.val)
                    queue.append(node.left)
                if node.right:
                    children.append(node.right.val)
                    queue.append(node.right)

            # right side e a doua jumatate a lui level
            # daca avem doar un nod, atunci il folosim pe acela
            if children:
                rightSideNode = children[-1]
                rightSide.append(rightSideNode)

        print("right side ", rightSide)
        return rightSide