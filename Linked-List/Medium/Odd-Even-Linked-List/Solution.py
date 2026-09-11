# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        nums = []
        # First, to identify the odd nos. and taking them out
        temp = head
        while temp and temp.next:
            nums.append(temp.val)
            temp = temp.next.next
        if temp:
            nums.append(temp.val)
        
        # Second, to identify the even nos. and taking them out
        temp = head.next
        while temp and temp.next:
            nums.append(temp.val)
            temp = temp.next.next
        if temp:
            nums.append(temp.val)
        
        i = 0
        temp = head
        while temp:
            temp.val = nums[i]
            i += 1
            temp = temp.next
        return head