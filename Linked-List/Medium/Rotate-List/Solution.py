# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def findNthNode(self, head, n):
        temp=head
        for i in range(n-1):
            temp=temp.next
        return temp

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        len=1
        tail=head
        while tail.next:
            len+=1
            tail=tail.next
        k=k%len
        if k==0:
            return head
        tail.next=head
        
        newLastNode=self.findNthNode(head, len-k)
        head=newLastNode.next
        newLastNode.next=None
        return head