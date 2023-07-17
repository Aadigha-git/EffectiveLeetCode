class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(root):
    # Recursive function to calculate the height of a tree
    def height(node):
        if not node:
            return 0
        return max(height(node.left), height(node.right)) + 1

    # Recursive function to check if a tree is balanced
    def isBalancedHelper(node):
        if not node:
            return True

        left_height = height(node.left)
        right_height = height(node.right)

        if abs(left_height - right_height) > 1:
            return False

        return isBalancedHelper(node.left) and isBalancedHelper(node.right)

    return isBalancedHelper(root)

# Create a balanced binary tree
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(isBalanced(root))

"""
Question11:

Check if a binary tree is balanced or not
"""
