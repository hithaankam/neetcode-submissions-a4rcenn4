# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        node = head
        while node:
            stack.append(node)
            node = node.next
        head = None
        print(stack)
        while stack:
            top = stack.pop()
            #print(top.val)
            top.next = None
            if not head:
                head = top
                th = head
                continue
            th.next = top
            th = th.next
        return head
