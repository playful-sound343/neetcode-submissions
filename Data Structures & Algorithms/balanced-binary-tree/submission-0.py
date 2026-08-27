# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_Height(node)->int:
            if not node:
                return True
            
            left_h=check_Height(node.left)
            right_h=check_Height(node.right)

            if left_h==-1:
                return -1
            if right_h==-1:
                return -1 

            if abs(left_h-right_h)>1:
                return -1

            return 1+max(left_h,right_h)

        return check_Height(root)!=-1      