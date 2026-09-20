# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        # First, we will convert the linked list to python list
        nums=[]
        temp=head
        while temp:
            nums.append(temp.val)
            temp = temp.next
        # Second, using two-pointer to check if it is palindrome or not
        left =0
        right=len(nums)-1
        while left<right:
            if nums[left] != nums[right]:
                return False
            left += 1
            right -= 1
        return True