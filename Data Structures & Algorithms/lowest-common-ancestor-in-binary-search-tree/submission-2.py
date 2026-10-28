# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def findLCA(root, p, q):

            # LCA is in the left subtree
            if p.val < root.val and q.val < root.val:
                return findLCA(root.left, p, q)

            # LCA is in the right subtree
            elif p.val > root.val and q.val > root.val:
                return findLCA(root.right, p, q)

            # LCA is above both p and q
            else:
                return root
                
        return findLCA(root, p, q)