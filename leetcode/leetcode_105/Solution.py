from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    inorder_index_map = {val: idx for idx, val in enumerate(inorder)}

    def helper(pre_start, in_start, in_end):
        if pre_start >= len(preorder) or in_start > in_end:
            return None

        root_val = preorder[pre_start]
        root = TreeNode(root_val)

        # Find root index in inorder
        root_index = inorder_index_map[root_val]

        # Recursively build left and right subtree
        root.left = helper(pre_start + 1, in_start, root_index - 1)
        root.right = helper(pre_start + (root_index - in_start) + 1, root_index + 1, in_end)

        return root

    return helper(0, 0, len(inorder) - 1)

preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

root = buildTree(preorder, inorder)
print(root.val, root.left.val, root.right.val)
