# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(p, q):
            if not p and not q:
                return True
            if not p:
                return False
            if not q:
                return False
            if not (p.val == q.val):
                return False
            if not dfs(p.left, q.left):
                return False
            if not dfs(p.right, q.right):
                return False
            return True
        def traverse(root):
            if dfs(root, subRoot):
                return True
            if not root:
                return False
            if traverse(root.left):
                return True
            if traverse(root.right):
                return True
            return False
        return traverse(root)