# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        def lo():
            queue = deque([])
            queue.append(root)
            queue.append(None)
            curr = []
            ans = []
            while queue:
                node = queue.popleft()
                if not node:
                    ans.append(curr[:])
                    if queue:
                        queue.append(node)
                    curr = []
                    continue
                    
                curr.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            return ans
        ans = lo()
        nc_1704 = []
        for level in ans:
            nc_1704.append(level[-1])
        return nc_1704