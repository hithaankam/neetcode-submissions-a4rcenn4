# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        serial = [""]
        def dfs(node):
            if not node:
                serial[0] += "N,"
                return
            serial[0] += str(node.val) + ","
            dfs(node.left)
            
            dfs(node.right)
        #print(serial[0])
        dfs(root)
        return serial[0]
            
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        i = [0]
        values = data.split(",")
        n = len(values) - 1
        def dfs():
            if i[0]  >= n:
                return None
            if values[i[0]] == "N":
                i[0] += 1
                return None
            new = TreeNode(values[i[0]])
            i[0] += 1
            new.left = dfs()
            new.right = dfs()
            return new
   
        return dfs()