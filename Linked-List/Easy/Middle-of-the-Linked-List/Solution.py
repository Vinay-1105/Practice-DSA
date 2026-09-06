# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        cnt = 0
        while temp:
            cnt += 1
            temp = temp.next
        mid = (cnt//2) + 1
        temp = head
        while temp:
            mid = mid-1
            if mid == 0:
                break
            temp = temp.next
        return temp