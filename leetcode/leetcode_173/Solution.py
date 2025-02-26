class TreeNode:
    __init__(self, val = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stack = []
        self._push_leftmost(root)

    def _push_leftmost(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        if not self.stack:
            return None
        # get the smallest element
        node = self.stack.pop()
        # push the leftmost path of right subtree
        if node.right:
            self._push_leftmost(node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


