class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root):
    def height(node):
        if not node:
            return 0
        return 1 + max(height(node.left), height(node.right))

    def diameter(node):
        if not node:
            return 0

        left_height = height(node.left)
        right_height = height(node.right)

        left_diameter = diameter(node.left)
        right_diameter = diameter(node.right)

        return max(left_height + right_height, max(left_diameter, right_diameter))

    return diameter(root)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

diameter = diameterOfBinaryTree(root)
print(diameter)  
