# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def size():
            s = 0
            node = head
            while node:
                node = node.next
                s += 1
            return s
        pos = size() - n
        idx = 0
        node = head
        if pos == 0:
            return head.next
        for i in range(pos - 1):
            node = node.next
        if node.next:
            node.next = node.next.next
        else:
            node.next = None
        return head
        
