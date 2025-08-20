# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
from typing import List, Optional

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for idx, node in enumerate(lists):
            if node:
                # Include the index to resolve cases where node.val is the same.
                heapq.heappush(heap, (node.val, idx, node))
        
        head = ListNode(0)
        cur = head
        while heap:
            val, idx, node = heapq.heappop(heap)
            cur.next = ListNode(val)
            cur = cur.next
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))
        return head.next
