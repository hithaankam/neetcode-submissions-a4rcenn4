# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        gmax = [0]
        def helper(root):
            if not root:
                return -1
            
            l = helper(root.left) 
            r = helper(root.right)

            gmax[0] = max(gmax[0], l + r + 2)
            #print(root.val, max(l, r) + 1, l, r)
            return max(l, r) + 1
        helper(root)
        return gmax[0]
