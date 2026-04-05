# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next
        
        dummy = node = ListNode()
        n = len(stack)
        i, j = 0, len(stack) - 1
        while i < j:
            stack[i].next = stack[j]
            i = i + 1
            if i >= j:
                break
            stack[j].next = stack[i]
            j = j - 1 
        stack[i].next = None