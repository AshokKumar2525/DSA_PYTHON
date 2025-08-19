# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        pre, cur, post = None, head, head.next

        while post:
            cur.next = pre
            pre, cur, post = cur, post, post.next

        cur.next = pre
        return cur
