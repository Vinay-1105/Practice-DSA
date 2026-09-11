# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # edge case
        if head == None or head.next == None:
            return head
        arr = []
        temp = head
        while temp and temp.next:
            arr.append(temp.val)
            temp = temp.next.next
        if temp:
            arr.append(temp.val)
        
        temp = head.next
        while temp and temp.next:
            arr.append(temp.val)
            temp = temp.next.next
        if temp:
            arr.append(temp.val)
        
        i = 0
        temp = head
        while temp:
            temp.val = arr[i]
            i += 1
            temp = temp.next
        return head

        