# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_parent) -> int:
            if not node:
                return 0
            is_good_node = 1 if node.val >= max_parent else 0
            max_parent = max(max_parent, node.val)
            return is_good_node + dfs(node.left, max_parent) + dfs(node.right, max_parent)
        return dfs(root, -101)