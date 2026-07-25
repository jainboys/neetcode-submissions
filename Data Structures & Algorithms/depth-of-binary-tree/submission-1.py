# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        s = [(root, 1)]
        dmax = 0
        while s:
            r, d = s.pop()
            dmax = max(d, dmax)
            if r.left:
                s.append((r.left, d+1))
            if r.right:
                s.append((r.right, d+1))

        return dmax
        