# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(node):
            if not node:
                return -1
            l = helper(node.left)
            r = helper(node.right)
            if l == float('inf') or r == float('inf'):
                return float('inf')
            if abs(l - r) > 1:
                return float('inf')
            return max(l, r) + 1
        if helper(root) == float('inf'):
            return False
        return True
            