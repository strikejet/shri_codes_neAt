# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        for _ in range(n):
            curr = curr.next

        left = head
        prev = None
        right = curr
        while right:
            prev = left
            left = left.next
            right = right.next

        if prev is None:
            return head.next
        prev.next = left.next
        return head
