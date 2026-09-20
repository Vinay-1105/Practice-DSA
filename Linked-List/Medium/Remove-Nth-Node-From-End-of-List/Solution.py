# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        # cnt=0
        # temp=head
        # while temp:
        #     cnt+=1
        #     temp=temp.next
        # if cnt == n:
        #     return head.next
        # res=cnt-n
        # temp=head
        # while temp:
        #     res-=1
        #     if res==0:
        #         break
        #     temp=temp.next
        # temp.next=temp.next.next
        # return head
        fast = head
        for _ in range(n):
            fast=fast.next
        if fast is None:
            return head.next
        slow=head
        while fast.next:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return head