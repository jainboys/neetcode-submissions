# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow = head
        fast = head.next.next if head.next else None
        while slow or fast:
            if slow == fast:
                return True
            slow = slow.next if slow else None
            fast = fast.next.next if fast and fast.next else None
        return False