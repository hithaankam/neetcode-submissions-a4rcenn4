# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        def helper(node):
            if not node:
                return
            heapq.heappush(heap, -node.val)
            if len(heap) > k:
                heapq.heappop(heap)
            helper(node.left)
            helper(node.right)
        helper(root)
        if heap:
            return -heap[0]