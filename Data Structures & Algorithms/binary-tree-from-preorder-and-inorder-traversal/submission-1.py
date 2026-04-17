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
        pt = [0]
        def helper(curr, low, high):
            if not curr or pt[0] >= n:
                return None
  
            new_node = TreeNode(preorder[pt[0]])
            
            pos = positions[preorder[pt[0]]]
            pt[0] += 1
            #print(pos, low, high)
            new_node.left = helper(set(inorder[low:pos]), low, pos - 1)
            new_node.right = helper(set(inorder[pos + 1: high + 1]), pos + 1, high)
            return new_node
        return helper(set(inorder), 0, n - 1)
