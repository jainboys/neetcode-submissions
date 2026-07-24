# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(-1)
        r = res
        carry = 0
        while l1 is not None or l2 is not None or carry:
            total = (l1.val if l1 else 0)+(l2.val if l2 else 0)+carry
            carry = 1 if total > 9 else 0
            res.next = ListNode(total%10)
            res = res.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        
        return r.next
            

