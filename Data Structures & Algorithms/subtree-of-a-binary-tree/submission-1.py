# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, tree, subTree):
        if not tree and not subTree:
            return True
        if not tree or not subTree or tree.val != subTree.val:
            return False
        return (self.isSameTree(tree.left, subTree.left) and
                self.isSameTree(tree.right, subTree.right))
    
    def isSubtree(self, tree: Optional[TreeNode], subTree: Optional[TreeNode]) -> bool:
        if not subTree:
            return True
        if not tree:
            return False
        if self.isSameTree(tree, subTree):
            return True
        return (self.isSubtree(tree.left, subTree) or
                self.isSubtree(tree.right, subTree))