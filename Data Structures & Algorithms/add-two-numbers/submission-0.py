# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = l1
        n = 0
        num1 = 0 
        while node1:
            num1 += node1.val * (10**n)
            n = n + 1
            node1 = node1.next
        
        node2 = l2
        n = 0
        num2 = 0 
        while node2:
            num2 += node2.val * (10**n)
            n = n + 1
            node2 = node2.next
        
        res = num1 + num2
        res_str = str(res)
        head = node = ListNode(0)
        for i in res_str[::-1]:
            new_node = ListNode(int(i))
            node.next = new_node
            node = node.next
        
        return head.next