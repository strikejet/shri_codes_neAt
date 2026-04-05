# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node_1 = list1
        node_2 = list2
        head = ListNode(0)
        curr = head
        while node_1 and node_2:
            if node_1.val < node_2.val:
                curr.next = node_1
                curr = curr.next
                node_1 = node_1.next
            else:
                curr.next = node_2
                curr = curr.next
                node_2 = node_2.next
        curr.next = node_1 or node_2
           
        return head.next