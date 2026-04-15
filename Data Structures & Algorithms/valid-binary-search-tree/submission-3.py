# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, lb, ub):
            if not node:
                return True
           # print(node.val, lb, ub)
            if node.val >= ub or node.val <= lb:
                return False
            if not helper(node.left, lb, min(ub, node.val)):
                return False
            if not helper(node.right, max(lb, node.val), ub):
                return False
            return True
            
        return helper(root, float('-inf'), float('inf')) 