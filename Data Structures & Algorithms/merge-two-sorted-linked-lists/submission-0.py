# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        a, b = list1, list2
        if a.val < b.val:
            a.next = self.mergeTwoLists(list1.next, list2)
            return a
        else:
            b.next = self.mergeTwoLists(list1, list2.next)
            return b
