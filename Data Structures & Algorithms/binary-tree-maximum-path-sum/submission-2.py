# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        gmax = [float('-inf')]
        def helper(node: TreeNode) -> int:
            if not node:
                return 0
            l = helper(node.left)
            r = helper(node.right)
            #print(l, r)
            gmax[0] = max(gmax[0], l + r + node.val, node.val)
            #print(gmax[0])
            return max(l, r, 0) + node.val
        #print(gmax[0])
        return max(helper(root), gmax[0])
