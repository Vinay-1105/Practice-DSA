# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = head
        nodeHash = {}
        while temp:
            if temp in nodeHash:
                return True
            nodeHash[temp] = 1
            temp = temp.next
        return False