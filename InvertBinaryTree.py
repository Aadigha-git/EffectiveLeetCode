class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):
    if not root:
        return None

    # Swap the left and right subtrees
    root.left, root.right = root.right, root.left

    # Recursively invert the left and right subtrees
    invertTree(root.left)
    invertTree(root.right)

    return root
# Create the binary tree
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

# Invert the tree
inverted_root = invertTree(root)

# Print the inverted tree (in-order traversal)
def printInOrder(node):
    if node:
        printInOrder(node.left)
        print(node.val, end=" ")
        printInOrder(node.right)

printInOrder(inverted_root)
# Output: 9 7 6 4 3 2 1


"""
Question6:

Given the root of a binary tree, invert the tree, and return its root.
"""