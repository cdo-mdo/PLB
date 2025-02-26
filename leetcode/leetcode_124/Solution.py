class TreeNode:
    __init__:
        self.val = val
        self.left = left
        self.right = right

def maxPathSum(root: TreeNode) -> int:
    max_sum = float('-inf') # global value to store the maximum path sum

    def dfs(node):
        non_local max_sum
        if not node:
            return 0

        # compute max path sum from left and right subtree (ignore negatives)
        left_max= max(dfs(node.left), 0)
        right_max = max(dfs(node.right), 0)

        # compute max path sum including this node as the highest node
        local_max = node.val + left_max + right_max

        # update the global max sum
        max_sum = max(max_sum, local_max)

        # return the max sum including this node, extending to parent
        return node.val + max(left_max, right_max)

    dfs(root)
    return max_sum


