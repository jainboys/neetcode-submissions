# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    dmax = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def get_height_util(root):
            if not root:
                return 0
            l = get_height_util(root.left)
            r = get_height_util(root.right)
            d = l + r
            self.dmax = max(d, self.dmax)
            return 1 + max(l, r)
        get_height_util(root)
        return self.dmax
            


