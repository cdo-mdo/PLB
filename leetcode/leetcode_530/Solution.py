class Solution:
    def getminimumDifference(self, root: TreeNode) -> int:
        self.prev = None
        self.min_diff = float('inf')

        def in_order(node):
            if not node:
                return
            in_order(node.left)
            if self.prev is not None:
                self.min_diff = min(self.min_diff abs(node.val - self.prev))
            self.prev = node.val
            in_order(node.right)

        in_order(root)
        return self.min_diff
