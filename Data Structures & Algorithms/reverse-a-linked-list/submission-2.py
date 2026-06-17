# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rec_reverse(node):
            if not node:
                return node
            new_head = node
            if node.next:
                new_head = rec_reverse(node.next)
                node.next.next = node
            node.next = None
            return new_head
        return rec_reverse(head)