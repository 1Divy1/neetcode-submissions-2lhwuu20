class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def getMaxDepth(node) -> int:
            if not node:
                return 0
            return 1 + max(getMaxDepth(node.left), getMaxDepth(node.right))

        def getDiameter(node):
            nonlocal diameter
            if not node:
                return
            diameter = max(diameter, getMaxDepth(node.left) + getMaxDepth(node.right))
            getDiameter(node.left)
            getDiameter(node.right)

        getDiameter(root)
        return diameter