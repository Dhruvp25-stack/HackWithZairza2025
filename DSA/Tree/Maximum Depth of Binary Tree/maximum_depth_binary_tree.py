# Problem: Maximum Depth of Binary Tree
# Approach: Recursive Depth-First Search (DFS)

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def maxDepth(root):
    # Base case: empty tree
    if not root:
        return 0
    
    # Recursively find depth of left & right subtrees
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    
    # Add 1 to include current node
    return 1 + max(left_depth, right_depth)

# ------- Driver Code / Sample Test --------

if __name__ == "__main__":
    # Constructing the binary tree
    #        1
    #      /   \
    #     2     3
    #    / \
    #   4   5

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print("Maximum Depth of Binary Tree:", maxDepth(root))
