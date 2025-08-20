# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = slow = dummy

        # Move fast pointer n+1 steps ahead (to create gap of n)
        for _ in range(n + 1):
            fast = fast.next

        # Move fast to the end, keeping the gap
        while fast:
            slow = slow.next
            fast = fast.next

        # Skip the target node
        slow.next = slow.next.next

        return dummy.next
