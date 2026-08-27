# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter=0
        def get_depth(node):
            nonlocal diameter

            if not node:
                return 0
            
            # Recursively calculate depth of left and right subtrees
            left_depth = get_depth(node.left)
            right_depth = get_depth(node.right)
            
            # Update the global max diameter if the path through current node is larger
            diameter = max(diameter, left_depth + right_depth)
            
            # Return height/depth of current subtree to parent
            return 1 + max(left_depth, right_depth)

        get_depth(root)
        return diameter
        