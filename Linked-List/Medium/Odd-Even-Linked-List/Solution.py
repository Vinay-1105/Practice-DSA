# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case if the linked list is empty
        if head == None or head.next == None:
            return head
        # Optimized way can be to solve for odd and even simultaneously
        odd = head
        even = head.next
        evenHead = head.next
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        odd.next = evenHead 
        return head