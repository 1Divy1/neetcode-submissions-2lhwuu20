# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes = []

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            dfs(root.right)
            nonlocal nodes
            if root.val not in nodes:
                nodes.append(root.val)

        dfs(root)
        nodes.sort()
        return nodes[k - 1]