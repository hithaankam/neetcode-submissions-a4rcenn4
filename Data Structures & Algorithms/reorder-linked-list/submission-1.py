# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]):
        def find_mid():
            slow = fast = head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            return slow
        def reverseLL(th):
            prev = None
            curr = th
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev
        mid = find_mid()

        
        back = reverseLL(mid.next)
        mid.next = None
        front = head
        
        while front and back:
            next_front = front.next
            front.next = back
            next_back = back.next
            back.next = next_front
            front = next_front
            back = next_back
        

            


