# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return arr == arr[::-1]
        # slow = head
        # fast = head
        # while fast.next and fast.next.next:
        #     slow = slow.next
        #     fast = fast.next.next
        
        # curr = slow.next
        # slow.next = None

        # prev = None
        # next = None
        # while curr:
        #     next = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = next
        
        # while prev:
        #     if prev.val != head.val:
        #         return False
        #     prev = prev.next
        #     head = head.next
        # return True
        