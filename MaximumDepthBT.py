class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root):
    if not root:
        return 0

    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)

    return max(left_depth, right_depth) + 1
# Create the binary tree: 1 -> 2 -> 4, 2 -> 5, 1 -> 3
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

depth = maxDepth(root)
print(depth)  
