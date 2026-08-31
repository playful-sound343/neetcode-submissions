# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def traverse(node,max_so_far):
            if not node:
                return 0
                
            
            good=1 if node.val>=max_so_far else 0
            current_max=max(max_so_far,node.val)
            left_good=traverse(node.left,current_max)
            right_good=traverse(node.right,current_max)

            return left_good+good+right_good

        return traverse(root, root.val)

            
        