"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        mp = {}
        if not node:
            return node
        def helper(node):
            
            new = Node(node.val)
            mp[node.val] = new
            for nei in node.neighbors:
                if nei.val in mp:
                    new.neighbors.append(mp[nei.val])
                else:
               
                    new.neighbors.append(helper(nei))
            return new

    
        helper(node)
        return mp[1]
