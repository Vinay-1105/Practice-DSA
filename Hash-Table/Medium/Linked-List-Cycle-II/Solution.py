# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Hum iss question ko Tortoise And Hare Algorithm se solve kar sakte hai
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next # Slow pointer moves one place at a time
            fast = fast.next.next # Whereas, fast pointer moves 2 places at a time
            if slow == fast: # hum yaha par check karte hai ki slow & fast have collided
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return fast
        return None