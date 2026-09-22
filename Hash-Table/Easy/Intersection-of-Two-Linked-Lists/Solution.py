# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodeHash={}
        temp=headA
        while temp:
            nodeHash[temp]=1
            temp=temp.next
        
        temp=headB
        while temp:
            if temp in nodeHash:
                return temp
            temp=temp.next
        return None