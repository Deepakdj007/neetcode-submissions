# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None: return False
        fast = head.next
        slow = head

        while fast:
            if slow.val == fast.val:
                return True
            fast = fast.next.next if fast.next else None
            slow = slow.next
        return False
        
