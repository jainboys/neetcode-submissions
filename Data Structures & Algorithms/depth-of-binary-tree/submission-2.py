# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([(root, 1)])
        dmax = 0
        while q:
            r, d = q.popleft()
            dmax = max(d, dmax)
            if r.left:
                q.append((r.left, d+1))
            if r.right:
                q.append((r.right, d+1))

        return dmax
        