# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        temp1=headA
        temp2=headB
        len1=0
        len2=0

        while temp1:
            len1 += 1
            temp1 = temp1.next
        while temp2:
            len2 += 1
            temp2 = temp2.next
        
        #reset the pointers again
        temp1=headA
        temp2=headB
        skip1=max(0, len1-len2)
        skip2=max(0, len2-len1)

        # Skipping the starting nodes if any
        while skip1>0:
            temp1 = temp1.next
            skip1 -= 1
        while skip2>0:
            temp2 = temp2.next
            skip2 -= 1
        
        #Here, both the pointers are at the same distance from the end
        #Hum abh sath mai inko move karega jab hume intersection nahi milta
        while temp1 and temp2:
            if temp1==temp2:
                return temp1
            temp1=temp1.next
            temp2=temp2.next
        return None