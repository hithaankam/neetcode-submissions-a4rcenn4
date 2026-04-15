# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        paths_2h = []
        def helper(root: TreeNode, greatest: int) -> None:
            if not root:
                return 0
            prev = greatest
            greatest = max(root.val, greatest)
            l = helper(root.left, greatest)
            r = helper(root.right, greatest)
            curr = 0
            if prev <= root.val:
                curr = 1 
            return l + r + curr
                
        return helper(root, -101)


