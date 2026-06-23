# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(node, max_till):
            if not node:
                return 0
            good = 0
            if node.val >= max_till:
                good = 1
            l = helper(node.left, max(max_till, node.val))
            r = helper(node.right, max(max_till, node.val))
            return l + r + good
        return helper(root, float('-inf'))
    

