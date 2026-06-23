# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        gmax = [float('-inf')]
        def helper(node):
            if not node:
                return 0
            l = helper(node.left)
            r = helper(node.right)
            
            gmax[0] = max(gmax[0], l + r + node.val, max(l, r, 0) + node.val)
            return max(l, r, 0) + node.val
        helper(root)
        return gmax[0]