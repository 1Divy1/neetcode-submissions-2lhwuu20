# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def dfs(node):
            # cazul de oprire al apelurilor recursive
            if not node:
                return 0
            
            # iteram toate nodurile, pe stanga si dreapta
            left = dfs(node.left)
            right = dfs(node.right)

            # daca e cazul, actualizam diametrul cu suma inaltimilor curente left si right
            self.diameter = max(self.diameter, left + right)

            # returnam maximul inaltimilor dintre left si right 
            return 1 + max(left, right)

        dfs(root)
        return self.diameter