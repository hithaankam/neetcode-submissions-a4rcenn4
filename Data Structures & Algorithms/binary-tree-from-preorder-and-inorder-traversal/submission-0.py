# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        positions = {}
        for i, val in enumerate(inorder):
            positions[val] = i
        n = len(inorder)
        def helper(curr, low, high):
            if not curr:
                return None
            for idx, num in enumerate(preorder):
                if num in curr:
                    pt = idx 
                    break
            new_node = TreeNode(preorder[pt])
            pos = positions[preorder[pt]]
            #print(pos, low, high)
            new_node.left = helper(set(inorder[low:pos]), low, pos - 1)
            new_node.right = helper(set(inorder[pos + 1: high + 1]), pos + 1, high)
            return new_node
        return helper(set(inorder), 0, n - 1)
