# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        nums1=[]
        nums2=[]
        
        while l1:
            nums1.append(l1.val)
            l1 = l1.next
        while l2:
            nums2.append(l2.val)
            l2 = l2.next
        i=0
        carry=0
        dummyNode=ListNode(-1)
        curr = dummyNode
        
        while i<len(nums1) or i<len(nums2) or carry:
            x = nums1[i] if i<len(nums1) else 0
            y = nums2[i] if i<len(nums2) else 0
            total = x+y+carry
            curr.next=ListNode(total%10)
            curr=curr.next
            carry=total//10
            i+=1
        return dummyNode.next