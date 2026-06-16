# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        heap = []
        if list1:
            heapq.heappush(heap, (list1.val, id(list1), list1))
        if list2:
            heapq.heappush(heap, (list2.val, id(list2), list2))
        th = None
        head = None
        while heap:
            min_node, _, ll = heapq.heappop(heap)
            if ll.next:
                heapq.heappush(heap, (ll.next.val, id(ll.next), ll.next))
            ll.next = None
            if not th:
                th = ll
                head = th
            else:
                th.next = ll
                th = th.next
          
            
        return head
            



