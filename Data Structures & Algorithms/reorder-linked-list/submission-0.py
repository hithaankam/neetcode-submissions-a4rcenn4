# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]):
        node = head
        nodes = []
        while node:
            nodes.append(node)
            node = node.next
        i, j = 0, len(nodes) - 1
        pt = None
        th = None
        while i <= j:
            front, back = nodes[i], nodes[j]
    
            if not pt:
                pt = front
                th = pt
            else:
                pt.next = front
            front.next = back
            back.next = None
            pt = back
            i += 1
            j -= 1
        if i == j:
            if not pt:
                pt = front
                th = pt
            else:
                pt.next = front
        

