# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = k
        kThItem = 0

        def dfs(root):
            nonlocal counter, kThItem
            if not root:
                return
            # inorder traversal => sorted order
            dfs(root.left)
            counter -= 1
            if counter == 0:
                kThItem = root.val
                return
            dfs(root.right)

        dfs(root)
        return kThItem