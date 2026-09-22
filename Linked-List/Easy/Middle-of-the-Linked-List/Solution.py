# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        cnt=0
        temp=head
        while temp:
            cnt+=1
            temp=temp.next
        ans=cnt//2

        for i in range(ans):
            head=head.next
        return head