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

        queue = deque()
        rightMostNodes = []
        queue.append(root)

        # BFS
        while queue:
            qLen = len(queue)
            level = []  # store every node from the current level

            # iterate only the nodes from the current level
            for _ in range(qLen):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # only add the right most node to the output list
            rightMostNodes.append(level[-1])

        return rightMostNodes