# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        arr=[]
        temp1=list1
        temp2=list2
        while temp1:
            arr.append(temp1.val)
            temp1=temp1.next
        while temp2:
            arr.append(temp2.val)
            temp2=temp2.next
        
        arr.sort()
        #convering the array back to linked list
        dummy=ListNode(0)
        tail=dummy
        for x in arr:
            tail.next=ListNode(x)
            tail=tail.next
        return dummy.next
