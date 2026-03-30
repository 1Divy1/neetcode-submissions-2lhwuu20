# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiam = 0

        # we use this nested method in order to keep track of current max diameter
        def dfs(root):
            if not root:
                return 0

            # maxDiam variable doesn't belong to this method
            nonlocal maxDiam

            # get current max height for left and right subtrees
            left = dfs(root.left)
            right = dfs(root.right)

            # store the largest diameter up to this point
            maxDiam = max(maxDiam, left + right)

            # return to parent node the largest height up to this point
            return 1 + max(left, right)

        dfs(root)

        return maxDiam