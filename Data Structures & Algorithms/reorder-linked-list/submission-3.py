# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]):
        def helper(front, back):
            if not back:
                return front
            front = helper(front, back.next)
            
            if not front:
                return None
            next_front = front.next
            if front.next == back or front == back:
                back.next = None
                return None
            
            front.next = back
            back.next = next_front
            return next_front
        helper(head, head.next)


