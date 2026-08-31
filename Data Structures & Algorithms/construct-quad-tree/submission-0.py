"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(r,c,length):

            if length==1:
                return Node(grid[r][c]==1,True)

            l=length//2

            top_right=dfs(r,c+l,l)
            bottom_right=dfs(r+l,c+l,l)
            top_left=dfs(r,c,l)
            bottom_left=dfs(r+l,c,l)

            if(top_right.isLeaf and top_left.isLeaf and bottom_left.isLeaf and bottom_right.isLeaf and top_right.val==top_left.val==bottom_right.val==bottom_left.val):

                return Node(top_left.val,True)

            return Node(True, False, top_left, top_right, bottom_left, bottom_right)

        return dfs(0,0,len(grid))


