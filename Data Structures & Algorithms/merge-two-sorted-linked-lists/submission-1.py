# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = None
        head = None
        while list1 and list2:
            if list1.val < list2.val:
            
                if not temp:
                    temp = list1
                    head = temp
                else:
                    temp.next = list1
                    temp = temp.next
                
                list1 = list1.next
                temp.next = None
            else:
                if not temp:
                    temp = list2
                    head = temp
                else:
                    temp.next = list2
                    temp = temp.next
                

                list2 = list2.next
                temp.next = None
        while list1:
            if not temp:
                temp = list1
                head = temp
            else:
                temp.next = list1
                temp = temp.next
            
            list1 = list1.next 
            temp.next = None
        while list2:
            if not temp:
                temp = list2
                head = temp
            else:
                temp.next = list2
                temp = temp.next
            
            list2 = list2.next
            temp.next = None
        return head

