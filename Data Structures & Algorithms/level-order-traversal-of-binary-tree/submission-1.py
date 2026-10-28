# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # EDGE CASE: the tree is empty
        if not root:
            return []

        level = [[root.val]]
        queue = deque([root])

        while queue:
            # we pop as many nodes from the queue, as its size
            poppedNodes = []
            for i in range(len(queue)):
                poppedNodes.append(queue.popleft())
            
            # we process the popped nodes' children in batch
            temp = []
            for node in poppedNodes:
                if node.left:
                    queue.append(node.left)
                    temp.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    temp.append(node.right.val)
                    
            # if there are children, we save the current level's nodes
            if temp:
                level.append(temp)
        
        return level